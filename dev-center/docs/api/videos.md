# 영상 관리 API

## POST /api/videos

영상을 등록하고 VC 발급을 준비합니다.

**형식** `multipart/form-data`

| 파트 | 타입 | 필수 | 설명 |
|---|---|---|---|
| `file` | file | O | 영상 파일 (최대 100MB) |
| `title` | string | O | 영상 제목 |

**권한** `ISSUER` (DID 등록 완료 회원)

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

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `V001` | 403 | ISSUER 아님 |
| `V002` | 400 | DID 미등록 |
| `V003` | 500 | 영상 처리 실패 |
| `V004` | 409 | 다른 계정에 등록됨 |
| `V008` | 500 | 블록체인 실패 |
| `C002` | 413 | 용량 초과 |

---

## GET /api/videos

내 영상 목록을 조회합니다.

**쿼리** Spring `Pageable` (`page`, `size`, `sort`)
**응답** `Page<VideoDetailResponse>` — `registeredAt` 내림차순

---

## GET /api/videos/{videoId}

영상 상세를 조회합니다.

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

`vcIssuanceStatus`: `NOT_REQUESTED` / `PENDING_WALLET` / `ISSUED`

**에러** `V005`(404) 없음 · `V006`(403) 본인 영상 아님

---

## POST /api/videos/{videoId}/vc/prepare

VC 발급을 준비하거나 재개합니다. 요청 본문 없음.

**응답** `VideoRegisterResponse` (`alreadyRegistered`는 항상 `true`)

**에러** `D006`(503) 기능 비활성 · `V005`(404) · `V006`(403) · `D001`(500) 발급 준비 실패

---

## POST /api/videos/{videoId}/vc/complete

Wallet에서 발급받은 VC를 연결합니다.

**요청**

```json
{ "vcId": "vc-abc123", "offerId": "offer-abc123" }
```

두 필드 모두 필수이며 각각 500자 이하.

**응답** `data: null`

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `D006` | 503 | 기능 비활성 |
| `D005` | 400 | Offer 불일치 |
| `D004` | 400 | 발급 준비 전 |
| `D002` | 500 | VC 검증 실패 |
| `V006` | 403 | 본인 아님 |
| `V005` | 404 | 영상 없음 |

---

## PATCH /api/videos/{videoId}/deactivate

영상을 비활성화합니다. 요청 본문 없음.

**응답** `data: null`

::: warning
비활성화된 영상은 검증 시 `REGISTERED_BUT_REVOKED`로 판정됩니다. 등록 기록 자체가 사라지지는 않습니다.
:::

**에러** `V007`(400) 이미 비활성 · `V005`(404) · `V006`(403) · `V008`(500) 블록체인 실패
