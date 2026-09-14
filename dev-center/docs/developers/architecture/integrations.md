# 외부 연동

진본은 세 개의 외부 시스템과 하나의 CLI 도구를 사용합니다.

## 1. OmniOne CX — 모바일 신분증

### 역할
등록자의 본인확인. 신분증 검증 결과에서 CI·이름·생년월일만 취합합니다.

### 연동 지점
- 클라이언트: `OmniOneCxClient`, `OmniOneCxApi`
- 설정: `omnione.cx.server-url` (`OMNIONE_CX_URL`)
- 인증사 코드: `comdl` (모바일 운전면허증)

### 개인정보 처리
CI 원문은 저장하지 않습니다. `CiHasher`가 HMAC-SHA256으로 변환한 `h1:` 접두사 문자열만 `members.ci` 컬럼에 저장합니다. 이 값은 회원 중복 확인·로그인·DID 복구에만 쓰이고, VC·DID Document·블록체인에는 포함되지 않습니다.

## 2. Open DID — VC 보증서

### 역할
"이 영상이 언제, 어떤 온체인 기록으로 등록되었는가"를 보증하는 VC를 발급하고 검증합니다.

### 구성

Open DID Orchestrator 2.0.0이 다음 서버를 관리합니다.

| 서버 | 포트 | 백엔드 호출 | 앱 호출 |
|---|---|---|---|
| Orchestrator UI | 9001 | — | — |
| TAS | 8090 | 아니오 | 예 |
| Issuer | 8091 | **예** | 예 |
| Verifier | 8092 | **예** | 예 |
| API Gateway | 8093 | 아니오 | 예 |
| CA | 8094 | 아니오 | 예 |
| Wallet | 8095 | 아니오 | 예 |

::: info 별도 체인
DID Document 앵커링용 블록체인은 Hyperledger Besu이며, 영상 기록용 OmniOne Chain과 **다른 체인**입니다.
:::

### 백엔드 클래스

| 클래스 | 역할 |
|---|---|
| `VcIssuanceService` | 발급 준비 오케스트레이션 |
| `OpenDidIssuerClient` | Holder·클레임 등록, Offer 생성 |
| `VcVerificationService` | 상태·서명 검증 |
| `OpenDidVerifierClient` | VC 상태 조회, 서명 검증 |

### 검증 판정

| 값 | 조건 |
|---|---|
| `VERIFIED` | 상태 `ACTIVE` + 서명 `VALID` |
| `INVALID` | 상태가 ACTIVE가 아니거나 서명 실패 |
| `UNAVAILABLE` | Verifier 호출 중 예외 발생 |
| `DISABLED` | `opendid.enabled=false` 이거나 VC 미발급 |

## 3. OmniOne Chain — 온체인 등록

### 역할
영상의 `merkleRoot`, 등록자 DID, 서명을 블록체인에 기록하고 검증 시 대조합니다.

### 연동 방식
- 체인: OmniOne Chain (BESU 기반)
- 접근: JSON-RPC + API 토큰
- 라이브러리: web3j 4.12.3
- 서명 지갑: `src/main/resources/keystore/omnione-chain-keystore.json`

### 클래스

| 클래스 | 역할 |
|---|---|
| `OmniOneChainClient` | 트랜잭션 전송, ethCall, 영수증 조회 |
| `ContractEncoder` | register, deactivate, getRecord 인코딩 |
| `ContractDecoder` | getRecord 디코딩 |

::: warning onlyOwner 제한
`register`와 `deactivate`에 `onlyOwner`가 걸려 있어 **컨트랙트 배포 지갑만** 호출할 수 있습니다. `.env`의 `WALLET_ADDRESS`와 keystore가 배포 지갑과 반드시 일치해야 합니다.
:::

### 트랜잭션 확정 대기
영수증을 250ms 간격으로 최대 20회(약 5초) 폴링합니다. 실패 시 `BLOCKCHAIN_TX_FAILED`(V008, 500).

## 4. yt-dlp — URL 영상 다운로드

외부 서비스가 아닌 서버에 설치하는 CLI 도구입니다.

- 사용처: `VideoDownloadService`
- 호출 시점: `POST /api/verify/url`
- 처리: 다운로드 → 해시 계산 → 즉시 삭제
- 미설치 시 URL 검증만 실패, 파일 업로드 검증은 정상

## 연동별 실패 영향

| 연동 | 끊겼을 때 |
|---|---|
| OmniOne CX | 가입·로그인 불가. 검증은 정상 |
| Open DID Issuer | VC 발급 준비만 실패. 영상 등록은 성공 |
| Open DID Verifier | VC 발급 영상 검증이 `VERIFICATION_UNAVAILABLE` |
| OmniOne Chain | 등록 실패, 검증은 `VERIFICATION_UNAVAILABLE` |
| yt-dlp | URL 검증만 실패 |
