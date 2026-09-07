# 백엔드 API 명세

기본 주소: `http://localhost:8070` (`SERVER_PORT`)
Swagger UI: `http://localhost:8070/swagger-ui/index.html` (개발 프로필에서만 접근 가능)

## 공통 규약

### 응답 포맷

모든 응답은 `CommonResponse<T>`로 감쌉니다.

```json
{ "status": 200, "message": "Success", "data": { } }
```

실패 시 `code`에 에러 코드가 채워집니다.

```json
{ "status": 409, "code": "V004", "message": "동일한 영상이 다른 계정에 이미 등록되어 있습니다." }
```

`null` 필드는 직렬화에서 제외됩니다(`@JsonInclude(NON_NULL)`).

### 인증

인증이 필요한 API는 헤더에 액세스 토큰을 넣습니다.

```
Authorization: Bearer {accessToken}
```

액세스 토큰 만료는 30분입니다.

### 업로드 제한

파일 100MB, 요청 전체 110MB. 초과 시 `C002`(413).

## 엔드포인트 목록

| Method | Path | 설명 | 인증 |
|---|---|---|---|
| POST | `/api/auth/token` | OmniOne CX 세션 토큰 발급 | — |
| POST | `/api/auth/app/request` | WebToApp 딥링크 생성 | — |
| POST | `/api/auth/app/verify` | 신분증 검증 + 로그인 | — |
| POST | `/api/auth/did/rebind` | 앱 재설치 후 DID 재연결 | 재연결 토큰 |
| POST | `/api/auth/refresh` | 토큰 갱신 | 리프레시 토큰 |
| POST | `/api/auth/logout` | 로그아웃 | 리프레시 토큰 |
| POST | `/api/signup/token` | 가입용 세션 토큰 발급 | — |
| POST | `/api/signup/app/request` | 가입용 딥링크 생성 | — |
| POST | `/api/signup/app/verify` | 본인확인 + PENDING 회원 생성 | — |
| POST | `/api/signup/did/complete` | DID 연결 + 가입 완료 | 가입 토큰 |
| POST | `/api/videos` | 영상 등록 및 VC 발급 준비 | ISSUER |
| GET | `/api/videos` | 내 영상 목록 | O |
| GET | `/api/videos/{videoId}` | 영상 상세 | O (본인) |
| POST | `/api/videos/{videoId}/vc/prepare` | VC 발급 준비·재개 | O (본인) |
| POST | `/api/videos/{videoId}/vc/complete` | VC 발급 완료 연결 | O (본인) |
| PATCH | `/api/videos/{videoId}/deactivate` | 영상 비활성화 | O (본인) |
| POST | `/api/verify` | 파일 업로드 검증 | — |
| POST | `/api/verify/url` | URL 기반 검증 | — |

---

## 인증 API

### POST /api/auth/token

OmniOne CX 인증 세션을 시작합니다. 파라미터 없음.

**응답** `OacxTokenResponse` — `token`, `txId`

### POST /api/auth/app/request

쿼리 파라미터로 받습니다.

| 파라미터 | 타입 | 설명 |
|---|---|---|
| `provider` | string | 인증사 코드. 모바일 운전면허증은 `comdl` |
| `token` | string | STEP 1의 `token` |
| `txId` | string | STEP 1의 `txId` |

**응답** `OacxAppResponse` — `data.androidLink`, `data.iosLink`, `cxId`

### POST /api/auth/app/verify

**요청**

```json
{
  "provider": "comdl",
  "token": "eyJhbGciOiJIUzI1NiJ9...",
  "txId": "a80161c7c7fe4dcb93f6d6e2da7a9537pdrmn0ck",
  "cxId": "b12345..."
}
```

모든 필드 필수(`@NotBlank`).

**응답** `AuthResponse`

```json
{
  "accessToken": "eyJ...",
  "refreshToken": "eyJ...",
  "memberId": 1,
  "name": "홍길동",
  "role": "ISSUER",
  "status": "ACTIVE",
  "did": "did:omn:abc123",
  "didRebindToken": "eyJ..."
}
```

**오류** `A001`(401) 검증 실패 · `A005`(400) CI 없음 · `A007`(409) 검증 진행 중 ·
`M001`(404) 미가입 · `M003`(409) 가입 미완료 · `M004`(403) 비활성 회원

### POST /api/auth/did/rebind

