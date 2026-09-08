# 검증 API

인증이 필요 없는 공개 API입니다.

## POST /api/verify

파일을 업로드하여 영상을 검증합니다.

**형식** `multipart/form-data`의 `file` 파트 하나

**응답** `VideoVerifyResponse`

```json
{
  "verdict": "EXACT_MATCH",
  "displayStatus": "AUTHENTICATED",
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

### 응답 필드

| 필드 | 설명 |
|---|---|
| `verdict` | 내부 7종 판정값 (로그·디버깅용) |
| `displayStatus` | 클라이언트 표시용 3종: `AUTHENTICATED` / `NOT_AUTHENTICATED` / `UNAVAILABLE` |
| `similarityDistance` | `SIMILAR_MATCH`일 때만 값이 있음 |
| `authentic` | 구버전 호환 boolean. 신규 화면은 `displayStatus` 사용 |
| `issuerDid` | **영상 등록자의 DID** (VC 발급기관 아님) |
| `blockchainVerified` | 온체인 기록 대조 통과 여부 |
| `vcVerified` | VC 검증 통과 여부 |
| `notice` | 판정 해석 시 주의사항. 있으면 반드시 노출 |

**에러** `V003`(500) 영상 처리 실패

---

## POST /api/verify/url

URL로 영상을 검증합니다.

**요청**

```json
{ "url": "https://www.youtube.com/watch?v=abc123" }
```

`@NotBlank`, 최대 2048자.

**응답** — `POST /api/verify`와 동일

### 허용 호스트

`youtube.com`, `youtu.be`, `instagram.com`, `tiktok.com`, `twitter.com`, `x.com`, `vimeo.com` (서브도메인 포함)

**에러** `VF002`(400) 다운로드 실패 — 잘못된 URL, HTTPS 아님, 허용되지 않은 호스트, 내부 IP 차단, yt-dlp 실패가 모두 이 코드로 옵니다.

---

## displayStatus — 클라이언트 표시 상태

사용자에게는 3종의 상태만 표시합니다. 백엔드가 `displayStatus` 필드로 매핑해서 내려줍니다.

| displayStatus | 사용자 표시 | 매핑되는 verdict |
|---|---|---|
| `AUTHENTICATED` | **진본 인증** | `EXACT_MATCH`, `SAME_CONTENT`, `SIMILAR_MATCH` |
| `NOT_AUTHENTICATED` | **미인증** | `NOT_REGISTERED`, `REGISTERED_BUT_REVOKED`, `CERTIFICATE_INVALID` |
| `UNAVAILABLE` | **확인 중** | `VERIFICATION_UNAVAILABLE` |

::: tip 클라이언트 구현 가이드
- `AUTHENTICATED` → 인증 뱃지 표시
- `NOT_AUTHENTICATED` → 미인증 안내
- `UNAVAILABLE` → "잠시 후 다시 시도해 주세요" + 재시도 버튼
:::

## verdict 7종 (내부 판정값)

로그, 디버깅, CS 대응을 위해 백엔드는 세분화된 verdict를 유지합니다.

| verdict | 의미 | 메시지 |
|---|---|---|
| `EXACT_MATCH` | 원본 파일과 SHA-256 일치 | 등록된 원본 파일과 정확히 일치합니다. |
| `SAME_CONTENT` | 프레임 지각해시 완전 일치 | 등록된 영상과 동일한 콘텐츠로 판단됩니다. |
| `SIMILAR_MATCH` | 지각해시 거리 < 10 | 등록 영상과 유사합니다. 재인코딩 또는 일부 변환되었을 수 있습니다. |
| `NOT_REGISTERED` | 일치·유사 기록 없음 | 진본에 등록된 기록을 찾지 못했습니다. |
| `REGISTERED_BUT_REVOKED` | 비활성화됨 | 등록 후 비활성화된 영상입니다. |
| `CERTIFICATE_INVALID` | VC 무효 | 블록체인 등록 기록은 확인했지만 VC 보증서가 유효하지 않습니다. |
| `VERIFICATION_UNAVAILABLE` | 외부 장애 | 외부 검증 서비스에 연결할 수 없어 현재 진본 여부를 확인할 수 없습니다. |

::: warning NOT_REGISTERED 주의
미등록은 **조작의 증거가 아닙니다.** 등록된 적이 없다는 뜻일 뿐입니다. `notice` 필드가 있으면 반드시 노출해야 합니다.
:::
