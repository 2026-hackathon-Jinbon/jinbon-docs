# 백엔드 구조

저장소: `jinbon-backend` · 패키지 루트: `com.jinbon`

## 패키지 구성

```
src/main/java/com/jinbon/
├── JinbonApplication.java
├── domain/
│   ├── auth/
│   │   ├── controller/   AuthController, AuthApi, SignupController
│   │   ├── dto/          VerifyRequest, AuthResponse, RefreshRequest 등
│   │   └── service/      AuthService, JwtTokenProvider, RefreshTokenService,
│   │                     DidRebindTokenService, CiHasher, CiHashMigration
│   ├── member/
│   │   ├── entity/       Member, MemberRole, MemberStatus
│   │   └── repository/   MemberRepository
│   └── video/
│       ├── controller/   VideoRegisterController(+Api), VideoVerifyController(+Api)
│       ├── dto/          VideoRegisterResponse, VideoVerifyResponse,
│       │                 VerificationVerdict, UrlVerifyRequest 등
│       ├── entity/       Video, VcIssuanceStatus
│       ├── repository/   VideoRepository
│       └── service/      VideoRegisterService, VideoVerifyService, HashService,
│                         PerceptualHashService, SignatureService, VideoCertificateClaims
├── global/
│   ├── common/           CommonResponse
│   ├── config/           SecurityConfig, JwtAuthenticationFilter, JwtProperties,
│   │                     BlockchainProperties, OpenDidProperties, PrivacyProperties
│   └── error/            ErrorCode, BusinessException, 예외 핸들러
└── infra/
    ├── blockchain/       OmniOneChainClient, ContractEncoder, ContractDecoder
    ├── download/         VideoDownloadService
    ├── omnione/          OmniOneCxClient, OmniOneCxApi
    └── opendid/          OpenDidIssuerClient, OpenDidTasClient,
                          VcIssuanceService, VcVerificationService
```

컨트롤러는 `XxxApi` 인터페이스와 `XxxController` 구현으로 나뉩니다.
Swagger 애너테이션은 인터페이스에 모여 있어 구현체는 라우팅과 위임만 담당합니다.

## 핵심 서비스

### VideoRegisterService

영상 등록의 전 과정을 조율합니다.

1. 회원 조회 후 `ISSUER` 역할과 `userDid` 존재 확인
2. fineHash 계산 → 동일 fineHash 기존 영상 확인
   - 같은 회원 → 기존 결과 반환 (`alreadyRegistered=true`)
   - 다른 회원 → `VIDEO_ALREADY_REGISTERED`(409) 차단
3. perceptualHash 계산 → 양방향 거리가 0인 영상을 같은 콘텐츠로 판정
4. merkleRoot · merklePath · signature 생성
5. **DB에 먼저 저장 (`saveAndFlush`)** → fineHash unique 제약으로 등록 권한 선점
6. 선점 성공한 요청만 온체인 `register` 트랜잭션 전송
7. 영수증을 최대 20회(250ms 간격) 폴링해 `blockNumber` 확보
8. 온체인 기록 대조 후 VC 발급 준비 시도

::: tip DB 먼저, 블록체인 나중
5번과 6번의 순서가 핵심입니다. 블록체인 전송을 먼저 하면 동시 요청이 여러 트랜잭션을 만들 수 있으므로, DB 제약으로 먼저 걸러냅니다.
:::

VC 발급 준비는 `try/catch`로 감싸 실패해도 등록은 유지됩니다.

### VideoVerifyService

검증 로직과 SSRF 방어를 함께 담당합니다.

- 캐시 키: `verify:result:{fineHash}` 또는 `verify:result:url:{sha256(url)}`
- 영상별 캐시 인덱스: `verify:video:{videoId}` (Set) — 비활성화 시 일괄 무효화
- TTL 10분, `VERIFICATION_UNAVAILABLE`은 캐싱 제외
- 유사도 검색은 `findByActiveTrue()`로 활성 영상 전체를 메모리에 올려 비교 (MVP 방식)

### PerceptualHashService

| 상수 | 값 | 의미 |
|---|---|---|
| `MAX_FRAMES` | 10 | 추출할 최대 프레임 수 |
| `FRAME_INTERVAL_SECONDS` | 2.0 | 프레임 추출 간격(초) |
| `DCT_SIZE` | 32 | DCT 계산용 이미지 크기 |
| `HASH_SIZE` | 8 | 저주파 영역 크기 (64비트 해시) |
| `SIMILARITY_THRESHOLD` | 10 | 동일 영상 판정 해밍 거리 임계값 |

프레임 추출은 JavaCV의 `FFmpegFrameGrabber`를 사용합니다.

### HashService · SignatureService

- `generateFineHash(InputStream)` — 8KB 버퍼로 스트리밍 SHA-256
- `buildMerkleRoot(pHash, fineHash)` — `SHA-256(pHash || fineHash)`
- `sign(data)` — `HMAC-SHA256(data)`, 키는 **JWT secret을 재사용**

::: warning 서명 키 = JWT 키
서명 키가 JWT secret과 같아 키 로테이션이 사실상 불가능합니다. 자세한 내용은 [보안 문서](/developers/security/overview)를 참고하세요.
:::

## 공통 응답 포맷

모든 API는 `CommonResponse<T>`로 감싸 응답합니다. `code`는 성공 시 생략, 실패 시 `ErrorCode` 문자열이 들어갑니다.

## 보안 설정

| 경로 | 인증 |
|---|---|
| `/api/auth/**`, `/api/signup/**`, `/api/verify/**` | 불필요 |
| `/swagger-ui/**`, `/v3/api-docs/**`, `/auth.html` | **개발 프로필에서만** 허용 |
| 그 외 전체 | JWT 필요 |

활성 프로필을 지정하지 않으면 개발 모드로 간주되어 Swagger가 공개됩니다.

## 업로드 제한

파일 100MB, 요청 110MB. 초과 시 `UPLOAD_SIZE_EXCEEDED`(C002, 413).
