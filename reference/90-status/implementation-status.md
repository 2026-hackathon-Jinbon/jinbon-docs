# 구현 현황

기준일: 2026-09-07 · 코드 기준으로 확인한 내용입니다.

## 기능별 현황

| 기능 | 백엔드 | iOS | 웹 | 확장 |
|---|:---:|:---:|:---:|:---:|
| 모바일 신분증 본인확인 | 구현 | 구현 | — | — |
| 회원가입 (DID 연결) | 구현 | 구현 | — | — |
| 로그인 / 토큰 갱신 / 로그아웃 | 구현 | 구현 | — | — |
| DID 재연결 (앱 재설치) | 구현 | 구현 | — | — |
| 영상 등록 + 온체인 기록 | 구현 | 구현 | — | — |
| 중복 등록 방지 (3중) | 구현 | — | — | — |
| VC 보증서 발급 준비 | 구현 | 구현 | — | — |
| VC 발급 완료 연결 | 구현 | 구현 | — | — |
| VC 발급 재개 | 구현 | 구현 | — | — |
| 내 영상 목록 | 구현 | 구현 | — | — |
| 영상 상세 조회 | 구현 | 미사용 | — | — |
| 영상 비활성화 | 구현 | 구현 | — | — |
| 보증서 목록·상세 | — | 구현 | — | — |
| 파일 업로드 검증 | 구현 | 구현 | 구현 | — |
| URL 기반 검증 | 구현 | 구현 | 미구현 | 구현 |
| 검증 결과 캐싱 | 구현 | — | — | — |
| 오픈소스 라이선스 고지 | — | 구현 | — | — |

## 과제 대응 현황

| 과제 | 대상 | 구현 | 비고 |
|---|---|---|---|
| 필수 | OmniOne CX 모바일 신분증 | 구현 완료 | WebToApp 3단계 + CI 해싱 |
| 선택 1 | Open DID VC | 구현 완료 | 발급 준비·완료·검증·재개 |
| 선택 2 | OmniOne Chain | 구현 완료 | `JinBon.sol` register/deactivate/getRecord |

## 테스트 현황

### 백엔드

커밋된 테스트는 **모두 통과**합니다(`./gradlew test` 성공).

| 테스트 | 대상 |
|---|---|
| `ContractDecoderTest` | 컨트랙트 응답 디코딩 |
| `VcVerificationServiceTest` | VC 검증 상태 판정 |
| `OpenDidPropertiesTest` | 클레임 키 생성 |
| `VideoVerifyResponseTest` | 응답 DTO 팩토리 |
| `VideoTest` | 엔티티 상태 전이 |

다만 **커밋되지 않은 작업 중 파일 2개가 테스트 컴파일을 깨뜨립니다.**

```
src/test/java/com/jinbon/domain/video/service/   ← git 미추적
├── VideoRegisterServiceTest.java
└── VideoVerifyServiceTest.java
```

현재 상태로 `./gradlew test`를 실행하면 컴파일 오류 6건으로 중단됩니다.
원인은 이 파일들이 **존재하지 않는 메서드와 옛 생성자 시그니처**를 참조하기 때문입니다.

| 오류 | 내용 |
|---|---|
| `VideoRegisterService` 생성자 | 인자 9개로 호출, 실제는 12개 |
| `VideoVerifyService` 생성자 | 인자 7개로 호출, 실제는 9개 |
| `hashService.buildReRegistrationMerkleRoot(...)` | 해당 메서드 없음 |
| `hashService.buildReRegistrationMerklePath(...)` | 해당 메서드 없음 |
| `perceptualHashService.generateRotationFingerprints(...)` | 해당 메서드 없음 |

이 두 파일을 제외하면 컴파일과 테스트가 모두 성공하는 것을 확인했습니다.
참조된 메서드 이름(재등록 머클루트, 회전 핑거프린트)으로 보아
아직 구현되지 않은 기능을 앞서 작성한 테스트로 보입니다.

### 웹

