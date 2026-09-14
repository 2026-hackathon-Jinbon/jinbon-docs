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
  "registrantName": "기획재정부 대변인실",
  "blockchainVerified": true,
  "vcVerified": true,
  "vcClaimsBound": true,
  "active": true,
  "message": "등록된 원본 파일과 정확히 일치합니다.",
  "notice": null
}
```

### 응답 필드

| 필드 | 설명 |
|---|---|
| `verdict` | 내부 9종 판정값 (로그·디버깅용) |
| `displayStatus` | 클라이언트 표시용 — `AUTHENTICATED` / `CONTENT_SIMILAR` / `NOT_AUTHENTICATED` |
| `similarityDistance` | 지각해시 매칭일 때만 값이 있음 (16프레임 평균 해밍 거리) |
| `authentic` | `displayStatus == AUTHENTICATED`와 같음 (구버전 호환) |
| `issuerDid` | **영상 등록자의 DID** (VC 발급기관 아님) |
| `registrantName` | 등록자 표시명 (기관명 등). 없으면 실명. 미등록이면 `null` |
| `blockchainVerified` | 온체인 기록 대조 통과 여부 |
| `vcVerified` · `vcClaimsBound` | VC 검증 통과 여부 · VC 클레임이 등록 당시 스냅샷과 결속됐는지 |
| `notice` | 판정 해석 시 주의사항. 있으면 반드시 노출 |

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `V003` | 500 | 영상 처리 실패 |

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

| 호스트 | 비고 |
|---|---|
| `youtube.com`, `youtu.be` | 서브도메인 포함 |
| `instagram.com` | 서브도메인 포함 |
| `tiktok.com` | 서브도메인 포함 |
| `twitter.com`, `x.com` | 서브도메인 포함 |
| `vimeo.com` | 서브도메인 포함 |

**에러**

| 코드 | HTTP | 상황 |
|---|---|---|
| `VF002` | 400 | 다운로드 실패 — 잘못된 URL, HTTPS 아님, 허용되지 않은 호스트, 내부 IP 차단, yt-dlp 실패 |

---

## displayStatus — 클라이언트 표시 상태

사용자에게는 **진본 / 콘텐츠 유사 / 미인증** 세 가지로 보여줍니다. 외부 검증 장애는 별도 사용자 상태로 노출하지 않고 내부 오류·재시도 정책으로 처리합니다.

> 아래의 CONTENT_SIMILAR 매핑은 음성·구간 검증을 도입한 목표 정책입니다. 현재 백엔드의 SIMILAR_MATCH 동작과 다를 수 있으며, 구현 전환 시 API 계약을 함께 변경합니다.

| displayStatus | 사용자 표시 | 매핑되는 verdict |
|---|---|---|
| `AUTHENTICATED` | **진본** | `EXACT_MATCH` · `SAME_CONTENT` |
| `CONTENT_SIMILAR` | **콘텐츠 유사** | 원본 후보 발견, 부분 구간 일치, 추가 검증 필요 |
| `NOT_AUTHENTICATED` | **미인증** | `NOT_REGISTERED` · 등록 증거 무효 · 음성·영상·자막 변경 확인 |

::: tip 클라이언트 구현 가이드
- `AUTHENTICATED` → 진본 배지 + `registrantName` + 등록 시각
- `CONTENT_SIMILAR` → 콘텐츠 유사 안내 + 원본 후보의 `registrantName`·등록 시각·VC 상태. 진본 배지는 표시하지 않음
- `NOT_AUTHENTICATED` → 미인증 안내. `notice`("미등록은 조작의 증거가 아닙니다")가 있으면 반드시 노출
:::

## verdict 9종 — 내부 판정값

로그, 디버깅, CS 대응을 위해 백엔드는 세분화된 verdict를 유지합니다.

### 진본

| verdict | 의미 | 메시지 |
|---|---|---|
| `EXACT_MATCH` | 원본 파일과 SHA-256 일치 | 등록된 원본 파일과 정확히 일치합니다. |
| `SAME_CONTENT` | 프레임 지각해시 완전 일치 (컨테이너·메타데이터만 다름) | 등록된 영상과 동일한 콘텐츠로 판단됩니다. |
| `SIMILAR_MATCH` | 지각해시 4중 임계값 통과. 원본 후보를 찾았지만 영상·음성·시간 순서의 전체 무변조는 추가 검증 대상 | 등록 원본과 콘텐츠가 유사하지만 전체 진본은 확정하지 않습니다. |

지각해시 4중 임계값: 영상 길이 ±5% · 16프레임 평균 해밍 거리 ≤ 10 · 프레임 일치율 ≥ 90% · 최대 거리 ≤ 16. 세 verdict 모두 온체인 서명 재대조와 VC 클레임 결속을 통과해야 `AUTHENTICATED`가 됩니다.

### 미인증

| verdict | 의미 | 메시지 |
|---|---|---|
| `PARTIAL_MATCH` | 일부 프레임만 유사 (길이·순서·구간 차이) | 등록 영상과 일부 프레임이 유사하지만 원본 일치는 확인할 수 없습니다. |
| `NOT_REGISTERED` | 일치·유사 기록 없음 | 진본에 등록된 기록을 찾지 못했습니다. |
| `REGISTERED_BUT_REVOKED` | 비활성화됨 | 등록 후 비활성화된 영상입니다. |
| `CERTIFICATE_MISSING` | 온체인 기록은 있으나 VC 미발급 | 블록체인 등록 기록은 확인했지만 신원 기반 VC 보증서가 발급되지 않았습니다. |
| `CERTIFICATE_INVALID` | VC 무효 또는 클레임 불일치 | 블록체인 등록은 확인했지만 VC가 유효하지 않습니다. |

### 내부 확인 불가

| verdict | 의미 | 메시지 |
|---|---|---|
| `VERIFICATION_UNAVAILABLE` | 외부 장애 또는 온체인 무결성 불일치 | 외부 검증 서비스에 연결할 수 없습니다. |

::: warning NOT_REGISTERED 주의
미등록은 **조작의 증거가 아닙니다.** 등록된 적이 없다는 뜻일 뿐입니다. `notice` 필드가 있으면 반드시 노출해야 합니다.
:::
