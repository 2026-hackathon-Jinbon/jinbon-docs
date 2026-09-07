# 클라이언트 API 매트릭스

어느 채널이 어떤 엔드포인트를 실제로 호출하는지 코드에서 확인한 결과입니다.

## 전체 매트릭스

| 엔드포인트 | iOS 앱 | 인증 웹페이지 | 웹 | 확장 |
|---|:---:|:---:|:---:|:---:|
| `POST /api/auth/token` | — | O | — | — |
| `POST /api/auth/app/request` | — | O | — | — |
| `POST /api/auth/app/verify` | — | O | — | — |
| `POST /api/auth/did/rebind` | O | — | — | — |
| `POST /api/auth/refresh` | O | — | — | — |
| `POST /api/auth/logout` | O | — | — | — |
| `POST /api/signup/token` | — | O | — | — |
| `POST /api/signup/app/request` | — | O | — | — |
| `POST /api/signup/app/verify` | — | O | — | — |
| `POST /api/signup/did/complete` | O | — | — | — |
| `POST /api/videos` | O | — | — | — |
| `GET /api/videos` | O | — | — | — |
| `GET /api/videos/{id}` | — | — | — | — |
| `POST /api/videos/{id}/vc/prepare` | O | — | — | — |
| `POST /api/videos/{id}/vc/complete` | O | — | — | — |
| `PATCH /api/videos/{id}/deactivate` | O | — | — | — |
| `POST /api/verify` | O | — | O | — |
| `POST /api/verify/url` | O | — | — | O |

**인증 웹페이지**는 백엔드가 서빙하는 `src/main/resources/static/auth.html`입니다.
iOS 앱이 `AuthWebViewController`의 `WKWebView`로 이 페이지를 띄웁니다.
따라서 OmniOne CX 3단계는 앱의 네이티브 코드가 아니라 **이 페이지 안의 자바스크립트**가 호출합니다.

```
mode == signup  →  /auth.html?mode=signup  →  apiPrefix = '/api/signup'
mode == login   →  /auth.html              →  apiPrefix = '/api/auth'
```

두 모드가 같은 페이지를 공유하고 접두사만 바꿉니다.

## 채널별 요약

### iOS 앱 (`JinBonAPIClient`)

10개 엔드포인트를 호출합니다. 유일하게 등록·관리 API를 쓰는 채널입니다.

| 화면 | 호출 |
|---|---|
| 시작 / 인증 완료 후 | `signup/did/complete`, `auth/did/rebind` |
| 홈 | `GET /api/videos` (최근 등록 표시) |
| 내 영상 | `GET /api/videos`, `vc/prepare`, `deactivate` |
| 영상 등록 | `POST /api/videos`, `vc/prepare`, `vc/complete` |
| 영상 검증 | `POST /api/verify` |
| 설정(로그아웃) | `POST /api/auth/logout` |

`GET /api/videos/{videoId}`(상세 조회)는 **어느 클라이언트도 호출하지 않습니다.**
앱의 목록 조회 응답에 이미 상세 필드가 모두 들어 있어 별도 조회가 필요 없습니다.

### 웹 (`app/page.tsx`)

`POST /api/verify` 하나만 호출합니다.
URL 검증은 백엔드에 있지만 웹 화면에는 URL 입력이 없습니다.

### Chrome 확장 (`src/background.js`)

`POST /api/verify/url` 하나만 호출합니다.
파일 업로드 검증은 쓰지 않습니다.

## 인증 요구 사항

| 그룹 | 인증 | 토큰 종류 |
|---|---|---|
| `/api/auth/token`, `app/request`, `app/verify` | 불필요 | — |
| `/api/auth/refresh`, `logout` | 본문의 리프레시 토큰 | refresh |
| `/api/auth/did/rebind` | 본문의 재연결 토큰 | did-rebind |
| `/api/signup/*` (token, app/*) | 불필요 | — |
| `/api/signup/did/complete` | 본문의 가입 토큰 | signup |
| `/api/videos/**` | `Authorization` 헤더 | access |
| `/api/verify/**` | 불필요 | — |

`/api/videos`의 등록만 `ISSUER` 역할을 추가로 확인하고,
나머지 영상 API는 로그인 + 소유권 확인으로 통제합니다.

## CORS 고려 사항

웹과 확장은 브라우저에서 직접 백엔드를 호출하므로 CORS 설정의 영향을 받습니다.

- `cors.allowed-origins` 미설정 → 전체 허용 (개발 기본값)
- 설정 시 → 쉼표로 구분한 오리진만 허용

배포 시에는 웹 도메인과 확장의 오리진(`chrome-extension://{id}`)을
허용 목록에 넣어야 합니다.

확장은 추가로 `manifest.json`의 `host_permissions`에 백엔드 호스트가 있어야 합니다.
현재는 `http://localhost:8070/*`만 등록되어 있습니다.

## 백엔드에만 있고 아직 쓰이지 않는 것

| 항목 | 상태 |
|---|---|
| `GET /api/videos/{videoId}` | 구현·문서화되었으나 호출하는 클라이언트 없음 |
| `VC_REVOCATION_FAILED` (D003) | 에러 코드만 정의, VC 폐기 API 없음 |
| `BLOCKCHAIN_VERIFICATION_FAILED` (VF001) | 정의되어 있으나 검증 실패는 verdict로 처리 |
| `domain/member/controller`, `domain/member/service`, `config` | 디렉터리만 있고 파일 없음 |
