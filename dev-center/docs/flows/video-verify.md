# 영상 검증

인증이 필요 없는 공개 API입니다.

| 엔드포인트 | 입력 | 사용 채널 |
|---|---|---|
| `POST /api/verify` | `multipart/form-data`의 `file` | 웹, iOS 앱 |
| `POST /api/verify/url` | JSON `{ "url": "..." }` | Chrome 확장 |

## 판정 순서

```mermaid
flowchart TD
  START[검증 요청] --> CACHE{Redis 캐시 있음?}
  CACHE -->|HIT| RET[즉시 반환]
  CACHE -->|MISS| FINE[fineHash 계산]
  FINE --> EXACT{fineHash 일치 영상?}
  EXACT -->|있음| BUILD[EXACT_MATCH]
  EXACT -->|없음| PH[perceptualHash 계산]
  PH --> SIM{해밍 거리 < 10인 영상?}
  SIM -->|없음| NR[NOT_REGISTERED]
  SIM -->|거리 0| SC[SAME_CONTENT]
  SIM -->|거리 0 초과| SM[SIMILAR_MATCH]
  BUILD --> CHECK
  SC --> CHECK
  SM --> CHECK
  CHECK{활성 영상?} -->|아니오| REV[REGISTERED_BUT_REVOKED]
  CHECK -->|예| BC[온체인 검증 + VC 검증]
  BC --> FINAL[최종 verdict 산출]
  FINAL --> CACHE2[캐싱 후 반환]
  NR --> CACHE2
  REV --> CACHE2
```

## 1단계: 캐시

| 항목 | 값 |
|---|---|
| 결과 키 | `verify:result:{fineHash}` |
| URL 검증 키 | `verify:result:url:{SHA-256(url)}` |
| 영상별 인덱스 | `verify:video:{videoId}` (Set) |
| TTL | 10분 |

`VERIFICATION_UNAVAILABLE` 결과는 캐싱하지 않습니다.

## 2단계: 정확 일치

파일 전체 SHA-256을 계산해 `videos.fine_hash`와 대조합니다. 일치하면 `EXACT_MATCH`이며, 지각해시를 계산하지 않습니다.

## 3단계: 유사도 검색

정확 일치가 없으면 프레임별 지각해시를 만들어 활성 영상 전체와 비교합니다.

| 거리 | 판정 |
|---|---|
| `0.0` | `SAME_CONTENT` |
| `0.0 < d < 10` | `SIMILAR_MATCH` |
| `>= 10` | `NOT_REGISTERED` |

## 4단계: 온체인 검증

서명을 **재계산해서** DB 값과 온체인 값 양쪽에 대조합니다. DB가 조작되었더라도 서버 비밀키 없이는 서명을 다시 만들 수 없고, 온체인 값은 변경 불가하므로 두 값이 동시에 맞아야 통과합니다.

## 5단계: VC 검증

`video.vcId`가 있을 때만 Verifier를 호출합니다. 없으면 블록체인 검증만으로 판정합니다.

## 최종 판정 규칙

| 순위 | 조건 | verdict | authentic |
|---|---|---|---|
| 0 | 영상이 비활성 | `REGISTERED_BUT_REVOKED` | `false` |
| 1 | 외부 검증 불가 | `VERIFICATION_UNAVAILABLE` | `false` |
| 2 | 블록체인 검증 실패 | `VERIFICATION_UNAVAILABLE` | `false` |
| 3 | VC가 유효하지 않음 | `CERTIFICATE_INVALID` | `false` |
| 4 | 매칭 결과 그대로 | `EXACT_MATCH` / `SAME_CONTENT` / `SIMILAR_MATCH` | `true` |
| — | 매칭 없음 | `NOT_REGISTERED` | `false` |

## 클라이언트 표시 매핑

사용자에게는 verdict를 직접 노출하지 않고, `displayStatus` 3종으로 단순화해서 표시합니다.

| displayStatus | verdict | 사용자 화면 |
|---|---|---|
| `AUTHENTICATED` | `EXACT_MATCH`, `SAME_CONTENT`, `SIMILAR_MATCH` | 진본 인증 |
| `NOT_AUTHENTICATED` | `NOT_REGISTERED`, `REGISTERED_BUT_REVOKED`, `CERTIFICATE_INVALID` | 미인증 |
| `UNAVAILABLE` | `VERIFICATION_UNAVAILABLE` | 확인 중 (재시도 유도) |

## URL 검증의 추가 절차

허용 호스트: `youtube.com`, `youtu.be`, `instagram.com`, `tiktok.com`, `twitter.com`, `x.com`, `vimeo.com`

DNS 응답의 **모든** IP를 검사해 루프백·사설·링크로컬·멀티캐스트가 하나라도 있으면 차단합니다 (DNS 리바인딩 방어).
