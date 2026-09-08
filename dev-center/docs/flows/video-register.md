# 영상 등록

`POST /api/videos` · 권한: `ISSUER` · 요청 형식: `multipart/form-data` (`file`, `title`)

## 전체 순서

```mermaid
sequenceDiagram
  participant A as 앱
  participant B as 백엔드
  participant DB as PostgreSQL
  participant CH as OmniOne Chain
  participant IS as Open DID Issuer

  A->>B: POST /api/videos (file, title)
  B->>B: 회원 조회 + ISSUER 권한·DID 확인
  B->>B: fineHash = SHA-256(파일)
  B->>DB: fineHash로 기존 영상 조회
  alt 같은 회원의 동일 파일
    B-->>A: 기존 결과 (alreadyRegistered=true)
  else 다른 회원의 동일 파일
    B-->>A: 409 VIDEO_ALREADY_REGISTERED
  end

  B->>B: perceptualHash = 프레임별 pHash
  B->>DB: 동일 콘텐츠 영상 조회 (거리 0)
  Note over B,DB: 소유자 판정은 위와 동일

  B->>B: merkleRoot = SHA-256(pHash + fineHash)
  B->>B: signature = HMAC-SHA256(issuerDid + merkleRoot)
  B->>DB: saveAndFlush (unique 제약으로 등록 권한 선점)
  B->>CH: register(merkleRoot, issuerDid, signature)
  CH-->>B: txHash
  B->>CH: 영수증 폴링 (250ms × 최대 20회)
  CH-->>B: blockNumber
  B->>DB: recordBlockchain(blockNumber, txHash)

  B->>CH: getRecord(merkleRoot) 재조회
  B->>B: 온체인 값과 DB 값 대조
  B->>IS: Holder DID + 보증 클레임 등록
  B->>IS: 발급 Offer 생성
  IS-->>B: offerId, issuerDid
  B->>DB: markVcPending → PENDING_WALLET
  B-->>A: videoId, merkleRoot, txHash, blockNumber, vcPlanId, vcIssuerDid, vcOfferId
```

## 단계별 상세

### 1. 권한 검증

```
role != ISSUER            → ISSUER_ROLE_REQUIRED (V001, 403)
member.userDid == null    → ISSUER_DID_NOT_REGISTERED (V002, 400)
```

### 2. fineHash 생성과 중복 확인

파일 전체를 8KB 버퍼로 스트리밍하며 SHA-256을 계산합니다. `videos.fine_hash`에 unique 제약이 있어 DB 레벨에서도 중복이 막힙니다.

**중복 발견 시 소유자 판정:**

| 상황 | 결과 |
|---|---|
| 같은 회원 | 기존 등록 결과 반환, `alreadyRegistered = true` |
| 다른 회원 | `VIDEO_ALREADY_REGISTERED` (V004, 409) |

### 3. perceptualHash 생성과 동일 콘텐츠 확인

양방향 거리가 모두 0.0인 영상을 찾아 동일 콘텐츠로 판정합니다. 한쪽만 0인 경우는 부분 포함 관계일 수 있어 제외합니다.

### 4. merkleRoot와 서명

```
merkleRoot = SHA-256(perceptualHash || fineHash)
signature  = HMAC-SHA256(issuerDid + merkleRoot)
```

### 5. DB 선점 후 블록체인 기록

동시성 방어의 핵심입니다.

```java
Video saved = videoRepository.saveAndFlush(video);   // 먼저 DB
String txHash = sendBlockchainTx(encodeRegister(...)); // 통과한 요청만 체인
```

트랜잭션 영수증은 250ms 간격으로 최대 20회(약 5초) 폴링합니다.

### 6. 온체인 증거 재확인

VC에 담을 증거가 실제 온체인 상태와 일치하는지 다시 확인합니다.

### 7. VC 발급 준비

발급 준비가 실패해도 등록 결과는 유지됩니다. (`try/catch`로 감싸져 있음)

## 비활성화

`PATCH /api/videos/{videoId}/deactivate`

블록체인 기록이 먼저이고 DB 변경이 나중입니다. 체인 전송이 실패하면 트랜잭션이 롤백되어 DB도 활성 상태로 남습니다.

::: tip 저장하지 않는 것
원본 영상 파일은 서버에 남지 않습니다. 지각해시 계산용 임시 파일은 `finally` 블록에서 즉시 삭제합니다.
:::
