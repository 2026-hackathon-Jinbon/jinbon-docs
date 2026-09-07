# 환경 설정값

네 저장소의 설정 항목을 한곳에 모았습니다.

## 백엔드 `.env`

`.env.example`을 복사해 사용합니다. `application.yml`이 `optional:file:.env[.properties]`로 읽습니다.

| 키 | 기본값 | 필수 | 설명 |
|---|---|:---:|---|
| `DB_PASSWORD` | — | O | PostgreSQL 비밀번호 |
| `DB_PORT` | `5432` | | DB 포트 |
| `SERVER_PORT` | `8070` | | 백엔드 포트 |
| `JWT_SECRET` | — | O | 토큰 서명 **및 영상 서명** 키 |
| `CI_HMAC_SECRET` | — | O | CI 해싱 키. 32자 이상, JWT와 달라야 함 |
| `OMNIONE_CX_URL` | — | | OmniOne CX 서버 주소 |
| `BLOCKCHAIN_API_URL` | — | | 체인 API 주소 |
| `BLOCKCHAIN_API_TOKEN` | — | | 체인 API 토큰 |
| `BLOCKCHAIN_RPC_URL` | — | | JSON-RPC 엔드포인트 |
| `BLOCKCHAIN_NETWORK` | `omnione` | | 네트워크 이름. VC 클레임에 포함 |
| `BLOCKCHAIN_CHAIN_ID` | — | | 체인 ID. VC 클레임에 포함 |
| `CONTRACT_ADDRESS` | — | | 배포된 `JinBon.sol` 주소 |
| `WALLET_ADDRESS` | — | | 컨트랙트 배포 지갑 주소 |
| `KEYSTORE_PASSWORD` | — | | keystore 암호 |
| `OPENDID_ENABLED` | `.env.example`은 `false` | | VC 발급·검증 사용 여부 |
| `OPENDID_VC_CLAIM_NAMESPACE` | `ns-jinbon-video-01` | | VC 클레임 키 접두사 |

> `application.yml`의 기본값은 `OPENDID_ENABLED:true`이고 `.env.example`은 `false`입니다.
> `.env`를 복사해 쓰면 **Open DID가 꺼진 상태로 시작**합니다.

### 필수값 검증

`CI_HMAC_SECRET`은 `CiHasher.@PostConstruct`에서 길이를 확인합니다.
32자 미만이면 애플리케이션이 기동되지 않습니다.

```
IllegalStateException: CI_HMAC_SECRET must be at least 32 characters
```

### 파일 경로 설정

| 항목 | 경로 |
|---|---|
| 지갑 keystore | `src/main/resources/keystore/omnione-chain-keystore.json` |
| OmniOne CX 설정 | `/esign/config/config.mid.json` (CX 서버 기준 경로) |
| 인증 페이지 | `src/main/resources/static/auth.html` |

## 백엔드 `application.yml` 고정값

`.env`로 덮어쓸 수 없는 값들입니다.

| 설정 | 값 |
|---|---|
| `spring.jpa.hibernate.ddl-auto` | `update` |
| `spring.servlet.multipart.max-file-size` | `100MB` |
| `spring.servlet.multipart.max-request-size` | `110MB` |
| `spring.data.redis.host` / `port` | `localhost` / `6380` |
| `jwt.access-expiration` | `1800000` (30분) |
| `jwt.refresh-expiration` | `604800000` (7일) |
| `opendid.issuer-server-url` | `http://localhost:8091` |
| `opendid.verifier-server-url` | `http://localhost:8092` |
| `opendid.vc-plan-id` | `vcplan-jinbon-01` |
| `opendid.issuer-did` | `did:omn:issuer` |
| `blockchain.keystore-path` | `classpath:keystore/omnione-chain-keystore.json` |
| `logging.level.com.jinbon` | `DEBUG` |
| `logging.level.org.hibernate.SQL` | `DEBUG` |

Redis 호스트·포트와 Open DID 서버 주소가 하드코딩되어 있어
다른 호스트로 옮기려면 `application.yml` 수정이 필요합니다.

### 프로필 관련

| 설정 | 영향 |
|---|---|
| 활성 프로필 없음 또는 `dev` | Swagger UI, `/v3/api-docs`, `/auth.html` 공개 |
| 그 외 프로필 | 위 경로 모두 인증 필요 |
| `cors.allowed-origins` 미설정 | 모든 오리진 허용 |
| `cors.allowed-origins` 설정 | 쉼표로 구분한 오리진만 허용 |

## docker-compose

| 서비스 | 이미지 | 포트 | 볼륨 |
|---|---|---|---|
| `jinbon-postgres` | `postgres:16.4` | `${DB_PORT:-5432}:5432` | `jinbon_postgres_data` |
| `jinbon-redis` | `redis:7-alpine` | `6380:6379` | `jinbon_redis_data` |

