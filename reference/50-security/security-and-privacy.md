# 보안 · 개인정보

## 저장하지 않는 데이터

진본이 의도적으로 저장하지 않는 것들입니다.

| 데이터 | 처리 |
|---|---|
| 영상 원본 파일 | 해시 계산 후 즉시 삭제. DB·디스크에 남기지 않음 |
| CI 원문 | HMAC-SHA256 해시만 저장 (`h1:` 접두사) |
| 지각해시 임시 파일 | `jinbon-phash-*.tmp`, `finally`에서 삭제 |
| URL 다운로드 영상 | 해시 계산 후 `cleanup()`으로 삭제 |

웹 화면에도 "영상 원본은 서버에 저장되지 않습니다."라는 문구를 노출합니다.

## CI 보호

```
저장값 = "h1:" + HMAC-SHA256(CI, CI_HMAC_SECRET)
```

- 담당: `CiHasher`
- 키: `privacy.ci-hmac-secret` (`CI_HMAC_SECRET`)
- 용도: 회원 중복 확인, 로그인 시 회원 조회, DID 복구
- **VC·DID Document·블록체인에는 포함되지 않습니다.**

`CI_HMAC_SECRET`은 32자 이상이어야 하고 `JWT_SECRET`과 반드시 달라야 합니다.
`application.yml`에 이 요구사항이 주석으로 명시되어 있으며, 미설정 시 기동에 실패합니다.

이 키는 **변경하거나 분실하면 안 됩니다.** 키가 바뀌면 같은 CI가 다른 해시를 만들어
기존 회원을 찾지 못하고, 사실상 전 회원의 로그인이 불가능해집니다.

레거시 평문 CI는 `CiHashMigration`이 `Member.migrateCiHash()`로 일괄 전환합니다.

## 서명 키

영상 서명은 `SignatureService`가 HMAC-SHA256으로 만듭니다.

```java
SecretKeySpec keySpec = new SecretKeySpec(
    jwtProperties.getSecret().getBytes(UTF_8), "HmacSHA256");
```

서명 키가 **JWT secret과 같습니다.**

이 때문에 다음 결과가 따라옵니다.

- `JWT_SECRET`을 교체하면 기존에 등록된 모든 영상의 서명 재계산이 달라집니다.
- 재계산 결과가 DB·온체인 값과 어긋나므로 **모든 영상 검증이 `VERIFICATION_UNAVAILABLE`이 됩니다.**
- 즉 JWT 키 로테이션이 사실상 불가능합니다.

토큰 서명용 키와 영상 서명용 키는 수명 주기와 노출 범위가 다르므로 분리하는 편이 안전합니다.
자세한 내용은 [알려진 이슈](../90-status/open-issues.md)에 기록했습니다.

## 인증과 인가

### 경로별 정책 (`SecurityConfig`)

| 경로 | 인증 |
|---|---|
| `/api/auth/**`, `/api/signup/**`, `/api/verify/**` | 불필요 |
| `/health`, `/favicon.ico` | 불필요 |
| `/swagger-ui/**`, `/v3/api-docs/**`, `/auth.html` | 개발 프로필에서만 |
| 그 외 | JWT 필요 |

- 세션 `STATELESS`, CSRF 비활성 (토큰 기반이므로 세션 쿠키 없음)
- 인증 실패 401 `Authentication required`, 권한 부족 403 `Access denied`

### 개발 프로필 판정

```java
boolean isDev = activeProfiles.contains("dev") || activeProfiles.length == 0;
```

**활성 프로필을 지정하지 않으면 개발 모드로 간주**됩니다.
`./gradlew bootRun`을 그냥 실행하면 Swagger와 `/auth.html`이 공개됩니다.
운영 환경에서는 `SPRING_PROFILES_ACTIVE=prod`처럼 프로필을 반드시 명시해야 합니다.

### 토큰

| 토큰 | 만료 | 무효화 |
|---|---|---|
| access | 30분 | 만료까지 유효 (서버 폐기 불가) |
| refresh | 7일 | 로그아웃·로테이션 시 즉시 무효 |
| signup | 단기 | 가입 완료 시 소비 |
| did-rebind | 단기 | 재연결 시 소비 |

토큰 타입은 JWT claim `type`으로 구분하며, 용도가 다른 토큰을 넣으면
`NOT_A_REFRESH_TOKEN` / `NOT_A_SIGNUP_TOKEN` / `NOT_A_DID_REBIND_TOKEN`으로 거부됩니다.

**Refresh Token Rotation**이 적용되어 갱신 시 이전 refreshToken은 즉시 폐기됩니다.
이미 쓴 토큰을 다시 제출하면 `REFRESH_TOKEN_EXPIRED`(A004, 401)입니다.

### 소유권 검사

영상 API는 역할 검사와 별개로 매 요청 소유권을 확인합니다.

```
findOwnedVideo(videoId, memberId)
  → memberId 불일치이고 레거시 소유도 아니면 VIDEO_NOT_OWNED (V006, 403)
```

VC 발급 완료는 여기에 더해 `vcOfferId` 일치까지 확인해
다른 영상의 VC를 잘못 연결하는 것을 막습니다.

## SSRF 방어

URL 검증은 서버가 외부 주소로 요청을 보내므로 SSRF 위험이 있습니다.
`VideoVerifyService.validateUrl()`이 네 겹으로 막습니다.