`tests/rendered-html.test.mjs` 하나가 있고 `npm run test`는 빌드 후 실행됩니다.
현재 `node_modules`가 설치되어 있지 않아 **이번 문서 작성 과정에서는 실행하지 않았습니다.**

### iOS · 확장

`DIDCATests`, `DIDCAUITests` 타깃이 있으나 진본 화면을 다루는 테스트는 없습니다.
확장에는 테스트가 없습니다.

## 배포 준비 상태

배포 전 반드시 처리해야 하는 항목입니다.

| 항목 | 현재 | 필요한 조치 |
|---|---|---|
| `JinBon.sol` 배포 | 미완 | 신규 배포 후 `CONTRACT_ADDRESS` 갱신 (기존 ABI와 비호환) |
| 배포 지갑 일치 | 확인 필요 | `WALLET_ADDRESS`·keystore를 배포 지갑과 일치시킬 것 |
| iOS `Prod.xcconfig` | 자리표시자 | `*.example.com`을 실제 도메인으로 교체 |
| iOS ATS | 열림 | `NSAllowsArbitraryLoads`를 `false`로 |
| Spring 프로필 | 미지정 시 dev | 운영에서 프로필 명시 (Swagger·`auth.html` 노출 방지) |
| CORS | 전체 허용 | `cors.allowed-origins` 지정 |
| 로그 레벨 | DEBUG + SQL 출력 | 운영 수준으로 하향 |
| 확장 `host_permissions` | localhost 고정 | 운영 백엔드 호스트 추가 |
| 웹 `NEXT_PUBLIC_API_BASE_URL` | localhost | 운영 주소로 빌드 |
| keystore 위치 | `src/main/resources` | 외부 시크릿으로 분리 검토 |

## 미구현 · 계획만 있는 항목

| 항목 | 상태 |
|---|---|
| 카카오 챗봇 채널 | 백엔드 플로우 문서에 채널로 기재되어 있으나 저장소·구현 없음 |
| 회원 정지(`SUSPENDED`) / 탈퇴(`WITHDRAWN`) | enum만 정의, 전이 API·화면 없음 |
| VC 폐기 | `VC_REVOCATION_FAILED`(D003) 코드만 정의 |
| 등록자 심사 절차 | 가입 완료 시 전원 `ISSUER` 자동 부여 |
| 웹의 URL 검증 | 백엔드 API는 있으나 웹에 입력란 없음 |
| 재등록 머클루트 / 회전 핑거프린트 | 미추적 테스트가 참조하나 구현 없음 |
| 유사도 검색 최적화 | 전체 활성 영상 메모리 순회 (MVP 방식) |

## 알려진 제약

| 제약 | 설명 |
|---|---|
| 유사도 검색 성능 | 영상 수에 선형 비례. 인덱싱 없음 |
| `JWT_SECRET` 교체 불가 | 영상 서명 키를 겸하고 있어 교체 시 전체 검증이 깨짐 |
| `CI_HMAC_SECRET` 교체 불가 | 교체 시 기존 회원 조회 불가 |
| 블록체인 필수 | 끄는 스위치가 없어 체인 없이는 등록 불가 |
| Redis 주소 고정 | `application.yml`에 하드코딩 |
| Open DID 서버 주소 고정 | `application.yml`에 하드코딩 |
| 트랜잭션 확정 5초 | 초과 시 등록 실패 |
| 프레임 20초 분량 | 최대 10프레임 × 2초 간격 |

## 채널별 완성도 요약

| 채널 | 완성도 | 설명 |
|---|---|---|
| 백엔드 | 높음 | 전 기능 구현, 보안 방어 다수, 테스트 일부 |
| iOS | 높음 | 전 흐름 구현, verdict 7종 개별 표현 |
| 웹 | 중간 | 검증 동작하나 verdict 3종으로 축약, 구버전 타입 잔존 |
| 확장 | 중간 | 동작하나 판정 영문 노출, Netflix 미지원 |

자세한 불일치 항목은 [알려진 이슈](open-issues.md)를 참고합니다.
