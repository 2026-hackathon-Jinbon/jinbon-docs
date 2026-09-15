# 검증 API

인증이 필요 없는 공개 API입니다.

## POST /api/verify

파일을 업로드하여 영상을 검증합니다.

**형식** `multipart/form-data`의 `file` 파트 하나

**응답** `VideoVerifyResponse`

원본 파일이 그대로 제출된 경우입니다. 세그먼트·음성 비교를 하지 않으므로 `segmentMatch`, `audioMatch`는 `null`입니다.

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
  "notice": null,
  "segmentMatch": null,
  "audioMatch": null
}
```

재인코딩본이나 원본에서 잘라낸 구간은 세그먼트·음성 비교를 거치며, 그 결과가 함께 내려옵니다.

```json
{
  "verdict": "SIMILAR_MATCH",
  "displayStatus": "AUTHENTICATED",
  "similarityDistance": 4.25,
  "authentic": true,
  "videoId": 1,
  "issuerDid": "did:omn:abc123",
  "registeredAt": "2026-09-07T14:30:00",
  "registrantName": "기획재정부 대변인실",
  "blockchainVerified": true,
  "vcVerified": true,
  "vcClaimsBound": true,
  "active": true,
  "message": "등록된 원본과 같은 내용의 영상입니다. 플랫폼 재인코딩 등으로 파일은 다를 수 있습니다.",
  "notice": "등록 원본의 15000~45000ms 구간과 영상·음성이 일치합니다.",
  "segmentMatch": {
    "coverage": 0.9666666666666667,
    "orderPreserved": true,
    "bestOffsetMs": 15000,
    "matchedStartMs": 15000,
    "matchedEndMs": 45000,
    "matchedSegments": 29,
    "totalQuerySegments": 30,
    "totalRefSegments": 600,
    "unmatchedRanges": [{ "startMs": 10000, "endMs": 11000 }],
    "silentSegments": 0
  },
  "audioMatch": {
    "coverage": 0.9333333333333333,
    "orderPreserved": true,
    "bestOffsetMs": 15000,
    "matchedStartMs": 15000,
    "matchedEndMs": 45000,
    "matchedSegments": 28,
    "totalQuerySegments": 30,
    "totalRefSegments": 600,
    "unmatchedRanges": [{ "startMs": 10000, "endMs": 12000 }],
    "silentSegments": 2
  }
}
```

### 응답 필드

| 필드 | 설명 |
|---|---|
| `verdict` | 세부 판정값. 같은 배지 안에서 파일 정확 일치·유사도 통과 근거를 구분하고 로그·CS에 사용 |
| `displayStatus` | 클라이언트 표시용 — `AUTHENTICATED` / `CONTENT_SIMILAR` / `NOT_AUTHENTICATED` / `UNAVAILABLE` |
| `similarityDistance` | 지각해시 매칭일 때만 값이 있음 (16프레임 평균 해밍 거리) |
| `authentic` | 콘텐츠 일치 + 블록체인 + VC 검증을 모두 통과했는지 (구버전 호환) |
| `issuerDid` | **영상 등록자의 DID** (VC 발급기관 아님) |
| `registrantName` | 등록자 표시명 (기관명 등). 없으면 실명. 미등록이면 `null` |
| `blockchainVerified` | 온체인 기록 대조 통과 여부 |
| `vcVerified` · `vcClaimsBound` | VC 검증 통과 여부 · VC 클레임이 등록 당시 스냅샷과 결속됐는지 |
| `notice` | 판정 해석 시 주의사항. 있으면 반드시 노출 |
| `segmentMatch` | 영상 세그먼트 비교 결과. 비교를 수행한 경우에만 값이 있음 |
| `audioMatch` | 음성 세그먼트 비교 결과. 비교를 수행한 경우에만 값이 있음 |

### SegmentMatchResult

`segmentMatch`와 `audioMatch`는 같은 구조입니다.

| 필드 | 설명 |
|---|---|
| `coverage` | 제출 영상 세그먼트 중 원본에 대응하는 비율 (0.0~1.0) |
| `orderPreserved` | 고정 오프셋에서 일치 인덱스의 증가 여부. 현재 구현에서 독립적인 재편집 탐지 신호는 아님 |
| `bestOffsetMs` | 원본 기준 최적 시간 오프셋 |
| `matchedStartMs` · `matchedEndMs` | 원본에서 대응하는 구간의 시작·끝 |
| `matchedSegments` · `totalQuerySegments` · `totalRefSegments` | 일치 수 · 제출본 전체 · 원본 전체 |
| `unmatchedRanges` | 최적 오프셋에서 대응하지 않는 제출본 샘플 구간. 삽입·편집 여부의 확정 증거는 아님 |
| `silentSegments` | 무음 세그먼트 수 (음성 비교에서만 유효, 영상은 항상 `0`) |

::: tip 쇼츠 판별
`totalRefSegments > totalQuerySegments`는 제출본의 비교 구간 수가 더 적다는 뜻입니다. 이것만으로 잘라낸 영상이라고 확정하지 마세요. 비교 기준을 통과한 경우 원본 대응 구간을 표시하고, 전체 맥락을 보증하지 않음을 안내하세요.
:::

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

사용자에게는 **진본 / 콘텐츠 유사 / 미인증 / 확인 중** 네 가지로 보여줍니다. 매핑은 `VerificationVerdict` enum에 고정되어 있어 서버가 임의로 바꾸지 않습니다.

| displayStatus | 사용자 표시 | 매핑되는 verdict |
|---|---|---|
| `AUTHENTICATED` | **진본** | `EXACT_MATCH` · `SAME_CONTENT` · `SIMILAR_MATCH` |
| `CONTENT_SIMILAR` | **콘텐츠 유사** | `CONTENT_SIMILAR` · `PARTIAL_MATCH` |
| `NOT_AUTHENTICATED` | **미인증** | `NOT_REGISTERED` · `REGISTERED_BUT_REVOKED` · `CERTIFICATE_MISSING` · `CERTIFICATE_INVALID` |
| `UNAVAILABLE` | **확인 중** | `VERIFICATION_UNAVAILABLE` |

::: tip 클라이언트 구현 가이드
- `AUTHENTICATED` → 진본 배지와 함께 `verdict`에 따라 **파일 정확 일치 / 유사도 기준 통과**를 구분. 등록자·등록 시각과 해당하는 경우 원본 대응 구간을 표시. 유사도 통과를 전체 무변조로 표현하지 않음
- `CONTENT_SIMILAR` → 콘텐츠 유사 안내 + 원본 후보의 `registrantName`·등록 시각·VC 상태. **진본 배지는 표시하지 않음**
- `NOT_AUTHENTICATED` → 미인증 안내. `notice`("미등록은 조작의 증거가 아닙니다")가 있으면 반드시 노출
- `UNAVAILABLE` → 현재 판정 불가. 외부 장애는 재시도, 온체인 무결성 불일치는 운영자 확인. `message`·`notice`의 구체적인 사유를 함께 표시
:::

## verdict 10종 — 내부 판정값

로그, 디버깅, CS 대응을 위해 백엔드는 세분화된 verdict를 유지합니다.

### 진본 — `AUTHENTICATED`

| verdict | 의미 | 메시지 |
|---|---|---|
| `EXACT_MATCH` | 원본 파일과 SHA-256 일치 | 등록된 원본 파일과 정확히 일치합니다. |
| `SIMILAR_MATCH` | 지각해시 후보 + **영상 커버리지 ≥ 95%** + **음성 커버리지 ≥ 90%** + 양쪽 모두 시간 순서 보존 | 등록된 원본과 같은 내용의 영상입니다. 플랫폼 재인코딩 등으로 파일은 다를 수 있습니다. |
| `SAME_CONTENT` | 프레임 지각해시 완전 일치 (컨테이너·메타데이터만 다름) | 등록된 영상과 동일한 콘텐츠로 판단됩니다. |

플랫폼 재인코딩본과 연속 쇼츠는 후보 검색·영상·음성 비교 기준을 충족하면 `SIMILAR_MATCH`가 될 수 있습니다. 샘플 기반 판정은 전체 무변조나 맥락을 보증하지 않습니다. 세 verdict 모두 온체인 서명 재대조와 VC 클레임 결속을 추가로 통과해야 `authentic: true`가 됩니다.

::: info SAME_CONTENT
enum과 클라이언트 매핑에는 존재하지만 현재 판정 파이프라인에서는 산출되지 않습니다. 지각해시 완전 일치를 별도 경로로 분리할 때를 위해 예약된 값입니다.
:::

### 콘텐츠 유사 — `CONTENT_SIMILAR`

등록 후보는 찾았지만 유사도 승인 기준에 미달하거나 비교 정보가 부족한 상태입니다. 진본 배지를 표시하지 않습니다. 유사도 기준을 통과한 경우에도 전체 무변조가 보장되는 것은 아닙니다.

| verdict | 의미 | 메시지 |
|---|---|---|
| `CONTENT_SIMILAR` | 지각해시는 통과했으나 음성이 없거나 불일치, 또는 영상 커버리지가 80~95% | 등록 원본 후보는 찾았지만 대응 구간의 무변조까지 확정하지 못했습니다. |
| `PARTIAL_MATCH` | 일부 세그먼트만 대응 (길이·순서·구간 차이) | 등록 영상과 일부 프레임이 유사하지만 원본 일치는 확인할 수 없습니다. |

`CONTENT_SIMILAR`의 `notice`에는 세그먼트 커버리지, 원본 대응 구간, 불일치 구간 개수가 담깁니다. 음성 대응 비율이 기준에 미달하면 이 경로로 분류될 수 있습니다. 일부 교체는 기준 안에 남을 수 있습니다.

### 미인증 — `NOT_AUTHENTICATED`

| verdict | 의미 | 메시지 |
|---|---|---|
| `NOT_REGISTERED` | 일치·유사 기록 없음 | 진본에 등록된 기록을 찾지 못했습니다. |
| `REGISTERED_BUT_REVOKED` | 비활성화됨 | 등록 후 비활성화된 영상입니다. |
| `CERTIFICATE_MISSING` | 온체인 기록은 있으나 VC 미발급 | 블록체인 등록 기록은 확인했지만 신원 기반 VC 보증서가 발급되지 않았습니다. |
| `CERTIFICATE_INVALID` | VC 무효 또는 클레임 불일치 | 영상의 블록체인 등록 기록은 확인했지만 VC 보증서가 유효하지 않습니다. |

### 확인 중 — `UNAVAILABLE`

| verdict | 의미 | 메시지 |
|---|---|---|
| `VERIFICATION_UNAVAILABLE` | 외부 장애 또는 온체인 무결성 불일치 | 외부 검증 서비스에 연결할 수 없어 현재 진본 여부를 확인할 수 없습니다. |

콘텐츠 매칭 결과와 무관하게 블록체인·VC 검증을 수행할 수 없으면 이 값으로 덮어씁니다. 이 결과는 **캐싱하지 않습니다.**

::: warning NOT_REGISTERED 주의
미등록은 **조작의 증거가 아닙니다.** 현재 비교에서 등록 후보를 찾지 못했다는 뜻입니다. `notice` 필드가 있으면 반드시 노출해야 합니다.
:::
