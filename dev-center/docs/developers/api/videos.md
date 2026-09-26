# 영상 관리 API

## POST /api/videos

영상을 등록하고 VC 발급을 준비합니다. 업로드 → 블록체인 기록 → Wallet 발급·연결의 전체 흐름은 [영상 등록](/developers/flows/video-register)을 참고하세요. 아래 응답 예시는 공통 응답의 `data` 내부입니다.

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

`vcIssuanceStatus`의 상태별 의미는 [보증서 발급 상태](/developers/flows/vc-issuance#issuance-status)를 참고하세요.

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `V005` | 404 | 영상 없음 |
| `V006` | 403 | 본인 영상 아님 |

---

## POST /api/videos/{videoId}/vc/prepare

VC 발급을 준비하거나 재개합니다. 요청 본문 없음.

**응답** `VideoRegisterResponse` (`alreadyRegistered`는 항상 `true`)

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `D006` | 503 | 기능 비활성 |
| `V005` | 404 | 영상 없음 |
| `V006` | 403 | 본인 아님 |
| `D001` | 500 | 발급 준비 실패 |

---

## POST /api/videos/{videoId}/vc/complete

Wallet에서 발급받은 VC를 연결합니다.

**요청**

```json
{
  "vcId": "vc-abc123",
  "offerId": "offer-abc123",
  "credential": "<Wallet에서 읽은 서명 포함 VC JSON 문자열>"
}
```

| 필드 | 필수 | 제약·설명 |
|---|---|---|
| `vcId` | O | Wallet에 저장된 VC 식별자, 최대 500자 |
| `offerId` | O | 해당 영상의 발급 Offer 식별자, 최대 500자 |
| `credential` | O | 서명 포함 VC JSON 원문을 문자열로 전달, 최대 100,000자 |

예시의 `credential`은 자리표시자입니다. 실제 요청에는 Wallet에서 읽은 JSON 원문을 넣어야 합니다. 서버는 원장 상태·VC 서명·발급자·등록자·등록 클레임을 확인하고 연결하며, 성공 시 관련 검증 캐시를 제거합니다.

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

## PUT /api/videos/{videoId}/vc/holder

Wallet의 `issuer_init` 발급 프로필 조회 전에 Holder 정보를 Issuer에 동기화합니다. 앱의 VC 발급 절차에서 사용합니다.

**권한** 로그인한 영상 등록자 본인. **요청 본문** 없음. **응답** `data: null`.

Open DID가 비활성화되어 있으면 `D006`(503), 본인 영상이 아니면 `V006`(403), 등록 DID가 맞지 않으면 `D005`(400)입니다.

---

## PATCH /api/videos/{videoId}/deactivate {#deactivate}

영상을 비활성화합니다. 요청 본문 없음.

**응답** `data: null`

::: warning
비활성화된 파일의 정확 일치 검증은 `REGISTERED_BUT_REVOKED`로 판정됩니다. 유사도 검색은 활성 등록만 대상으로 하므로 재압축된 사본은 후보를 찾지 못할 수 있습니다. 등록 기록 자체가 사라지지는 않습니다.
:::

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `V007` | 400 | 이미 비활성 |
| `V005` | 404 | 영상 없음 |
| `V006` | 403 | 본인 아님 |
| `V008` | 500 | 블록체인 실패 |
