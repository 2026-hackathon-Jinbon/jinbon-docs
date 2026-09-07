# 스마트 컨트랙트

파일: `jinbon-backend/contracts/JinBon.sol`
체인: OmniOne Chain (BESU 기반)
Solidity: `^0.8.20` · 라이선스: MIT

## 목적

영상의 `merkleRoot`를 키로 등록자 DID와 서명을 온체인에 남깁니다.
검증 시 이 기록과 서버가 재계산한 값을 대조해 무결성을 판정합니다.

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

`records`와 `registered`가 모두 `private`이므로
외부에서는 `getRecord()`를 통해서만 조회할 수 있습니다.

`owner`는 `immutable`이며 생성자에서 배포자(`msg.sender`)로 고정됩니다.
소유권 이전 함수가 없으므로 **배포 후 변경할 수 없습니다.**

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
| 저장 | `active = true`, `registeredAt = block.timestamp`, `deactivatedAt = 0` |
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
| 권한 | `onlyOwner` |
| 사전 조건 | 등록됨(`"Not registered"`), 활성(`"Already deactivated"`), DID 일치(`"Not the original issuer"`) |
| 변경 | `active = false`, `deactivatedAt = block.timestamp` |
| 이벤트 | `VideoDeactivated(merkleRoot, issuerDid, timestamp)` |

DID 비교는 `keccak256(bytes(...))`로 합니다. Solidity에서 문자열은 직접 비교할 수 없기 때문입니다.

기록은 삭제하지 않고 `active` 플래그만 내립니다.
등록 이력 자체는 영구히 남으므로 "등록되었다가 취소되었다"는 사실을 계속 증명할 수 있습니다.

### getRecord

```solidity
function getRecord(string calldata merkleRoot)
    external view
    returns (
        bool isRegistered,
        bool isActive,
        string memory issuerDid,
        string memory signature,
        uint256 registeredAt
    )
```

권한 제한이 없는 `view` 함수입니다. 누구나 조회할 수 있습니다.
미등록 merkleRoot는 `(false, false, "", "", 0)`을 반환합니다.

반환값에 `signature`가 포함되는 것이 중요합니다.
서버는 이 값을 자신이 재계산한 서명과 대조해 DB 조작을 탐지합니다.

## 이벤트

```solidity
event VideoRegistered(string indexed merkleRoot, string issuerDid, uint256 timestamp);
event VideoDeactivated(string indexed merkleRoot, string issuerDid, uint256 timestamp);
```

`merkleRoot`가 `indexed`이므로 특정 영상의 등록·비활성 이력을 로그에서 필터링할 수 있습니다.

> 동적 타입인 `string`을 `indexed`로 선언하면 원본이 아니라 keccak256 해시가 토픽에 들어갑니다.
> 로그 필터링 시 해시로 조회해야 하며, 이벤트에서 원본 문자열을 읽을 수는 없습니다.
> 다만 두 이벤트 모두 `issuerDid`를 non-indexed로 함께 담고 있어 데이터 부분에서 확인 가능합니다.

## 백엔드 연동

| 백엔드 코드 | 컨트랙트 함수 |
|---|---|
| `ContractEncoder.encodeRegister(merkleRoot, issuerDid, signature)` | `register` |
| `ContractEncoder.encodeDeactivate(merkleRoot, issuerDid)` | `deactivate` |
| `ContractEncoder.encodeGetRecord(merkleRoot)` | `getRecord` |
| `ContractDecoder.decodeGetRecord(result)` | 반환값 → `VideoRecord` 레코드 |

`register`와 `deactivate`는 `OmniOneChainClient.sendTransaction()`으로 상태 변경 트랜잭션을,
`getRecord`는 `ethCall()`로 조회를 수행합니다.

## 접근 제어의 의미

`onlyOwner` 때문에 **모든 온체인 쓰기는 진본 백엔드의 배포 지갑을 거칩니다.**
사용자가 직접 체인에 기록할 수는 없습니다.

이 설계의 결과:

- 장점 — 등록 전 권한·중복 검증을 서버가 강제할 수 있고, 사용자가 가스비를 부담하지 않습니다.
- 한계 — 진본 서버가 신뢰의 단일 지점이 됩니다. 서버 지갑이 탈취되면 임의 등록이 가능합니다.

`deactivate`의 DID 일치 검사는 서버가 잘못된 영상을 비활성화하는 실수를 막는
2차 방어선 역할을 합니다.

## 배포 시 주의

컨트랙트에 접근 제어와 온체인 signature 조회가 추가되면서
**이전 버전과 ABI가 호환되지 않습니다.**

1. `contracts/JinBon.sol`을 새로 배포
2. `.env`의 `CONTRACT_ADDRESS`를 새 주소로 변경
3. `WALLET_ADDRESS`와 `src/main/resources/keystore/omnione-chain-keystore.json`이
   **배포에 사용한 그 지갑**인지 확인

3번이 어긋나면 `register`와 `deactivate`가 `"Only owner"`로 revert되어
영상 등록이 전부 실패합니다.

`.env.example`에도 다음 주석으로 명시되어 있습니다.

```
# TODO(deployment): 변경된 contracts/JinBon.sol을 신규 배포한 뒤 새 주소 입력
CONTRACT_ADDRESS=
# 컨트랙트를 배포한 동일 지갑 주소를 사용
WALLET_ADDRESS=
```

## 온체인에 남지 않는 것

| 항목 | 온체인 |
|---|---|
| `merkleRoot` | 기록됨 |
| 등록자 DID | 기록됨 |
| 서명 | 기록됨 |
| 등록·비활성 시각 | 기록됨 |
| `fineHash` / `perceptualHash` | **기록 안 함** |
| 영상 제목 | **기록 안 함** |
| 영상 파일 | **기록 안 함** |
| CI·이름·생년월일 | **기록 안 함** |

개인정보와 원본 해시는 체인에 올리지 않고, 대표값인 `merkleRoot`만 남깁니다.
