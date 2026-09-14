# iOS 앱 구조

저장소: `jinbon-ios` · 프로젝트: `source/DIDCA.xcodeproj`

## 출신과 구성

OmniOne의 오픈소스 `did-ca-ios`를 포크한 앱입니다. 원본의 Wallet 기능(DID 생성, PIN, 생체인증, VC 저장)을 그대로 두고 진본 화면과 API 연동을 얹었습니다.

```
source/DIDCA/
├── Controller/       진본 추가분(JinBon*, Video*) + 원본 유래 화면
├── Common/           JinBonAPIClient, Properties, KeychainHelper, SDKUtils
├── VO/               JinBonModels(진본 DTO), UserVO 등
├── Protocol/         원본 SDK 프로토콜 (IssueVc, RegUser, VerifyVc …)
├── Configuration/    Dev.xcconfig / Prod.xcconfig
└── Assets.xcassets   이미지 리소스
source/Framework/did-wallet-sdk-ios-2.0.1/DIDWalletSDK.xcframework
```

진본 화면은 코드로 UI를 구성(`buildUI()` 패턴)하고, 원본 화면은 `Main.storyboard`를 사용합니다.

## 진입 분기 (SplashViewController)

1. Wallet 잠금 상태 확인 → 필요 시 잠금 해제 또는 Wallet 생성
2. `Properties.isLoggedIn()` false → `JinBonWelcomeViewController`
3. 로그인 + DID 등록 완료 → `JinBonTabBarController`
4. 로그인 + DID 미등록 → 시작 화면으로 유도

## 백엔드 연동 (JinBonAPIClient)

`Common/JinBonAPIClient.swift`가 백엔드 호출을 전담합니다. 서버 주소는 xcconfig의 `JINBON_URL`에서 읽습니다.

| 엔드포인트 | 용도 |
|---|---|
| `POST /api/signup/did/complete` | 가입 완료 (DID 연결) |
| `POST /api/auth/did/rebind` | 앱 재설치 후 DID 재연결 |
| `POST /api/auth/refresh` | 토큰 갱신 |
| `POST /api/auth/logout` | 로그아웃 |
| `POST /api/videos` | 영상 등록 |
| `GET /api/videos` | 내 영상 목록 |
| `POST /api/videos/{id}/vc/prepare` | VC 발급 준비·재개 |
| `POST /api/videos/{id}/vc/complete` | VC 발급 완료 연결 |
| `PATCH /api/videos/{id}/deactivate` | 영상 비활성화 |
| `POST /api/verify` | 파일 검증 |
| `POST /api/verify/url` | URL 검증 |

::: info 인증 웹뷰
`/api/auth/token`, `/api/auth/app/request`, `/api/auth/app/verify`는 앱이 직접 호출하지 않습니다. 웹뷰가 로드하는 `/auth.html` 안에서 수행되고 결과만 `WKScriptMessageHandler`로 앱에 전달됩니다.
:::

## 인증 웹뷰 (AuthWebViewController)

| 모드 | 접두사 | 결과 |
|---|---|---|
| `.signup` | `/auth.html?mode=signup` → `/api/signup/*` | `signupToken` |
| `.login` | `/auth.html` → `/api/auth/*` | `accessToken`, `refreshToken`, `did` |

## Wallet DID 정합성 검사

로그인 직후 `WalletAccountValidator`가 기기 Wallet의 DID와 서버 계정 DID를 대조합니다.

| 결과 | 의미 | 앱 동작 |
|---|---|---|
| `matches` | 일치 | 메인 화면 진입 |
| `noWallet` | 기기에 Wallet 없음 | DID 재연결 안내 |
| `mismatch` | 다른 계정의 Wallet | 세션 삭제 후 오류 안내 |
| `accountDidMissing` | 서버에 DID 없음 | 세션 삭제 후 재연결 안내 |

## 로컬 저장

`UserDefaults`와 Keychain을 함께 사용합니다.

| 저장 항목 | 용도 |
|---|---|
| `accessToken` / `refreshToken` | API 인증 |
| `memberId` / `memberName` / `memberRole` | 홈·설정 화면 표시 |
| `signupToken` | 가입 중 임시 보관, 완료 후 삭제 |
| `didRebindToken` | DID 재연결 중 임시 보관 |
| `pendingVideoVc(videoId)` | VC 발급 중단 시 재개용 문맥 |

## 환경 설정

`Dev.xcconfig`는 개발 서버 IP를, `Prod.xcconfig`는 도메인 자리표시자를 담고 있습니다.

| 키 | Dev | Prod |
|---|---|---|
| `JINBON_URL` | `http://10.48.200.183:8070` | `https://jinbon.example.com` |
| `TAS_URL` | `http://10.48.200.183:8090` | `https://jinbon-tas.example.com` |
| `VERIFIER_URL` | `http://10.48.200.183:8092` | `https://jinbon-verifier.example.com` |

::: warning 프로덕션 배포 전 필수 수정
Prod 값은 아직 실제 도메인으로 교체되지 않았습니다. `Info.plist`의 `NSAllowsArbitraryLoads`도 `true`로 열려 있으므로 프로덕션 배포 전 수정이 필요합니다.
:::
