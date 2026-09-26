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

가입·로그인에는 [인증 API](/developers/api/auth)와 [회원가입 API](/developers/api/signup), 영상에는 [영상 관리 API](/developers/api/videos)와 [검증 API](/developers/api/verify)를 사용합니다. VC 발급 중에는 Holder 정보 동기화도 수행합니다.

## 인증 웹뷰 (AuthWebViewController)

본인확인 API는 웹뷰의 `/auth.html`에서 호출합니다. 앱은 `WKScriptMessageHandler`로 결과를 전달받습니다.

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

`Configuration/Dev.xcconfig`와 `Prod.xcconfig`에서 서버 주소를 관리합니다. 개발용 IP는 환경에 따라 바뀌므로 해당 파일을 기준으로 확인하세요.

| 키 | 연결 대상 |
|---|---|
| `JINBON_URL` | 진본 백엔드 |
| `TAS_URL` · `VERIFIER_URL` | Open DID TAS·Verifier |
| `CAS_URL` · `WALLET_URL` · `API_URL` | Open DID CA·Wallet·API Gateway |

::: warning 배포 전 설정
`Prod.xcconfig`의 예시 도메인을 실제 주소로 교체하고, `Info.plist`의 `NSAllowsArbitraryLoads` 설정을 확인해야 합니다.
:::
