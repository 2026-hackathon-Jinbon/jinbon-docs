# 핵심 시퀀스

진본의 동작을 네 장면으로 나눠 봅니다.

---

## 1 · 가입 — 신분증에서 DID까지

```mermaid
sequenceDiagram
  autonumber
  participant A as 📱 앱
  participant B as ⚙️ 백엔드
  participant CX as 📇 OmniOne CX
  participant W as 🔐 Wallet SDK

  A->>B: 본인확인 요청
  B->>CX: 인증 세션 생성
  CX-->>A: 딥링크로 신분증 앱 호출
  Note over A,CX: 사용자가 모바일 신분증 제출
  A->>B: 검증 요청
  B->>CX: 결과 조회
  CX-->>B: CI · 이름 · 생년월일
  B->>B: CI를 HMAC 해싱<br/>(원문은 저장하지 않음)
  B-->>A: signupToken + PENDING 회원

  A->>W: DID 생성 및 등록
  W-->>A: Holder DID
  A->>B: signupToken + DID
  B->>B: ACTIVE + ISSUER 전환
  B-->>A: 🎫 accessToken · refreshToken
```

| 지키는 것 | 방법 |
|---|---|
| CI 원문 미저장 | `HMAC-SHA256` 해시(`h1:` 접두사)만 DB에 |
| 자동 가입 방지 | 로그인 흐름에서 회원을 만들지 않음 |
| 계정 도용 방지 | 기기 Wallet DID ≠ 계정 DID면 연결 거부 |

> **앱 재설치로 DID가 사라지면?** 로그인 시 함께 받은 단기 `didRebindToken`으로
> 새 DID를 안전하게 재연결합니다. 기존 영상 소유권은 `memberId` 기준이라 유지됩니다.

---

## 2 · 등록 — 해시에서 온체인까지

```mermaid
sequenceDiagram
  autonumber
  participant A as 📱 앱
  participant B as ⚙️ 백엔드
  participant DB as 🗄️ PostgreSQL
  participant CH as ⛓️ OmniOne Chain
  participant IS as 📜 Open DID Issuer

  A->>B: 영상 파일 + 제목
  B->>B: ISSUER 권한 · DID 확인
  B->>B: fineHash (SHA-256)
  B->>DB: 중복 확인
  B->>B: perceptualHash (프레임 DCT)
  B->>DB: 동일 콘텐츠 확인
  B->>B: merkleRoot + 서명 생성

  rect rgb(238, 244, 255)
  Note over B,DB: ① DB 선점이 먼저
  B->>DB: saveAndFlush (unique 제약)
  end
  rect rgb(238, 244, 255)
  Note over B,CH: ② 통과한 요청만 체인으로
  B->>CH: register(merkleRoot, DID, 서명)
  CH-->>B: txHash → 영수증 폴링 → blockNumber
  end

  B->>CH: getRecord 재조회
  B->>B: 온체인 값 ↔ DB 값 대조
  B->>IS: Holder + 보증 클레임 등록
  IS-->>B: 발급 Offer
  B-->>A: videoId · txHash · vcOfferId
```

**왜 DB를 먼저 저장할까요?**
블록체인을 먼저 부르면 동시에 들어온 같은 파일이 **여러 트랜잭션**을 만듭니다.
DB의 unique 제약으로 하나만 통과시킨 뒤 체인에 기록합니다.

**왜 기록 후 다시 조회할까요?**
트랜잭션 영수증만으로는 최종 상태를 보증할 수 없습니다.
확정된 값을 다시 읽어 대조한 뒤에야 보증서 발급을 시작합니다.

---

## 3 · 보증서 발급 — Wallet이 받아가는 구조

```mermaid
sequenceDiagram
  autonumber
  participant A as 📱 앱
  participant B as ⚙️ 백엔드
  participant IS as 📜 Issuer
  participant W as 🔐 Wallet

  Note over B: 온체인 등록 확정 후에만 시작
  B->>IS: 보증 클레임 등록
  IS-->>B: offerId
  B-->>A: vcPlanId · vcIssuerDid · vcOfferId

  A->>A: "등록 보증서를 발급할까요?"
  A->>W: offerId로 발급 시작
  W->>A: 사용자 동의 + PIN 인증
  W->>IS: issue-vc → confirm
  IS-->>W: 📜 VC
  W->>W: Wallet에 로컬 저장
  W-->>A: vcId
  A->>B: vcId + offerId
  B->>B: offerId 일치 확인 → Verifier 검증
  B-->>A: ✅ ISSUED
```