**요청** `{ "didRebindToken": "...", "did": "did:omn:new..." }`
**응답** `AuthResponse` (새 토큰 쌍)
**오류** `A008`(401) 토큰 무효 · `M005`(409) DID 중복

### POST /api/auth/refresh

**요청** `{ "refreshToken": "..." }`
**응답** `AuthResponse` (새 accessToken + 새 refreshToken)
**오류** `A002`(401) 무효 · `A003`(400) 리프레시 토큰 아님 · `A004`(401) 만료·재사용

### POST /api/auth/logout

**요청** `{ "refreshToken": "..." }` · **응답** `data: null`

토큰이 이미 무효해도 200을 반환합니다.

---

## 회원가입 API

`/api/signup/token`과 `/api/signup/app/request`는 인증 API와 요청·응답이 동일합니다.

### POST /api/signup/app/verify

**요청** `VerifyRequest` (인증 API와 동일)

**응답** `SignupIdentityResponse`

```json
{ "signupToken": "eyJ...", "memberId": 1, "name": "홍길동", "status": "PENDING" }
```

**오류** `M002`(409) 이미 가입 완료 · `A005`(400) CI 없음 · `A007`(409) 검증 진행 중

### POST /api/signup/did/complete

**요청** `{ "signupToken": "...", "did": "did:omn:abc123" }`
**응답** `AuthResponse` (`role`은 `ISSUER`, `status`는 `ACTIVE`)
**오류** `A006`(400) 가입 토큰 아님 · `M001`(404) · `M002`(409) · `M005`(409)

---

## 영상 관리 API

### POST /api/videos

`multipart/form-data`

| 파트 | 타입 | 필수 | 설명 |
|---|---|---|---|
| `file` | file | O | 영상 파일 (최대 100MB) |
| `title` | string | O | 영상 제목 |

**응답** `VideoRegisterResponse`

```json
{
  "videoId": 1,
  "title": "2026 기자회견 원본",
  "merkleRoot": "a1b2c3...",
  "txHash": "0xabc123...",
  "blockNumber": "12345",
  "vcId": null,
  "registeredAt": "2026-09-07T14:30:00",
  "alreadyRegistered": false,
  "vcPlanId": "vcplan-jinbon-01",
  "vcIssuerDid": "did:omn:issuer123",
  "vcAssuranceType": "BLOCKCHAIN_REGISTRATION",
  "vcOfferId": "offer-abc123"
}
```

| 필드 | 비고 |
|---|---|
| `alreadyRegistered` | 같은 회원의 재등록이면 `true` |
| `vcPlanId` / `vcIssuerDid` / `vcOfferId` | 발급 준비 실패 또는 이미 발급된 경우 `null` |
| `vcId` | Wallet 발급 완료 전 `null` |

**오류** `V001`(403) ISSUER 아님 · `V002`(400) DID 미등록 · `V003`(500) 영상 처리 실패 ·
`V004`(409) 다른 계정에 등록됨 · `V008`(500) 블록체인 실패 · `C002`(413) 용량 초과

### GET /api/videos

**쿼리** Spring `Pageable` (`page`, `size`, `sort`)
**응답** `Page<VideoDetailResponse>` — `registeredAt` 내림차순

### GET /api/videos/{videoId}

**응답** `VideoDetailResponse`

```json
{
  "videoId": 1,
  "title": "2026 기자회견 원본",
  "merkleRoot": "a1b2c3...",
  "txHash": "0xabc123...",
  "blockNumber": "12345",
  "vcId": "vc-abc123",
  "vcIssuerDid": "did:omn:issuer123",
  "vcAssuranceType": "BLOCKCHAIN_REGISTRATION",
  "vcIssuanceStatus": "ISSUED",
  "active": true,
  "registeredAt": "2026-09-07T14:30:00",
  "deactivatedAt": null
}
```

`vcIssuanceStatus`는 `NOT_REQUESTED` / `PENDING_WALLET` / `ISSUED`.

**오류** `V005`(404) 없음 · `V006`(403) 본인 영상 아님

### POST /api/videos/{videoId}/vc/prepare

요청 본문 없음. **응답** `VideoRegisterResponse` (`alreadyRegistered`는 항상 `true`)

**오류** `D006`(503) 기능 비활성 · `V005`(404) · `V006`(403) · `D001`(500) 발급 준비 실패

### POST /api/videos/{videoId}/vc/complete

