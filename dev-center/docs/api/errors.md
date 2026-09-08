# 에러 코드

`V004`만 한국어 메시지이고 나머지는 영문입니다.
클라이언트가 코드로 분기해 사용자 문구를 만드는 것을 전제로 합니다.

## 공통 (C)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `C001` | 500 | Internal server error. |
| `C002` | 413 | Upload size exceeds the 100MB limit. |
| `C003` | 400 | Invalid request. |

## 인증 (A)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `A001` | 401 | ID verification failed. |
| `A002` | 401 | Invalid refresh token. |
| `A003` | 400 | Not a refresh token. |
| `A004` | 401 | Expired or already used refresh token. |
| `A005` | 400 | Failed to retrieve CI information. |
| `A006` | 400 | Not a signup token. |
| `A007` | 409 | ID verification is still in progress. |
| `A008` | 401 | Invalid or expired DID rebind token. |

## 회원 (M)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `M001` | 404 | Member not found. |
| `M002` | 409 | Member is already registered. |
| `M003` | 409 | DID registration is not completed. |
| `M004` | 403 | Member is not active. |
| `M005` | 409 | DID is already registered. |

## 영상 (V)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `V001` | 403 | Only ISSUER role can register videos. |
| `V002` | 400 | Issuer DID is not registered. |
| `V003` | 500 | Failed to process video file. |
| `V004` | 409 | 동일한 영상이 다른 계정에 이미 등록되어 있습니다. |
| `V005` | 404 | Video not found. |
| `V006` | 403 | Not the owner of this video. |
| `V007` | 400 | Video is already deactivated. |
| `V008` | 500 | Blockchain transaction failed. |
| `V009` | 500 | Failed to generate signature. |

## 검증 (VF)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `VF001` | 500 | Blockchain verification failed. |
| `VF002` | 400 | Failed to download video from URL. |

## VC / Open DID (D)

| 코드 | HTTP | 메시지 |
|---|---|---|
| `D001` | 500 | Failed to issue verifiable credential. |
| `D002` | 500 | Failed to verify verifiable credential. |
| `D003` | 500 | Failed to revoke verifiable credential. |
| `D004` | 400 | VC issuance is not in PENDING_WALLET state. |
| `D005` | 400 | VC offer does not match this video. |
| `D006` | 503 | Open DID VC integration is disabled. |
