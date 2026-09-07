# 용어 사전

진본 문서 전반에서 쓰는 용어를 정리합니다. 코드에 등장하는 식별자는 백틱으로 표기했습니다.

## 신원과 자격증명

| 용어 | 설명 |
|---|---|
| **DID** | Decentralized Identifier. 중앙 기관 없이 소유자가 통제하는 분산 식별자. 진본에서는 Wallet이 생성한 Holder DID(`userDid`)를 회원과 1:1로 연결합니다. |
| **DID Document** | DID에 연결된 공개키와 서비스 정보를 담은 문서. Hyperledger Besu에 앵커링됩니다. |
| **VC** | Verifiable Credential. 발급기관이 서명한 검증 가능한 디지털 증명서. 진본에서는 "이 영상이 블록체인에 등록되었다"는 사실을 보증합니다. |
| **Holder** | VC를 보유하는 주체. 진본에서는 영상 등록자(앱 사용자)입니다. |
| **Issuer** | VC를 발급하는 기관. 진본 서비스가 Issuer 역할을 합니다. |
| **Verifier** | VC의 유효성을 검증하는 주체. Open DID Verifier 서버가 담당합니다. |
| **TAS** | Trust Agent Server. Open DID의 신뢰 관리 서버. |
| **CA** | Certificate Authority. Open DID의 인증서 발급 서버. |
| **Wallet** | 사용자의 DID와 VC를 보관하는 앱 내 저장소. iOS 앱은 `DIDWalletSDK`를 사용합니다. |
| **Offer** | Issuer가 만든 1회성 발급 제안. `vcOfferId`로 식별하며, Wallet이 이 값으로 발급을 시작합니다. |
| **VC Plan** | 발급할 VC의 스키마·정책 묶음. 진본은 `vcplan-jinbon-01`을 사용합니다. |

## 본인확인

| 용어 | 설명 |
|---|---|
| **OmniOne CX** | 모바일 신분증 검증 서비스. 진본의 필수과제 연동 대상입니다. |
| **모바일 신분증** | 정부 발급 모바일 신분증. 인증사 코드 `comdl`은 모바일 운전면허증입니다. |
| **WebToApp** | 웹에서 딥링크로 신분증 앱을 호출하는 인증 방식. 진본 앱은 웹뷰에서 이 방식을 씁니다. |
| **CI** | 연계정보(Connecting Information). 개인을 식별하는 고유값. **진본은 원문을 저장하지 않고** HMAC-SHA256 해시만 보관합니다. |
| **txId / cxId** | OmniOne CX 인증 세션의 트랜잭션 ID와 검증 컨텍스트 ID. |

## 해시와 블록체인

| 용어 | 설명 |
|---|---|
| **fineHash** | 영상 파일 전체의 SHA-256. DB에 unique 제약이 걸려 있어 동일 파일 중복 등록을 막습니다. |
| **perceptualHash (pHash)** | 프레임에서 DCT로 뽑은 64비트 지각해시의 목록. 재인코딩에 내성이 있습니다. |
| **핑거프린트** | 프레임별 pHash를 쉼표로 이어 붙인 문자열. `perceptualHash` 컬럼에 저장됩니다. |
| **해밍 거리** | 두 해시의 비트 차이 개수. 진본은 프레임별 최근접 매칭의 평균 거리를 유사도로 씁니다. |
| **merkleRoot** | `SHA-256(perceptualHash + fineHash)`. 블록체인에 기록되는 영상의 대표값입니다. |
| **merklePath** | 루트 재구성용 경로. `{"leaves": [pHash, fineHash], "root": ...}` JSON으로 저장합니다. |
| **signature** | `HMAC-SHA256(issuerDid + merkleRoot)`. 서버 비밀키로 만든 서명이며 온체인에도 함께 기록됩니다. |
| **OmniOne Chain** | BESU 기반 블록체인. 영상 등록 기록을 보관합니다. |
| **Hyperledger Besu** | Open DID Orchestrator가 DID Document 앵커링에 쓰는 별도 블록체인. |
| **txHash / blockNumber** | 등록 트랜잭션의 해시와 블록 번호. VC 클레임의 증거로 포함됩니다. |

> `merkleRoot`라는 이름을 쓰지만 실제 구조는 잎이 두 개인 최소 트리입니다.
> 두 해시를 이어 붙여 한 번 더 해싱한 값이며, 일반적인 다단 머클트리가 아닙니다.

## 판정과 상태

| 용어 | 설명 |
|---|---|
| **verdict** | 검증 결과의 구조화된 판정값. 7종이며 [영상 검증](../20-flows/video-verify.md)에서 설명합니다. |
| **authentic** | 진본 여부 boolean. 구버전 클라이언트 호환용이며 신규 화면은 `verdict`를 기준으로 합니다. |
| **similarityDistance** | 유사 일치일 때만 제공되는 평균 해밍 거리. |
| **MemberStatus** | `PENDING` → `ACTIVE`, 그 외 `SUSPENDED`, `WITHDRAWN`. |
| **MemberRole** | `USER`(레거시, 등록 불가) / `ISSUER`(등록 권한). |
| **VcIssuanceStatus** | `NOT_REQUESTED` → `PENDING_WALLET` → `ISSUED`. |
| **assuranceType** | VC의 보증 범위. 현재 값은 `BLOCKCHAIN_REGISTRATION` 하나입니다. |

## 진본 고유 표현

| 표현 | 의미 |
|---|---|
| **디지털 지문** | 사용자 화면에서 해시를 가리키는 말. iOS·웹 문구에 쓰입니다. |
| **등록 보증서** | 사용자 화면에서 VC를 가리키는 말. |
| **온체인 등록** | 영상 merkleRoot를 블록체인에 기록하는 행위. |
| **디지털 신원** | 사용자 화면에서 DID를 가리키는 말. |