```mermaid
stateDiagram-v2
  [*] --> NOT_REQUESTED: 영상 등록
  NOT_REQUESTED --> PENDING_WALLET: Offer 생성
  PENDING_WALLET --> ISSUED: Wallet 수령 + 검증
```

VC에 담기는 것은 **온체인 등록 증거**입니다.

| 클레임 | 값 |
|---|---|
| 영상 디지털 지문 | `merkleRoot` |
| 등록자 DID | 영상을 등록한 사람 |
| 블록체인 네트워크 · 체인 ID · 컨트랙트 | 어디에 기록했는지 |
| 트랜잭션 해시 · 블록 번호 | 어느 기록인지 |
| 온체인 등록 시각 | 언제인지 |

> 원본 해시(`fineHash`, `perceptualHash`)는 VC에 넣지 않습니다. 대표값만 담습니다.

---

## 4 · 검증 — 누구나, 로그인 없이

```mermaid
sequenceDiagram
  autonumber
  participant U as 🌐 웹 · 🧩 확장
  participant B as ⚙️ 백엔드
  participant R as ⚡ Redis
  participant DB as 🗄️ DB
  participant CH as ⛓️ Chain
  participant V as 📜 Verifier

  U->>B: 영상 파일 또는 URL
  B->>R: 캐시 조회 (TTL 10분)
  alt 캐시 적중
    R-->>U: ⚡ 즉시 반환
  else 캐시 없음
    B->>B: fineHash 계산
    B->>DB: 정확 일치 조회
    alt 불일치
      B->>B: perceptualHash 계산
      B->>DB: 유사도 검색 (해밍 거리 &lt; 10)
    end
    B->>CH: getRecord(merkleRoot)
    B->>B: 서명 재계산 → 온체인 값과 대조
    opt VC 발급된 영상
      B->>V: 상태 + 서명 검증
    end
    B->>R: 결과 캐싱
    B-->>U: verdict + message + notice
  end
```

**무결성이 보장되는 이유**

```mermaid
flowchart LR
  A["DB의 서명"] --> C{"세 값이<br/>모두 일치?"}
  B["온체인의 서명"] --> C
  D["서버가 재계산한 서명"] --> C
  C -->|예| E["✅ 무결성 확인"]
  C -->|아니오| F["⚠️ VERIFICATION_UNAVAILABLE"]
  style E fill:#12B76A,color:#fff
  style F fill:#F79009,color:#fff
```

DB가 조작돼도 서버 비밀키 없이는 서명을 다시 만들 수 없고,
온체인 값은 애초에 바꿀 수 없습니다. **셋이 동시에 맞아야** 통과합니다.

---

## 장애가 나면 어떻게 되나

```mermaid
flowchart TD
  X1["📜 Issuer 장애"] --> Y1["영상 등록 ✅<br/>보증서 발급만 보류"]
  X2["📜 Verifier 장애"] --> Y2["VC 발급 영상만<br/>확인 불가로 표시"]
  X3["⛓️ Chain 장애"] --> Y3["등록 ❌<br/>검증은 확인 불가"]
  X4["⚡ Redis 장애"] --> Y4["느려질 뿐<br/>기능은 정상"]
  style Y1 fill:#12B76A,color:#fff
  style Y4 fill:#12B76A,color:#fff
  style Y2 fill:#F79009,color:#fff
  style Y3 fill:#F04438,color:#fff
```

일시 장애 결과(`VERIFICATION_UNAVAILABLE`)는 **캐싱하지 않습니다.**
10분 동안 잘못된 결과가 고정되는 것을 막기 위해서입니다.

---

각 흐름의 조건·예외·에러 코드까지 필요하면
**[reference/20-flows/](../reference/20-flows/video-verify.md)** 를 참고하세요.
