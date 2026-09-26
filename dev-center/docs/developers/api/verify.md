# 검증 API

로그인 없이 파일 또는 URL을 검증합니다. 두 API는 같은 `VideoVerifyResponse`를 반환하며, 아래 응답 예시는 [공통 응답](/developers/api/conventions)의 `data` 내부입니다.

동작 설명은 [영상 검증](/developers/flows/video-verify), 결과 해석은 [검증 결과 읽는 법](/developers/guide/verification-results)을 참고하세요.

## POST /api/verify

`multipart/form-data`의 **`file` 파트 하나**로 영상 파일을 보냅니다.

## POST /api/verify/url

서버가 URL에서 영상을 다운로드해 검증합니다.

```json
{ "url": "https://www.youtube.com/watch?v=abc123" }
```

### 입력 조건과 다운로드 제한 {#input-limits}

| 항목 | 조건 |
|---|---|
| 파일 업로드 | 파일 최대 100MB, 전체 요청 110MB |
| URL | 공백 불가, 최대 2,048자, HTTPS. 사용자 정보·명시적 포트 포함 불가 |
| 허용 호스트 | `youtube.com`, `youtu.be`, `instagram.com`, `tiktok.com`, `twitter.com`, `x.com`, `vimeo.com`과 서브도메인 |
| 다운로드 | 최대 1080p 영상·음성 선택, 최대 500MB, 재생목록 제외 |
| 처리 제한 | 다운로드 프로세스 최대 120초, 서버당 동시 다운로드 4개 |

120초는 전체 검증 완료 시간을 보장하는 값이 아닙니다. URL의 내부 주소 차단 규칙은 [보안 문서](/developers/security/overview#ssrf)를 참고하세요.

### 요청 오류

| 코드 | HTTP | 상황 |
|---|---|---|
| `C002` | 413 | 업로드 크기 초과 |
| `V003` | 500 | 영상 처리 실패 |
| `VF002` | 400 | URL 검사 또는 다운로드 실패 |

요청 오류는 `verdict` 판정과 별개입니다. URL을 다운로드하지 못한 경우를 ‘미등록’으로 표시하지 마세요.

## 응답 예시

**파일 정확 일치**는 영상·음성 구간 비교를 생략하므로 `segmentMatch`, `audioMatch`가 `null`입니다.

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

<details>
<summary>유사도 기준을 통과한 클립 응답 예시</summary>

구간 비교를 수행한 경우 `segmentMatch`와 `audioMatch`로 대응 비율·원본 위치를 반환합니다.

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
  "message": "등록 원본과 영상·음성 유사도 기준을 통과했습니다.",
  "notice": "등록 원본의 130000~160000ms 대응 구간을 비교했습니다. 영상·음성 지문의 시간 오프셋이 일치합니다. 생략된 맥락이나 모든 변조의 부재를 보증하지 않습니다.",
  "segmentMatch": {
    "coverage": 0.9666666666666667,
    "orderPreserved": true,
    "bestOffsetMs": 130000,
    "matchedStartMs": 130000,
    "matchedEndMs": 160000,
    "matchedSegments": 29,
    "totalQuerySegments": 30,
    "totalRefSegments": 600,
    "unmatchedRanges": [{ "startMs": 10000, "endMs": 11000 }],
    "silentSegments": 0
  },
  "audioMatch": {
    "coverage": 1.0,
    "orderPreserved": true,
    "bestOffsetMs": 130000,
    "matchedStartMs": 130000,
    "matchedEndMs": 160000,
    "matchedSegments": 30,
    "totalQuerySegments": 30,
    "totalRefSegments": 600,
    "unmatchedRanges": [],
    "silentSegments": 2
  }
}
```

</details>

## 응답 필드

| 필드 | 설명 |
|---|---|
| `verdict` / `displayStatus` | 세부 판정 / 화면 표시 분류. 아래 매핑 사용 |
| `authentic` | 콘텐츠 비교·블록체인·VC·등록 정보 일치를 모두 통과했는지 |
| `videoId` / `registeredAt` | 찾은 등록 건의 ID / 등록 시점 |
| `issuerDid` | 영상 등록자의 DID. VC 발급기관 DID와 다름 |
| `registrantName` | 등록자 표시명. 없으면 실명, 미등록이면 `null` |
| `active` | 등록 활성 여부 |
| `similarityDistance` | 지각해시 후보 검색 시 평균 해밍 거리. 정확 일치 경로는 `null` |
| `blockchainVerified` | 온체인 기록 대조 통과 여부 |
| `vcVerified` / `vcClaimsBound` | VC 검증 통과 / VC 정보와 해당 등록 건의 일치 여부 |
| `message` / `notice` | 결과 설명 / 추가 안내. 함께 표시 |
| `segmentMatch` / `audioMatch` | 영상 / 음성 구간 비교 결과. 비교하지 않았다면 `null` |

## 구간 비교 결과 {#segment-result}

`segmentMatch`와 `audioMatch`는 같은 `SegmentMatchResult` 구조입니다.

| 필드 | 설명 |
|---|---|
| `coverage` | 제출본 비교 구간 중 등록 영상에 대응한 비율 (0~1) |
| `orderPreserved` | 고정 시간 이동량에서 일치 인덱스의 증가 여부. 독립적인 재편집 탐지 신호는 아님 |
| `bestOffsetMs` | 등록 영상 기준 최적 시간 이동량 |
| `matchedStartMs` / `matchedEndMs` | 등록 영상에서 대응한 구간의 시작·끝 |
| `matchedSegments` | 대응한 제출본 구간 수 |
| `totalQuerySegments` / `totalRefSegments` | 제출본 / 등록 영상의 비교 구간 수 |
| `unmatchedRanges` | 대응하지 않는 제출본 샘플 구간. 편집의 확정 증거는 아님 |
| `silentSegments` | 제출본의 무음 구간 수. 영상 비교에서는 `0` |

`totalRefSegments > totalQuerySegments`만으로 잘라낸 영상이라고 확정하지 마세요. 비교 기준을 통과한 경우에 원본 대응 구간을 표시합니다.

## 화면 표시 매핑 {#display-status}

| displayStatus | 상태 의미 | verdict |
|---|---|---|
| `AUTHENTICATED` | **진본** | `EXACT_MATCH`, `SIMILAR_MATCH`, `SAME_CONTENT` |
| `CONTENT_SIMILAR` | **콘텐츠 유사** | `CONTENT_SIMILAR`, `PARTIAL_MATCH` |
| `NOT_AUTHENTICATED` | **미인증** | `NOT_REGISTERED`, `REGISTERED_BUT_REVOKED`, `CERTIFICATE_MISSING`, `CERTIFICATE_INVALID` |
| `UNAVAILABLE` | **현재 확인 불가** | `VERIFICATION_UNAVAILABLE` |

- 진본에서는 **파일 정확 일치 / 유사도 기준 통과**를 구분하고 등록자·등록 시점·해당하는 경우 대응 구간을 표시합니다.
- 콘텐츠 유사에서는 후보 정보를 제공하되 진본 배지를 표시하지 않습니다.
- 미인증·확인 불가에서는 `message`·`notice`의 상세 원인과 대응 안내를 표시합니다.

`SAME_CONTENT`는 호환용 값이며 현재 파이프라인에서는 산출하지 않습니다. 판정 조건과 우선순위는 [최종 판정 규칙](/developers/flows/video-verify#final-verdict)에 정리되어 있습니다.