**요청**

```json
{ "vcId": "vc-abc123", "offerId": "offer-abc123" }
```

두 필드 모두 필수이며 각각 500자 이하.

**응답** `data: null`

**오류** `D006`(503) · `D005`(400) Offer 불일치 · `D004`(400) 발급 준비 전 ·
`D002`(500) VC 검증 실패 · `V006`(403) · `V005`(404)

### PATCH /api/videos/{videoId}/deactivate

요청 본문 없음. **응답** `data: null`

**오류** `V007`(400) 이미 비활성 · `V005`(404) · `V006`(403) · `V008`(500)

---

## 검증 API

인증이 필요 없습니다.

### POST /api/verify

`multipart/form-data`의 `file` 파트 하나.

**응답** `VideoVerifyResponse`

```json
{
  "verdict": "EXACT_MATCH",
  "similarityDistance": null,
  "authentic": true,
  "videoId": 1,
  "issuerDid": "did:omn:abc123",
  "registeredAt": "2026-09-07T14:30:00",
  "blockchainVerified": true,
  "vcVerified": true,
  "active": true,
  "message": "등록된 원본 파일과 정확히 일치합니다.",
  "notice": null
}
```

| 필드 | 설명 |
|---|---|
| `verdict` | 7종 판정값. 화면 구성의 기준 |
| `similarityDistance` | `SIMILAR_MATCH`일 때만 값이 있음 |
| `authentic` | 구버전 호환 boolean |
| `issuerDid` | **영상 등록자의 DID** (VC 발급기관 아님) |
| `notice` | 판정 해석 시 주의사항. 있으면 반드시 노출 |

**오류** `V003`(500) 영상 처리 실패

### POST /api/verify/url

**요청**

```json
{ "url": "https://www.youtube.com/watch?v=abc123" }
```

`@NotBlank`, 최대 2048자.

**응답** `POST /api/verify`와 동일합니다.

**오류** `VF002`(400) 다운로드 실패 — 잘못된 URL, HTTPS 아님,
허용되지 않은 호스트, 내부 IP 차단, yt-dlp 실패가 모두 이 코드로 옵니다.

---

## 에러 코드 전체

### 공통 (C)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `C001` | 500 | Internal server error. |
| `C002` | 413 | Upload size exceeds the 100MB limit. |
| `C003` | 400 | Invalid request. |

### 인증 (A)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `A001` | 401 | ID verification failed. |
| `A002` | 401 | Invalid refresh token. |
| `A003` | 400 | Not a refresh token. |
| `A004` | 401 | Expired or already used refresh token. |
| `A005` | 400 | Failed to retrieve CI information. |
| `A006` | 400 | Not a signup token. |
| `A007` | 409 | ID verification is still in progress. |
| `A008` | 401 | Invalid or expired DID rebind token. |

### 회원 (M)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `M001` | 404 | Member not found. |
| `M002` | 409 | Member is already registered. |
| `M003` | 409 | DID registration is not completed. |
| `M004` | 403 | Member is not active. |
| `M005` | 409 | DID is already registered. |

### 영상 (V)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `V001` | 403 | Only ISSUER role can register videos. |
| `V002` | 400 | Issuer DID is not registered. |
| `V003` | 500 | Failed to process video file. |
| `V004` | 409 | 동일한 영상이 다른 계정에 이미 등록되어 있습니다. |
| `V005` | 404 | Video not found. |
| `V006` | 403 | Not the owner of this video. |
| `V007` | 400 | Video is already deactivated. |
| `V008` | 500 | Blockchain transaction failed. |
| `V009` | 500 | Failed to generate signature. |

### 검증 (VF)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `VF001` | 500 | Blockchain verification failed. |
| `VF002` | 400 | Failed to download video from URL. |

### VC / Open DID (D)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `D001` | 500 | Failed to issue verifiable credential. |
| `D002` | 500 | Failed to verify verifiable credential. |
| `D003` | 500 | Failed to revoke verifiable credential. |
| `D004` | 400 | VC issuance is not in PENDING_WALLET state. |
| `D005` | 400 | VC offer does not match this video. |
| `D006` | 503 | Open DID VC integration is disabled. |

`V004`만 한국어 메시지이고 나머지는 영문입니다.
사용자에게 그대로 노출하는 대신 클라이언트가 코드로 분기해 문구를 만드는 것을 전제로 합니다.
