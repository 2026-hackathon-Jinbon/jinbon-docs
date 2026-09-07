# 백엔드 구조

저장소: `jinbon-backend` · 패키지 루트: `com.jinbon`

## 패키지 구성

```
src/main/java/com/jinbon/
├── JinbonApplication.java
├── domain/
│   ├── auth/
│   │   ├── controller/   AuthController, AuthApi, SignupController
│   │   ├── dto/          VerifyRequest, AuthResponse, RefreshRequest,
│   │   │                 RebindDidRequest, CompleteSignupRequest, SignupIdentityResponse
│   │   └── service/      AuthService, JwtTokenProvider, RefreshTokenService,
│   │                     DidRebindTokenService, CiHasher, CiHashMigration
│   ├── member/
│   │   ├── entity/       Member, MemberRole, MemberStatus
│   │   └── repository/   MemberRepository
│   └── video/
│       ├── controller/   VideoRegisterController(+Api), VideoVerifyController(+Api)
│       ├── dto/          VideoRegisterResponse, VideoDetailResponse, VideoVerifyResponse,
│       │                 VerificationVerdict, UrlVerifyRequest, CompleteVideoVcRequest
│       ├── entity/       Video, VcIssuanceStatus
│       ├── repository/   VideoRepository
│       └── service/      VideoRegisterService, VideoVerifyService, HashService,
│                         PerceptualHashService, SignatureService, VideoCertificateClaims
├── global/
│   ├── common/           CommonResponse
│   ├── config/           SecurityConfig, JwtAuthenticationFilter, JwtProperties,
│   │                     BlockchainProperties, OpenDidProperties, PrivacyProperties, Redis 설정
│   └── error/            ErrorCode, BusinessException, 예외 핸들러
└── infra/
    ├── blockchain/       OmniOneChainClient, ContractEncoder, ContractDecoder
    ├── download/         VideoDownloadService
    ├── omnione/          OmniOneCxClient, OmniOneCxApi, dto/
    └── opendid/          OpenDidIssuerClient/Api, OpenDidVerifierClient/Api,
                          VcIssuanceService, VcVerificationService
```

`domain/member/controller`, `domain/member/service`, 최상위 `config` 디렉터리는
현재 비어 있습니다.

컨트롤러는 `XxxApi` 인터페이스와 `XxxController` 구현으로 나뉩니다.
Swagger 애너테이션은 전부 인터페이스에 모여 있어 구현체는 라우팅과 위임만 담당합니다.

## 핵심 서비스

### VideoRegisterService

영상 등록의 전 과정을 조율합니다. 순서가 중요합니다.

1. 회원 조회 후 `ISSUER` 역할과 `userDid` 존재를 확인
2. fineHash 계산 → 동일 fineHash 기존 영상 확인
   - 같은 회원이면 기존 결과를 그대로 반환(`alreadyRegistered=true`)
   - 다른 회원이면 `VIDEO_ALREADY_REGISTERED`(409)로 차단
3. perceptualHash 계산 → 내용이 완전히 같은 영상 확인
   - 양방향 거리가 모두 0인 영상을 같은 콘텐츠로 판정
   - 소유자 판정 규칙은 2번과 동일
4. merkleRoot·merklePath·signature 생성
5. **DB에 먼저 저장(`saveAndFlush`)** 하여 fineHash unique 제약으로 등록 권한을 선점
6. 선점에 성공한 요청만 온체인 `register` 트랜잭션 전송
7. 트랜잭션 영수증을 최대 20회(250ms 간격) 폴링해 `blockNumber` 확보
8. 온체인 기록을 다시 조회해 DB 값과 대조 후 VC 발급 준비 시도

5번과 6번의 순서가 핵심입니다. 블록체인 전송을 먼저 하면 동시 중복 요청이
같은 영상에 대해 여러 트랜잭션을 발생시킬 수 있으므로, DB 제약으로 먼저 걸러냅니다.

VC 발급 준비는 `try/catch`로 감싸 실패해도 등록은 유지됩니다.

### VideoVerifyService

검증 로직과 SSRF 방어를 함께 담당합니다.