| 단계 | 규칙 |
|---|---|
| 1 | 스킴이 `https`여야 함 (HTTP 차단) |
| 2 | 호스트가 허용 목록에 있어야 함 |
| 3 | `userInfo` 없음, 명시적 포트 없음 |
| 4 | DNS 응답의 **모든** IP가 공인 IP여야 함 |

허용 호스트: `youtube.com`, `youtu.be`, `instagram.com`, `tiktok.com`,
`twitter.com`, `x.com`, `vimeo.com` (정확히 일치하거나 서브도메인)

4단계에서 차단하는 주소 유형:

```java
address.isLoopbackAddress()   // 127.x, ::1
address.isSiteLocalAddress()  // 10.x, 172.16-31.x, 192.168.x
address.isLinkLocalAddress()  // 169.254.x — 클라우드 메타데이터
address.isAnyLocalAddress()   // 0.0.0.0
address.isMulticastAddress()
```

`getAllByName()`으로 받은 모든 IP를 검사하는 것이 핵심입니다.
공인 IP와 사설 IP를 섞어 응답하는 DNS 리바인딩을 막습니다.

한계: DNS 조회와 실제 다운로드 사이에 응답이 바뀌는 TOCTOU 공격은 남아 있습니다.
호스트 허용 목록이 이를 실질적으로 제한합니다.

## 리소스 보호

| 대상 | 조치 |
|---|---|
| 업로드 크기 | 파일 100MB, 요청 110MB |
| URL 길이 | 최대 2048자 |
| `vcId` / `offerId` | 각 500자 |
| Redis 캐시 키 | URL을 SHA-256 해싱해 키 길이 고정 |
| 블록체인 폴링 | 250ms × 20회에서 중단 |

## 동시성 방어

같은 영상에 대한 동시 등록 요청이 여러 트랜잭션을 만들지 않도록
**DB 저장을 블록체인 전송보다 먼저** 수행합니다.

```java
videoRepository.saveAndFlush(video);   // unique 제약으로 선점
// 여기서 걸러진 요청만
sendBlockchainTx(...);
```

`DataIntegrityViolationException`은 `VIDEO_ALREADY_REGISTERED`(409)로 변환합니다.

## 로깅

해시와 서명은 로그에 전체를 남기지 않습니다.

```java
log.debug("Fine hash generated - fineHash={}", fineHash.substring(0, 16) + "...");
```

앞 16자만 기록합니다. CI·토큰·개인정보는 로그에 남기지 않습니다.

다만 `logging.level`이 `com.jinbon: DEBUG`, `org.hibernate.SQL: DEBUG`이고
`spring.jpa.show-sql: true`입니다. 운영 환경에서는 낮춰야 합니다.

## CORS

```yaml
cors.allowed-origins: ""   # 미설정 시 전체 허용 (개발 모드)
```

미설정 상태로 배포하면 모든 오리진이 API를 호출할 수 있습니다.
검증 API는 공개라 큰 문제가 아니지만, 운영에서는 웹 도메인과
확장 오리진(`chrome-extension://{id}`)만 허용하도록 지정해야 합니다.

## 키와 비밀값 목록

| 항목 | 위치 | 비고 |
|---|---|---|
| `JWT_SECRET` | `.env` | 토큰 서명 + **영상 서명 겸용** |
| `CI_HMAC_SECRET` | `.env` | 32자 이상, JWT와 달라야 함, 변경 금지 |
| `DB_PASSWORD` | `.env` | |
| `KEYSTORE_PASSWORD` | `.env` | 블록체인 지갑 keystore 암호 |
| `BLOCKCHAIN_API_TOKEN` | `.env` | OmniOne Chain API 토큰 |
| 지갑 keystore | `src/main/resources/keystore/omnione-chain-keystore.json` | **컨트랙트 배포 지갑과 동일해야 함** |

keystore가 소스 트리 안(`src/main/resources`)에 있어 빌드 산출물 JAR에 포함됩니다.
`.gitignore`로 커밋은 막고 있으나, 배포 시에는 외부 볼륨이나 시크릿 매니저로
분리하는 편이 안전합니다.

## 클라이언트 측 주의

### iOS

- `Info.plist`의 `NSAllowsArbitraryLoads`가 열려 있어 HTTP 통신을 허용합니다.
  `Dev.xcconfig`가 `http://10.48.200.183:*`를 쓰기 때문이며,
  두 xcconfig 파일 모두 프로덕션 배포 전 수정이 필요하다고 주석에 적혀 있습니다.
- 토큰은 `Properties`를 통해 로컬에 저장되며 Keychain 헬퍼(`KeychainHelper`)가 함께 있습니다.
- Wallet 잠금 해제에 PIN과 생체인증(`BiometricAuthenticator`)을 사용합니다.
- `WalletAccountValidator`가 기기 Wallet DID와 서버 계정 DID를 대조해
  다른 계정의 Wallet 연결을 차단합니다.

### 확장

- 결과 패널의 모든 삽입값은 `escapeHtml()`을 거칩니다.
- `host_permissions`가 `localhost:8070`으로 고정되어 있어
  임의 호스트로 요청을 보낼 수 없습니다(권한 자체가 없음).

### 웹

- 업로드 전 파일 타입(`video/`)과 크기(100MB)를 검사합니다.
- 백엔드 주소는 빌드 시점 환경변수(`NEXT_PUBLIC_API_BASE_URL`)로 고정됩니다.
