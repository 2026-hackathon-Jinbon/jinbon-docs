# 회원가입 API

`/api/signup/token`과 `/api/signup/app/request`는 [인증 API](/api/auth)와 요청·응답이 동일합니다.

## POST /api/signup/app/verify

**요청** — 인증 API의 `VerifyRequest`와 동일

```json
{
  "provider": "comdl",
  "token": "eyJ...",
  "txId": "a80161c7...",
  "cxId": "b12345..."
}
```

**응답** `SignupIdentityResponse`

```json
{
  "signupToken": "eyJ...",
  "memberId": 1,
  "name": "홍길동",
  "status": "PENDING"
}
```

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `M002` | 409 | 이미 가입 완료 |
| `A005` | 400 | CI 없음 |
| `A007` | 409 | 검증 진행 중 |

## POST /api/signup/did/complete

DID를 연결하고 가입을 완료합니다.

**요청**
```json
{ "signupToken": "...", "did": "did:omn:abc123" }
```

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
| `A006` | 400 | 가입 토큰 아님 |
| `M001` | 404 | 회원 없음 |
| `M002` | 409 | 이미 가입 완료 |
| `M005` | 409 | DID 중복 |

::: tip 상태 전이
`[없음] → PENDING(USER) → ACTIVE(ISSUER)`

`updateDid()` 한 번의 호출로 DID 연결, 역할 승격, 상태 전환, 가입 시각 기록이 모두 일어납니다.
:::
