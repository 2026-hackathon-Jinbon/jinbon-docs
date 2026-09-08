# 스마트 컨트랙트

파일: `jinbon-backend/contracts/JinBon.sol`
체인: OmniOne Chain (BESU 기반) · Solidity `^0.8.20`

## 목적

영상의 `merkleRoot`를 키로 등록자 DID와 서명을 온체인에 남깁니다. 검증 시 이 기록과 서버가 재계산한 값을 대조해 무결성을 판정합니다.

## 저장 구조

```solidity
struct VideoRecord {
    string issuerDid;
    string signature;
    bool active;
    uint256 registeredAt;
    uint256 deactivatedAt;
}

mapping(string => VideoRecord) private records;
mapping(string => bool) private registered;
address public immutable owner;
```

`owner`는 배포자(`msg.sender`)로 고정되며, 소유권 이전 함수가 없어 **변경 불가**합니다.

## 함수

### register

```solidity
function register(
    string calldata merkleRoot,
    string calldata issuerDid,
    string calldata signature
) external onlyOwner
```

| 항목 | 내용 |
|---|---|
| 권한 | `onlyOwner` — 배포 지갑만 |
| 사전 조건 | `!registered[merkleRoot]`, 위반 시 `"Already registered"` |
| 이벤트 | `VideoRegistered(merkleRoot, issuerDid, timestamp)` |

### deactivate

```solidity
function deactivate(
    string calldata merkleRoot,
    string calldata issuerDid
) external onlyOwner
```

| 항목 | 내용 |
|---|---|
| 사전 조건 | 등록됨, 활성, DID 일치 |
| 변경 | `active = false`, `deactivatedAt = block.timestamp` |
| 이벤트 | `VideoDeactivated(merkleRoot, issuerDid, timestamp)` |

기록은 삭제하지 않고 `active` 플래그만 내립니다.

### getRecord

```solidity
function getRecord(string calldata merkleRoot)
    external view
    returns (
        bool isRegistered, bool isActive,
        string memory issuerDid, string memory signature,
        uint256 registeredAt
    )
```

권한 제한 없는 `view` 함수입니다. 누구나 조회할 수 있습니다.

## 이벤트

```solidity
event VideoRegistered(string indexed merkleRoot, string issuerDid, uint256 timestamp);
event VideoDeactivated(string indexed merkleRoot, string issuerDid, uint256 timestamp);
```

## 백엔드 연동

| 백엔드 코드 | 컨트랙트 함수 |
|---|---|
| `ContractEncoder.encodeRegister(...)` | `register` |
| `ContractEncoder.encodeDeactivate(...)` | `deactivate` |
| `ContractEncoder.encodeGetRecord(...)` | `getRecord` |
| `ContractDecoder.decodeGetRecord(...)` | 반환값 → `VideoRecord` |

## 접근 제어

`onlyOwner` 때문에 **모든 온체인 쓰기는 진본 백엔드의 배포 지갑을 거칩니다.**

- **장점** — 등록 전 권한·중복 검증을 서버가 강제, 가스비 사용자 부담 없음
- **한계** — 진본 서버가 신뢰의 단일 지점. 서버 지갑 탈취 시 임의 등록 가능

## 온체인에 남는 것 / 남지 않는 것

| 항목 | 온체인 |
|---|---|
| merkleRoot, 등록자 DID, 서명, 시각 | O |
| fineHash, perceptualHash, 영상 제목, 영상 파일, CI·이름 | **X** |
