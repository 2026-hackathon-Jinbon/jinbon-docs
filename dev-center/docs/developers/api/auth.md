# 인증 API

## POST /api/auth/token

OmniOne CX 인증 세션을 시작합니다. 파라미터 없음.

**응답** `OacxTokenResponse`

```json
{ "token": "eyJ...", "txId": "a80161c7..." }
```

## POST /api/auth/app/request

쿼리 파라미터로 받습니다.

| 파라미터 | 타입 | 설명 |
|---|---|---|
| `provider` | string | 인증사 코드. 모바일 운전면허증은 `comdl` |
| `token` | string | STEP 1의 `token` |
| `txId` | string | STEP 1의 `txId` |

**응답** `OacxAppResponse`

```json
{
  "data": { "androidLink": "...", "iosLink": "..." },
  "cxId": "b12345..."
}
```

## POST /api/auth/app/verify

**요청**

```json
{
  "provider": "comdl",
  "token": "eyJhbGciOiJIUzI1NiJ9...",
  "txId": "a80161c7c7fe4dcb93f6d6e2da7a9537pdrmn0ck",
  "cxId": "b12345..."
}
```

모든 필드 필수 (`@NotBlank`).

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

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `A001` | 401 | 검증 실패 |
| `A005` | 400 | CI 없음 |
| `A007` | 409 | 검증 진행 중 |
| `M001` | 404 | 미가입 |
| `M003` | 409 | 가입 미완료 |
| `M004` | 403 | 비활성 회원 |

## POST /api/auth/did/rebind

앱 재설치 후 DID를 재연결합니다.

**요청**
```json
{ "didRebindToken": "...", "did": "did:omn:new..." }
```

**응답** `AuthResponse` (새 토큰 쌍)

**에러** `A008`(401) 토큰 무효 · `M005`(409) DID 중복

## POST /api/auth/refresh

**요청**
```json
{ "refreshToken": "..." }
```

**응답** `AuthResponse` (새 accessToken + 새 refreshToken)

::: info Refresh Token Rotation
갱신 시 이전 refreshToken은 즉시 무효화됩니다. 이미 사용된 토큰을 다시 쓰면 `A004`(401)입니다.
:::

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `A002` | 401 | 무효 |
| `A003` | 400 | 리프레시 토큰 아님 |
| `A004` | 401 | 만료·재사용 |

## POST /api/auth/logout

**요청**
```json
{ "refreshToken": "..." }
```

**응답** `data: null`

토큰이 이미 무효해도 200을 반환합니다. accessToken은 만료(최대 30분)까지 유효하므로 클라이언트도 로컬 토큰을 삭제해야 합니다.