- 캐시 키: `verify:result:{fineHash}` 또는 `verify:result:url:{sha256(url)}`
- 영상별 캐시 인덱스: `verify:video:{videoId}` (Set) — 비활성화 시 일괄 무효화용
- TTL 10분, `VERIFICATION_UNAVAILABLE`은 캐싱 제외
- 유사도 검색은 `findByActiveTrue()`로 활성 영상 전체를 메모리에 올려 비교 (MVP 방식)

URL 검증은 다음 조건을 모두 통과해야 다운로드로 진행합니다.

- 스킴이 `https`
- 호스트가 허용 목록에 포함: `youtube.com`, `youtu.be`, `instagram.com`, `tiktok.com`, `twitter.com`, `x.com`, `vimeo.com`
- userInfo 없음, 명시적 포트 없음
- DNS 응답의 **모든** IP가 사설·루프백·링크로컬·멀티캐스트가 아님

### PerceptualHashService

| 상수 | 값 | 의미 |
|---|---|---|
| `MAX_FRAMES` | 10 | 추출할 최대 프레임 수 |
| `FRAME_INTERVAL_SECONDS` | 2.0 | 프레임 추출 간격(초) |
| `DCT_SIZE` | 32 | DCT 계산용 이미지 크기 |
| `HASH_SIZE` | 8 | 저주파 영역 크기 (64비트 해시) |
| `SIMILARITY_THRESHOLD` | 10 | 동일 영상 판정 해밍 거리 임계값 |

프레임 추출은 JavaCV의 `FFmpegFrameGrabber`를 사용합니다.
유사도는 각 프레임에 대해 최근접 매칭을 찾아 평균 해밍 거리를 계산합니다.

### HashService · SignatureService

- `generateFineHash(InputStream)` — 8KB 버퍼로 스트리밍 SHA-256
- `buildMerkleRoot(pHash, fineHash)` — `SHA-256(pHash || fineHash)`
- `buildMerklePath(...)` — `{"leaves": [...], "root": ...}` JSON
- `sign(data)` — `HMAC-SHA256(data)`, 키는 **JWT secret을 재사용**

서명 키가 JWT secret과 동일하다는 점은 설계상 주의가 필요합니다.
자세한 내용은 [보안 문서](../50-security/security-and-privacy.md)를 참고합니다.

## 공통 응답 포맷

모든 API는 `CommonResponse<T>`로 감싸 응답합니다.

```json
{
  "status": 200,
  "message": "Success",
  "data": { }
}
```

`code`는 성공 시 `null`이며 `@JsonInclude(NON_NULL)`로 직렬화에서 빠집니다.
실패 시 `code`에 `ErrorCode`의 코드 문자열이 들어갑니다.

## 보안 설정

`SecurityConfig`의 규칙입니다.

| 경로 | 인증 |
|---|---|
| `/api/auth/**` | 불필요 |
| `/api/signup/**` | 불필요 |
| `/api/verify/**` | 불필요 |
| `/health`, `/favicon.ico` | 불필요 |
| `/swagger-ui/**`, `/v3/api-docs/**`, `/auth.html` | **개발 프로필에서만** 허용 |
| 그 외 전체 | JWT 필요 |

- 세션은 `STATELESS`, CSRF 비활성화
- CORS는 `cors.allowed-origins` 미설정 시 전체 허용(개발 모드), 설정 시 목록 제한
- 인증 실패는 401, 권한 부족은 403

개발 프로필 판정은 활성 프로필에 `dev`가 있거나 **활성 프로필이 하나도 없을 때**입니다.
즉 프로필을 지정하지 않고 띄우면 Swagger와 `/auth.html`이 열립니다.

## 업로드 제한

`application.yml`에서 파일 100MB, 요청 110MB로 제한합니다.
초과 시 `UPLOAD_SIZE_EXCEEDED`(C002, 413)를 반환합니다.

## 관련 문서

- [API 명세](../30-api/backend-api.md)
- [데이터 모델](../40-data/data-model.md)
- [환경 설정값](../60-operations/environment-config.md)
