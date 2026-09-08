# 보안 및 개인정보

## 저장하지 않는 데이터

| 데이터 | 처리 |
|---|---|
| 영상 원본 파일 | 해시 계산 후 즉시 삭제 |
| CI 원문 | HMAC-SHA256 해시만 저장 (`h1:` 접두사) |
| 지각해시 임시 파일 | `finally`에서 삭제 |
| URL 다운로드 영상 | 해시 계산 후 삭제 |

## CI 보호

```
저장값 = "h1:" + HMAC-SHA256(CI, CI_HMAC_SECRET)
```

- 키: `CI_HMAC_SECRET` (32자 이상, JWT_SECRET과 반드시 다른 값)
- 용도: 회원 중복 확인, 로그인 시 회원 조회
- VC·DID Document·블록체인에는 포함되지 않음

::: danger CI_HMAC_SECRET 변경 금지
키가 바뀌면 같은 CI가 다른 해시를 만들어 전 회원의 로그인이 불가능해집니다.
:::

## 인증과 인가

### 경로별 정책

| 경로 | 인증 |
|---|---|
| `/api/auth/**`, `/api/signup/**`, `/api/verify/**` | 불필요 |
| `/swagger-ui/**`, `/v3/api-docs/**` | 개발 프로필에서만 |
| 그 외 | JWT 필요 |

- 세션 `STATELESS`, CSRF 비활성 (토큰 기반)
- 활성 프로필 미지정 시 개발 모드로 간주

### 토큰

| 토큰 | 만료 | 무효화 |
|---|---|---|
| access | 30분 | 만료까지 유효 (서버 폐기 불가) |
| refresh | 7일 | 로그아웃·로테이션 시 즉시 무효 |
| signup | 단기 | 가입 완료 시 소비 |
| did-rebind | 단기 | 재연결 시 소비 |

Refresh Token Rotation 적용 — 갱신 시 이전 토큰 즉시 폐기.

## SSRF 방어

URL 검증은 서버가 외부 주소로 요청을 보내므로 SSRF 위험이 있습니다. 네 겹으로 방어합니다.

| 단계 | 규칙 |
|---|---|
| 1 | 스킴이 `https`여야 함 |
| 2 | 호스트가 허용 목록에 있어야 함 |
| 3 | `userInfo` 없음, 명시적 포트 없음 |
| 4 | DNS 응답의 **모든** IP가 공인 IP여야 함 |

차단하는 주소 유형: 루프백, 사설 IP, 링크로컬 (클라우드 메타데이터), 멀티캐스트

## 리소스 보호

| 대상 | 조치 |
|---|---|
| 업로드 크기 | 파일 100MB, 요청 110MB |
| URL 길이 | 최대 2048자 |
| `vcId` / `offerId` | 각 500자 |
| Redis 캐시 키 | URL을 SHA-256 해싱해 키 길이 고정 |
| 블록체인 폴링 | 250ms × 20회에서 중단 |

## 동시성 방어

DB 저장을 블록체인 전송보다 먼저 수행하여 동시 요청에 의한 중복 트랜잭션을 방지합니다.

```java
videoRepository.saveAndFlush(video);   // unique 제약으로 선점
sendBlockchainTx(...);                 // 통과한 요청만 체인
```

## 키와 비밀값

| 항목 | 비고 |
|---|---|
| `JWT_SECRET` | 토큰 서명 + 영상 서명 겸용 |
| `CI_HMAC_SECRET` | 32자 이상, 변경 금지 |
| `DB_PASSWORD` | |
| `KEYSTORE_PASSWORD` | 블록체인 지갑 keystore 암호 |
| `BLOCKCHAIN_API_TOKEN` | OmniOne Chain API 토큰 |

::: warning 서명 키 공유 주의
영상 서명과 JWT가 같은 키를 사용합니다. JWT_SECRET을 교체하면 기존 모든 영상의 서명 재계산이 달라져 **모든 검증이 `VERIFICATION_UNAVAILABLE`이 됩니다.**
:::

## CORS

```yaml
cors.allowed-origins: ""   # 미설정 시 전체 허용 (개발 모드)
```

운영에서는 웹 도메인과 확장 오리진(`chrome-extension://{id}`)만 허용해야 합니다.