PostgreSQL 환경변수는 `POSTGRES_USER=jinbon`, `POSTGRES_DB=jinbon`,
`POSTGRES_PASSWORD=${DB_PASSWORD:-jinbon}`입니다.

Redis 호스트 포트가 6380인 이유는 로컬에 이미 돌고 있을 수 있는
기본 Redis(6379)와 충돌을 피하기 위함입니다.

## 웹 `.env.local`

| 키 | 기본값 | 설명 |
|---|---|---|
| `NEXT_PUBLIC_API_BASE_URL` | `http://localhost:8070` | 백엔드 주소 |

`NEXT_PUBLIC_` 접두사가 붙어 있어 **빌드 시점에 번들에 박힙니다.**
런타임에 바꿀 수 없고, 주소를 바꾸려면 다시 빌드해야 합니다.

### 개발 포트

`package.json`의 스크립트에 `--port 8071`이 고정되어 있습니다.

```json
"dev": "WRANGLER_LOG_PATH=.wrangler/wrangler.log vinext dev --port 8071"
```

## iOS xcconfig

`source/DIDCA/Configuration/` 아래 두 파일입니다.

| 키 | Dev | Prod | 용도 |
|---|---|---|---|
| `JINBON_URL` | `http://10.48.200.183:8070` | `https://jinbon.example.com` | 진본 백엔드 |
| `TAS_URL` | `http://10.48.200.183:8090` | `https://jinbon-tas.example.com` | Trust Agent |
| `VERIFIER_URL` | `http://10.48.200.183:8092` | `https://jinbon-verifier.example.com` | VC 검증 |
| `CAS_URL` | `http://10.48.200.183:8094` | `https://jinbon-cas.example.com` | CA |
| `WALLET_URL` | `http://10.48.200.183:8095` | `https://jinbon-wallet.example.com` | Wallet 서버 |
| `API_URL` | `http://10.48.200.183:8093` | `https://jinbon-api.example.com` | API Gateway |
| `DEMO_URL` | `http://10.48.200.183:8099` | `https://jinbon-demo.example.com` | Demo |

### URL 표기 규칙

```
JINBON_URL = http:/$()/10.48.200.183:8070
```

xcconfig는 `//`를 주석 시작으로 해석합니다. 중간에 `$()`(빈 변수 치환)를 끼워 넣어
파싱을 피하는 관용 표현입니다. **이 부분을 지우면 URL이 `http:`로 잘립니다.**

### ATS 설정

`Info.plist`에 다음이 들어 있습니다.

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

HTTP 통신을 위한 임시 설정이며, xcconfig 주석에도
프로덕션 배포 전 `<false/>`로 바꾸라고 적혀 있습니다.

### 빌드 설정

| 항목 | 값 |
|---|---|
| `IPHONEOS_DEPLOYMENT_TARGET` | 15 (앱 타깃) |
| `SWIFT_VERSION` | 5.0 |
| `MARKETING_VERSION` | 1.0 |

## 확장 `manifest.json`

| 항목 | 값 | 변경이 필요한 경우 |
|---|---|---|
| `host_permissions` | `http://localhost:8070/*` 외 YouTube·Netflix | 백엔드 주소가 바뀌면 반드시 추가 |
| `permissions` | `storage`, `activeTab` | — |
| `content_scripts.matches` | YouTube, Netflix | 지원 사이트 추가 시 |
| `version` | `0.1.0` | 배포 시 |

### 런타임 설정

`chrome.storage.sync`의 `apiBaseUrl` 키로 백엔드 주소를 저장합니다.
확장 아이콘 → 팝업에서 변경할 수 있습니다.

```js
const { apiBaseUrl = 'http://localhost:8070' } =
  await chrome.storage.sync.get({ apiBaseUrl: 'http://localhost:8070' });
```

팝업에서 주소를 바꿔도 `host_permissions`에 없는 호스트면 요청이 차단됩니다.
두 곳을 함께 맞춰야 합니다.

## 설정 변경 시 영향 범위

| 바꾸는 값 | 파급 |
|---|---|
| `JWT_SECRET` | **기존 등록 영상 전체의 서명 검증이 깨집니다.** 로그인 세션도 전부 무효 |
| `CI_HMAC_SECRET` | **기존 회원 전체를 찾을 수 없게 됩니다.** 사실상 변경 불가 |
| `CONTRACT_ADDRESS` | 이전 컨트랙트에 기록된 영상의 검증이 실패 |
| `SERVER_PORT` | 웹 `.env.local`, 확장 팝업·manifest, iOS xcconfig를 모두 수정 |
| `DB_PORT` | docker-compose와 `.env` 양쪽 |
| `OPENDID_ENABLED` | `false`로 바꾸면 이미 발급된 VC의 검증도 중단(`DISABLED`) |
