# 서비스 한눈에

## 문제

```mermaid
flowchart LR
  O["📹 원본 영상"] -->|재인코딩| A["파일이 달라짐"]
  O -->|자막·편집| B["파일이 달라짐"]
  O -->|재업로드| C["파일이 달라짐"]
  A --> Q(["❓ 어느 것이 원본?<br/>❓ 누가 공개했나?"])
  B --> Q
  C --> Q
  style O fill:#EEF4FF,stroke:#2457E6
  style Q fill:#F04438,color:#fff
```

파일이 조금만 달라져도 단순 비교로는 **같은 영상인지조차** 알 수 없습니다.

---

## 해결 — 두 갈래 증명

```mermaid
flowchart TD
  V["📹 영상"] --> H1["fineHash<br/><sub>SHA-256 전체 파일</sub>"]
  V --> H2["perceptualHash<br/><sub>프레임 DCT 지각해시</sub>"]
  H1 --> M["merkleRoot"]
  H2 --> M
  M --> CH["⛓️ OmniOne Chain<br/><b>무결성 증명</b><br/><sub>변조되지 않았는가</sub>"]
  M --> VC["📜 Open DID VC<br/><b>신뢰성 증명</b><br/><sub>누가 언제 등록했는가</sub>"]
  style CH fill:#2457E6,color:#fff
  style VC fill:#12B76A,color:#fff
  style M fill:#111827,color:#fff
```

| 해시 | 성격 | 잡아내는 것 |
|---|---|---|
| **fineHash** | 바이트 단위 | 완전히 동일한 원본 파일 |
| **perceptualHash** | 내용 기반 | 재인코딩·리사이즈해도 **같은 영상** |

두 해시를 이어 SHA-256을 한 번 더 → `merkleRoot` → **이 값만 블록체인에 기록**

---

## 검증 판정 7단계

```mermaid
flowchart TD
  S["🔍 영상 검증"] --> E{"파일 해시<br/>일치?"}
  E -->|예| R1["✅ EXACT_MATCH<br/><sub>등록된 원본 그대로</sub>"]
  E -->|아니오| P{"지각해시<br/>유사?"}
  P -->|거리 0| R2["✅ SAME_CONTENT<br/><sub>같은 영상</sub>"]
  P -->|거리 &lt;10| R3["✅ SIMILAR_MATCH<br/><sub>재인코딩된 같은 영상</sub>"]
  P -->|불일치| R4["⬜ NOT_REGISTERED<br/><sub>등록 이력 없음</sub>"]
  R1 --> C{"등록 상태<br/>확인"}
  R2 --> C
  R3 --> C
  C -->|비활성화됨| R5["⚠️ REGISTERED_BUT_REVOKED"]
  C -->|보증서 무효| R6["⚠️ CERTIFICATE_INVALID"]
  C -->|외부 장애| R7["⚠️ VERIFICATION_UNAVAILABLE"]
  style R1 fill:#12B76A,color:#fff
  style R2 fill:#2457E6,color:#fff
  style R3 fill:#2457E6,color:#fff
  style R4 fill:#EAECF0
  style R5 fill:#F79009,color:#fff
  style R6 fill:#F79009,color:#fff
  style R7 fill:#F79009,color:#fff
```

> **미등록은 조작의 증거가 아닙니다.** 등록된 적이 없다는 뜻일 뿐이며,
> 서버가 이 안내 문구를 응답에 함께 담아 보냅니다.

---

## 해커톤 과제 대응

```mermaid
flowchart LR
  subgraph 필수["필수과제"]
    CX["📇 OmniOne CX<br/>모바일 신분증"]
  end
  subgraph 선택1["선택과제 1"]
    OD["📜 Open DID<br/>VC 발급·검증"]
  end
  subgraph 선택2["선택과제 2"]
    OC["⛓️ OmniOne Chain<br/>온체인 기록"]
  end
  CX -->|본인확인된 등록자| J["진본"]
  OC -->|무결성| J
  OD -->|신뢰성| J
  style J fill:#111827,color:#fff
  style CX fill:#F79009,color:#fff
  style OD fill:#12B76A,color:#fff
  style OC fill:#2457E6,color:#fff
```

| 과제 | 진본에서의 역할 | 상태 |
|---|---|---|
| 필수 · OmniOne CX | 등록자 본인확인 및 로그인 | ✅ 구현 |
| 선택 1 · Open DID | 온체인 등록 사실을 보증하는 VC | ✅ 구현 |
| 선택 2 · OmniOne Chain | merkleRoot 기록 + 서명 대조 | ✅ 구현 |

---

## 사용자와 채널

```mermaid
flowchart LR
  I["👤 공인 등록자<br/><sub>본인확인 + DID 연결</sub>"] -->|영상 등록| APP["📱 iOS 앱"]
  U["👥 누구나<br/><sub>로그인 불필요</sub>"] -->|검증| WEB["🌐 웹"]
  U -->|검증| EXT["🧩 Chrome 확장"]
  U -->|검증| APP
  APP --> BE["⚙️ 진본 백엔드"]
  WEB --> BE
  EXT --> BE
  style I fill:#2457E6,color:#fff
  style U fill:#F79009,color:#fff
  style BE fill:#111827,color:#fff
```

| 채널 | 하는 일 | 로그인 |
|---|---|---|
| 📱 **iOS 앱** | 가입 · DID/Wallet 관리 · **영상 등록** · 보증서 보관 | 필요 |
| 🌐 **웹** | 영상 파일 올려 검증 | 불필요 |
| 🧩 **Chrome 확장** | 보고 있는 YouTube 영상 즉시 검증 | 불필요 |

---

## 설계상 중요한 선택

```mermaid
flowchart LR
  A["영상 등록"] -->|성공| B["⛓️ 블록체인 기록 확정"]
  B --> C{"VC 발급"}
  C -->|성공| D["📜 보증서 발급 완료"]
  C -->|실패·나중에| E["등록은 그대로 유지<br/><sub>언제든 재발급 가능</sub>"]
  E -.->|재시도| C
  style B fill:#2457E6,color:#fff
  style D fill:#12B76A,color:#fff
  style E fill:#EEF4FF,stroke:#2457E6
```

**등록과 보증서 발급을 분리**했습니다.
Open DID 서버가 꺼져 있어도 영상 등록·블록체인 기록·검증은 정상 동작합니다.

| 지키는 원칙 | 방법 |
|---|---|
| 원본 영상을 서버에 남기지 않음 | 해시 계산 후 임시 파일 즉시 삭제 |
| 개인 식별정보(CI)를 저장하지 않음 | HMAC-SHA256 해시만 보관 |
| 중복 등록 차단 | 파일해시 · 내용해시 · DB 제약 **3중** |
| 동시 요청에 중복 트랜잭션 방지 | DB 선점 후 블록체인 전송 |
| DB가 조작돼도 탐지 | 서명 재계산 후 **온체인 값과 대조** |

---

→ 화면이 궁금하다면 **[화면 흐름](02-screen-flow.md)**
→ 동작 순서가 궁금하다면 **[핵심 시퀀스](03-key-sequences.md)**
