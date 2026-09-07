# iOS 화면 기획서

`jinbon-ios`의 현재 구현 화면 명세입니다.
모든 문구는 소스 코드에 있는 그대로이며, 진본 화면은 스토리보드 없이 코드로 구성됩니다.

## 공통 디자인 요소

| 요소 | 값 |
|---|---|
| 색상 토큰 | `ColorPalette.primary`, `.ink`, `.canvas`, `.card`, `.secondaryText`, `.softBlue`, `.divider`, `.success`, `.elevatedShadow` |
| 서체 | `UIFont.jinBonFont(ofSize:weight:)` |
| 줄 간격 | `setJinBonText(_:lineSpacing:)` 확장으로 지정 |
| 카드 | 흰 배경, 코너 반경 18~22, `cornerCurve = .continuous`, 옅은 그림자 |
| 기본 버튼 | 높이 54~56, 코너 반경 13~, 채움형은 `primary` 배경 + 흰 글자 |

---

## A-01 스플래시

**클래스** `SplashViewController` · **제목** 없음

앱 실행 직후 Wallet 잠금 상태를 확인하고 진입 화면을 결정합니다.

**분기**

| 조건 | 이동 |
|---|---|
| `isLoggedIn() == false` | A-02 시작 화면 |
| 로그인 + `getRegDidDocCompleted() == true` | A-05 탭바 |
| 로그인 + DID 미완료 | A-02 시작 화면 |
| Wallet 잠김 | 잠금 해제(PIN/생체) 후 재판정 |
| Wallet 없음 | `createWallet()` 수행 |

---

## A-02 시작 화면

**클래스** `JinBonWelcomeViewController` · **배경** `ColorPalette.canvas`

세로 스크롤. 좌우 여백 24, 상단 42.

**구성** (위에서 아래로)

| 요소 | 내용 |
|---|---|
| 로고 마크 | 58×58 정사각, 코너 18, `primary` 배경, 흰 글자 `J`, 30pt Black |
| 제목 | `진짜를 증명하는\n가장 간단한 방법` — 34pt Bold, 줄간격 7 |
| 부제 | `영상의 원본 여부를 안전하게 증명하세요.` — 16pt Regular, `secondaryText` |
| 카드 1 | 회원가입 |
| 카드 2 | 로그인 |
| 텍스트 버튼 | `로그인 없이 영상 검증하기  →` — 15pt Semibold, `primary`, 높이 48 |

**액션 카드 상세**

| 카드 | 아이콘 | 제목 | 설명 | 버튼 | 버튼 스타일 |
|---|---|---|---|---|---|
| 회원가입 | `person.badge.plus` | 처음 이용하시나요? | 디지털 신원을 만들고 진본을 시작해요 | `회원가입` | 채움 (`primary`) |
| 로그인 | `person.crop.circle.badge.checkmark` | 이미 가입하셨나요? | 모바일 신분증으로 안전하게 로그인해요 | `로그인` | 연한 배경 (`primary` 9%) |

카드는 흰 배경, 코너 22, 그림자 불투명도 0.05 / 반경 18 / 오프셋 (0,7).
아이콘 28×28, 버튼 높이 50.

**접근성 식별자** `welcome.signup`, `welcome.login`, `welcome.verify`

**분기 처리** — 로그인 완료 후 Wallet DID 검사 결과에 따라

| 결과 | 화면 |
|---|---|
| `matches` | A-05 탭바로 전환 |
| `noWallet` | 알림 `디지털 신원을 다시 연결할까요?` / 본문 `이 기기에 DID가 없습니다. 새 DID를 만든 뒤 기존 진본 계정에 안전하게 연결합니다.` / 버튼 `나중에`, `다시 연결` |
| `mismatch` | 알림 `디지털 신원 연결 실패` / `이 기기의 Wallet DID가 로그인한 진본 계정의 DID와 다릅니다. 다른 계정의 Wallet을 연결할 수 없습니다.` |
| `accountDidMissing` | 알림 `디지털 신원 연결 실패` / `진본 계정에 연결된 DID가 없습니다. 디지털 신원 재연결이 필요합니다.` |

**가입 시 기기에 Wallet이 이미 있는 경우** — 알림 `기존 Wallet을 연결할까요?` /
본문 `이 기기에 이미 디지털 신원이 있습니다. 본인의 Wallet이 맞을 때만 새 진본 계정에 연결해주세요.` /
버튼 `취소`, `내 Wallet 연결`

---

## A-03 본인인증 웹뷰

**클래스** `AuthWebViewController` · **표시** 전체 화면 모달 (내비게이션 포함)

**제목** — `mode == .signup`이면 `회원가입 본인인증`, 아니면 `로그인`

`WKWebView`로 백엔드의 `/auth.html`을 로드합니다.
화면 내용은 백엔드가 제공하며 구성은 다음과 같습니다.

| 영역 | 내용 |
|---|---|
| 브랜드 헤더 | 마크 + `진본` + `CREATOR IDENTITY` |
| Eyebrow | `SECURE ID VERIFICATION` |
| 제목 | `모바일 신분증으로<br>안전하게 확인할게요` |
| 안내 카드 | `모바일 신분증 본인확인` / `정부 모바일 신분증 앱을 통해 본인 여부만 안전하게 확인합니다.` |
| 단계 표시 | `요청 준비` → `신분증 확인` → `인증 완료` |
| 상태 영역 | `role="status"`, `aria-live="polite"` |
| 기본 버튼 | `모바일 신분증 앱 열기` |
| 개인정보 안내 | `개인정보를 안전하게 보호해요.` / `확인된 정보는 회원 식별과 계정 복구 목적으로만 사용하며 공개 검증 결과에는 노출하지 않습니다.` |
| 각주 | `모바일 신분증 앱이 설치되어 있어야 이용할 수 있습니다.` |

**앱 ↔ 웹 통신** — `WKScriptMessageHandler` 세 가지

| 핸들러 | 용도 |
|---|---|
| `openDeepLink` | 신분증 앱 딥링크(iosLink) 실행 요청 |
| `authCallback` | 인증 결과 JSON 전달 |
| `authLog` | 진행 상태 로그 |

**오류** — 로드 실패 시 알림 `연결 오류`

---

## A-04 디지털 신원 생성

**클래스** `StepViewController` (원본 SDK 화면) · **표시** 전체 화면 모달

DID 생성과 DID Document 등록 진행을 안내합니다.

| 단계 타입 | 조건 |
|---|---|
| `STEP_TYPE_1` | `Properties.getUserId() == nil` |
| `STEP_TYPE_2` | 사용자 ID가 이미 있음 |

완료 후 `signupToken`으로 `POST /api/signup/did/complete`를 호출하고 탭바로 진입합니다.

---

## A-05 탭바

**클래스** `JinBonTabBarController`

| 순번 | 탭 | 아이콘 (기본 / 선택) | 루트 화면 |
|---|---|---|---|
| 0 | 홈 | `house` / `house.fill` | `JinBonHomeViewController` |
| 1 | 내 영상 | `play.rectangle.on.rectangle` / `.fill` | `VideoListViewController` |
| 2 | 보증서 | `checkmark.seal` / `checkmark.seal.fill` | `JinBonCertificateViewController` |
| 3 | 설정 | `gearshape` / `gearshape.fill` | `JinBonSettingsViewController` |

각 탭은 `UINavigationController`로 감쌉니다.
탭바 배경 `ColorPalette.card`, 그림자선 `divider`, 선택 색 `primary`, 비선택 `systemGray`.

---

## A-06 홈

**클래스** `JinBonHomeViewController` · **제목** `홈`

당겨서 새로고침 지원.

**구성**

### 헤더
| 요소 | 내용 |
|---|---|
| Eyebrow | `진본 크리에이터 월렛` |
| 제목 | `안녕하세요, {이름}님` |
| 설명 | `영상의 온체인 등록과 VC 보증서를 관리하세요.` |

### 신원 카드
| 상태 | 제목 | 부제 |
|---|---|---|
| 로그인됨 | `디지털 신원 연결됨` | `공인 등록자 · 영상 등록 가능` (role이 `ISSUER`일 때) |
| 로그인됨, 기타 역할 | `디지털 신원 연결됨` | `{role} · 등록 권한 확인 필요` |
| 미로그인 | `로그인이 필요합니다` | — |

### 등록 카드
| 요소 | 내용 |
|---|---|
| 제목 | `새 영상 온체인 등록` |
| 본문 | `영상 디지털 지문을 블록체인에 기록하고 등록 보증서를 발급받아요.` |
| 버튼 | `영상 등록하기` → A-10 |

### 최근 등록 섹션
| 상태 | 표시 |
|---|---|
| 목록 있음 | 요약 `총 {n}건` + 영상 행 목록 |
| 비어 있음 (로그인) | `아직 등록한 영상이 없습니다.` |
| 비어 있음 (미로그인) | `로그인 후 등록 현황을 확인할 수 있습니다.` |
| 오류 | `최근 등록을 불러오지 못했습니다\n{메시지}` + `다시 시도` 버튼 |

**영상 행** — 제목 / 등록일(`YYYY-MM-DD`, 없으면 `등록일 확인 중`) / 배지

| `active` | 배지 |
|---|---|
| `true` 또는 미지정 | `인증 유효` |
| `false` | `취소` |

### 검증 도구 카드
| 요소 | 내용 |
|---|---|
| 제목 | `영상 검증 도구` |
| 설명 | `영상 일치·온체인 등록·VC 보증서 확인` |
| 동작 | 탭 시 A-13 |

**호출 API** `GET /api/videos`

---

## A-07 내 영상

**클래스** `VideoListViewController` · **제목** `내 영상` · **셀** `VideoTableViewCell`

당겨서 새로고침 지원.

**내비게이션 바**

| 로그인 상태 | 좌측 | 우측 |
|---|---|---|
| 로그인 | 없음 | 업로드 버튼 |
| 미로그인 | 없음 | 없음 |

**미로그인 화면**

| 요소 | 내용 |
|---|---|
| 제목 | `로그인하고 내 영상을 관리하세요` |
| 버튼 | 로그인 (흰 글자 채움), 회원가입 |

**상태별 표시** (`ContentState`)

| 상태 | 내용 |
|---|---|
| `hidden` | 목록 표시 |
| `loading` | `영상 목록을 불러오는 중입니다` |
| `empty` | `아직 등록한 영상이 없습니다\n홈에서 첫 영상의 디지털 지문을 등록해 보세요.` |
| `error` | 오류 메시지 + `다시 시도` 버튼 |

**셀 구성** — 높이 고정

| 요소 | 내용 |
|---|---|
| 제목 | `video.title` |
| 상태 배지 | 활성 `✓ 등록 유효` / 비활성 `! 비활성` |
| 날짜 | `YYYY-MM-DD · 등록됨` 또는 `YYYY-MM-DD · 비활성화됨` (날짜 없으면 `등록됨` / `비활성화됨`) |

**셀 선택 시** — 영상 정보 알림(`UIAlertController`)이 뜨고
등록 정보와 함께 다음 동작을 제공합니다.

| 동작 | 조건 |
|---|---|
| 영상 재생 | 로컬에 저장된 파일이 있을 때 |
| 보증서 발급 | VC 미발급 상태일 때 (`POST /api/videos/{id}/vc/prepare`) |
| 비활성화 | 활성 상태일 때 |

**비활성화 흐름** — 확인 알림 → 진행 알림 → 완료 또는 실패 알림

**로그아웃** — 알림 `로그아웃` / `로그아웃 하시겠습니까?`

**호출 API** `GET /api/videos`, `POST /api/videos/{id}/vc/prepare`, `PATCH /api/videos/{id}/deactivate`

---

## A-08 등록 보증서 목록

**클래스** `JinBonCertificateViewController` · **제목** `등록 보증서` · **셀 높이** 176

Wallet에 저장된 VC 중 진본이 발급한 것만 걸러 표시합니다(`isJinBonCredential`).
당겨서 새로고침 지원.

**상태별 표시**

| 상태 | 제목 | 설명 |
|---|---|---|
| 미로그인 | `로그인이 필요합니다` | `로그인하면 진본이 발급한 등록 보증서를\n이 Wallet에서 확인할 수 있어요.` |
| 비어 있음 | `아직 발급된 등록 보증서가 없습니다` | `영상의 디지털 지문을 등록하면\n온체인 등록 보증서를 Wallet에 받을 수 있어요.` |
| 오류 | `보증서를 불러오지 못했습니다` | 오류 메시지 + `다시 시도` |

**셀 구성** (`JinBonCertificateCell`)

| 요소 | 내용 |
|---|---|
| 마크 | `J` |
| 배지 | `VERIFIABLE CREDENTIAL` |
| 제목 | `영상 블록체인 등록 보증서` |
| ID | `credential.id` |
| 발급일 | `발급일  {변환된 날짜}` |

---

## A-09 설정

**클래스** `JinBonSettingsViewController` · **제목** `설정`

**프로필 카드**

| 요소 | 내용 |
|---|---|
| 아바타 | 이름 첫 글자 (없으면 `진`) |
| 이름 | `Properties.getMemberName()` 또는 `로그인이 필요합니다` |
| 역할 | `ISSUER`면 `공인 등록자`, 아니면 role 값 또는 `비회원` |

**메뉴 (로그인 상태)**

| 섹션 | 항목 | 설명 |
|---|---|---|
| 디지털 신원 및 보안 | 내 디지털 신원 | DID와 연결 상태 확인 |
| | Wallet 보안 | PIN 및 생체인증 관리 |
| | 인증서 관리 | 발급·폐기 상태 확인 (탭 2로 이동) |
| 계정 | 로그아웃 | 모바일 신분증으로 다시 로그인 (강조 스타일) |
| 앱 정보 | 오픈소스 라이선스 | 사용한 오픈소스와 저작권 정보 |

**메뉴 (미로그인 상태)**

| 섹션 | 항목 | 설명 |
|---|---|---|
| 비회원 이용 | 영상 검증 | 로그인 없이 진본 여부 확인 |
| | 회원가입·로그인 화면 | 진본 시작 화면으로 이동 |
| 앱 정보 | 오픈소스 라이선스 | 사용한 오픈소스와 저작권 정보 |

**하단** — `진본 Wallet {version} ({build})`

**로그아웃 알림** — 제목 `로그아웃할까요?` / 본문 `Wallet과 인증서는 이 기기에 안전하게 유지됩니다.`

**접근성 식별자** `settings.menu.{항목명}`

---

## A-10 영상 온체인 등록

**클래스** `VideoUploadViewController` · **제목** `영상 온체인 등록`

세로 스크롤, 좌우 여백 20, 상단 24. 키보드 대응 포함.

**헤더**

| 요소 | 내용 | 스타일 |
|---|---|---|
| Eyebrow | `온체인 등록` | 12pt Bold, `primary` |
| 제목 | `영상 디지털 지문을 등록하세요` | 28pt Bold, 줄간격 7 |
| 설명 | `영상 해시를 블록체인에 기록해요.` | 15pt Regular, `secondaryText` |

**STEP 1 — 등록할 영상 선택**

섹션 헤더: 배지 `1` / 제목 `등록할 영상 선택` / 캡션 `MP4, MOV 등 갤러리의 영상 파일`

선택 영역: 높이 210, `softBlue` 배경, 코너 22, `primary` 22% 테두리

| 상태 | 표시 |
|---|---|
| 미선택 | 중앙 아이콘 `video.badge.plus` (56×56, `primary` 배경, 흰색) + `탭하여 영상 선택` |
| 선택됨 | 썸네일 채움 + 하단 파일명 배지 (검정 62% 배경, 높이 34) |

영상 선택은 `PHPickerViewController`를 사용합니다.

**STEP 2 — 영상 정보**

섹션 헤더: 배지 `2` / 제목 `영상 정보` / 캡션 `내 영상에서 쉽게 구분할 이름`

| 요소 | 내용 |
|---|---|
| 라벨 | `제목` (13pt Bold, `secondaryText`) |
| 입력 | 플레이스홀더 `영상 제목을 입력하세요`, 17pt Semibold, 높이 42, 편집 중 클리어 버튼, 리턴키 `Done` |

**안내 카드** — `영상 원문은 저장하지 않고 디지털 지문만 블록체인에 등록해요.`

**등록 버튼**

| 상태 | 문구 |
|---|---|
| 기본 | `영상 디지털 지문 등록하기` (아이콘 `checkmark.shield.fill`, 높이 56) |
| 진행 중 | `블록체인에 등록 중...` |
| 완료 후 | `영상 디지털 지문 등록하기`로 복귀 |

**유효성 검사** — 제목이 비어 있으면 알림으로 안내하고 입력란으로 스크롤

**결과 뷰** (화면 하단, 등록 성공 시 노출)

| 요소 | 내용 |
|---|---|
| 아이콘 | `checkmark.shield.fill`, `success` 색 |
| VC 상태 배지 | 발급됨 `  등록 보증서 발급 완료  ` / 대기 `  등록 보증서 발급 대기  ` |
| 상세 | 등록 정보 + `VC ID     {vcId}` (모노스페이스 11pt) |

**호출 API** `POST /api/videos`, `POST /api/videos/{id}/vc/prepare`, `POST /api/videos/{id}/vc/complete`

---

## A-11 등록 완료

**클래스** `VideoRegistrationCompletionViewController` · **제목** `등록 완료`

뒤로 가기 버튼 숨김, 우측 상단 `닫기`.

| 요소 | 내용 |
|---|---|
| 아이콘 | `checkmark.shield.fill`, 76×76 원형 배경(`success` 12%) |
| 제목 | 신규 `블록체인 등록 완료` / 기존 확인 `기존 등록을 확인했어요` (26pt Bold, 가운데) |
| 설명 | `영상 디지털 지문과 등록자 DID가 블록체인에 기록됐어요.` |
| 상세 카드 | `영상` = 제목(없으면 `제목 없음`), `등록일` = `YYYY-MM-DD`(없으면 `방금`) |
| 보증서 섹션 | 제목 `영상 블록체인 등록 보증서` + 상태 아이콘·문구 |
| 기본 버튼 | `등록 보증서 발급하기` (높이 56) |
| 보조 버튼 | `내 영상으로 돌아가기` (높이 54) |

보증서 상태 아이콘은 발급 완료 시 `checkmark.circle.fill`, 미발급 시 `circle.dashed`입니다.

---

## A-12 보증서 발급 확인 팝업

**클래스** `JinBonVcOfferViewController` · **표시** 중앙 카드 모달 (좌우 여백 24)

| 요소 | 내용 |
|---|---|
| 아이콘 | `checkmark.seal.fill`, 56×56 원형 배경 |
| 브랜드 | `JINBON WALLET` (12pt Bold, `primary`) |
| 제목 | `등록 보증서를 발급할까요?` (22pt Bold, 가운데) |
| 본문 | `진본 Issuer가 영상 디지털 지문의 온체인 등록 사실과 등록 주체를 확인한 VC 보증서를 발급합니다.` |
| 버튼 1 | `나중에` (테두리형, 높이 52) |
| 버튼 2 | `등록 보증서 발급하기` (채움, 높이 54) |

`나중에`를 선택해도 등록은 유지되며, 내 영상 목록에서 다시 발급할 수 있습니다.

---

## A-13 영상 검증

**클래스** `VideoVerifyViewController` · **제목** `영상 검증`

`showsCloseButton`이 `true`면 좌측 상단에 닫기 버튼이 생깁니다(비회원 진입 시).

**안내 문구** (가운데 정렬, 줄간격 7)

```
공식 등록 영상과 비교하세요        ← 19pt Bold, ink
갤러리에서 영상 하나를 선택하면 돼요.   ← 15pt, secondaryText
```

**영상 선택 영역** — A-10과 동일한 스타일(`softBlue`, 코너 22, `탭하여 영상 선택`)

**검증 버튼**

| 상태 | 문구 |
|---|---|
| 기본 | `영상 검증하기` |
| 결과 표시 후 | `다시 검증` |
| 비활성 | 투명도 0.55 |

**결과 카드**

테두리 색은 판정 색상의 28%, 그림자 불투명도 0.08.
`accessibilityLabel`은 `검증 결과, {제목}`이고 결과 표시 시 음성 안내가 나갑니다.

판정별 제목·아이콘·색상:

| verdict | 제목 | 아이콘 | 색상 |
|---|---|---|---|
| `EXACT_MATCH` | 등록 영상과 정확히 일치합니다 | `checkmark.seal.fill` | systemGreen |
| `SAME_CONTENT` | 등록된 영상과 내용이 일치합니다 | `checkmark.circle.fill` | `primary` |
| `SIMILAR_MATCH` | 등록 영상과 유사합니다 | `equal.circle.fill` | systemBlue |
| `REGISTERED_BUT_REVOKED` | 비활성화된 등록 영상입니다 | `exclamationmark.shield.fill` | systemOrange |
| `CERTIFICATE_INVALID` | 등록은 확인됐지만 보증서가 유효하지 않습니다 | `xmark.shield.fill` | systemOrange |
| `NOT_REGISTERED` | 등록 기록을 찾지 못했습니다 | `questionmark.circle.fill` | systemGray |
| `VERIFICATION_UNAVAILABLE` | 현재 검증할 수 없습니다 | `exclamationmark.triangle.fill` | systemOrange |

**상세 행** (항상 3줄)

| 라벨 | 값 |
|---|---|
| 영상 디지털 지문 | 아래 표 참고 |
| 블록체인 등록 | `확인됨` / `확인되지 않음` |
| 진본 VC 보증서 | 아래 표 참고 |

영상 디지털 지문 값:

| verdict | 값 |
|---|---|
| `EXACT_MATCH` | 정확히 일치 |
| `SAME_CONTENT` | 동일 콘텐츠 |
| `SIMILAR_MATCH` | 유사 콘텐츠 |
| `REGISTERED_BUT_REVOKED`, `CERTIFICATE_INVALID` | 등록 영상과 일치 |
| `NOT_REGISTERED` | 등록 기록 없음 |
| `VERIFICATION_UNAVAILABLE` | 확인 불가 |

진본 VC 보증서 값:

| 조건 | 값 |
|---|---|
| `vcVerified == true` | 유효 |
| `verdict == CERTIFICATE_INVALID` | 유효하지 않음 |
| `videoId == nil` | 해당 없음 |
| 그 외 | 미발급 또는 미확인 |

**조건부 행**

| 행 | 조건 |
|---|---|
| 서버 메시지 콜아웃 | `message`가 있을 때 (판정 색 8% 배경, 15pt Semibold) |
| 등록일 | `registeredAt`이 있을 때 (`YYYY-MM-DD`) |
| 유사도 거리 | `SIMILAR_MATCH`이고 값이 있을 때 (소수점 1자리) |
| 주의 콜아웃 | `notice`가 있을 때 (`canvas` 배경, 13pt Medium) |

**호출 API** `POST /api/verify`

---

## A-14 등록 보증서 상세

**클래스** `JinBonCertificateDetailViewController` · **제목** `등록 보증서 상세`

**히어로 카드** (`ink` 배경)

| 요소 | 내용 |
|---|---|
| 제목 | `영상 블록체인 등록 보증서` |
| 설명 | `JinBon Verifiable Credential` |
| 상태 배지 | 초기 `상태 확인 중` |

상태 조회 결과:

| 상태 | 표시 |
|---|---|
| `ACTIVE` | `  유효한 보증서  ` |
| `INACTIVE` | `  비활성 보증서  ` |
| `REVOKED` | `  폐기됨  ` |
| 기타 | `  알 수 없는 상태  ` |
| 조회 실패 | `  상태 확인 불가  ` |

**클레임 카드** — 섹션 제목 `진본이 보증하는 내용`

VC의 클레임을 순서대로 나열하며, 각 행 사이에 1px 구분선을 넣습니다.
값이 비어 있으면 `정보 없음`으로 표시합니다.

클레임 캡션은 한국어로 변환합니다.

| 클레임 ID | 표시명 |
|---|---|
| `credentialType` | 보증서 종류 |
| `assuranceType` | 보증 범위 |
| `videoCommitment` | 영상 디지털 지문 |
| `registrantDid` | 등록자 DID |
| `blockchainNetwork` | 블록체인 네트워크 |
| `chainId` | 체인 ID |
| `contractAddress` | 컨트랙트 주소 |
| `transactionHash` | 트랜잭션 해시 |
| `blockNumber` | 블록 번호 |
| `registeredAt` | 온체인 등록 시각 |
| `videoTitle` | 영상 제목 |
| `schemaVersion` | 보증서 스키마 버전 |
| `videoHash` | 영상 해시 (구버전) |
| `uploaderDid` | 등록자 DID (구버전) |
| `uploadTimestamp` | 등록 시각 (구버전) |

매핑에 없는 캡션은 원문 그대로 노출합니다.

**메타데이터 카드** (`softBlue` 배경, 모노스페이스 11pt)

```
발급기관
{issuer.name 또는 진본} · {issuer.id}

VC ID
{credential.id}

발급일
{변환된 발급일}
```

**하단 고지**

> 이 보증서는 영상 디지털 지문의 블록체인 등록 사실과 등록 주체를 진본이 확인했다는 뜻입니다. 영상 내용의 사실성이나 법적 저작권은 보증하지 않습니다.

---

## A-15 오픈소스 라이선스

**클래스** `OpenSourceLicensesViewController` · **제목** `오픈소스 라이선스`

| 영역 | 내용 |
|---|---|
| 인트로 카드 | Eyebrow `OPEN SOURCE` + 제목 `함께 만든 기술을\n투명하게 공개합니다` + 설명 |
| 구성요소 카드 | 이름, 설명, 저작권, 라이선스 배지 |
| 문서 카드 | 고지 문서 및 Apache License 열람 |
| 각주 | 하단 안내 문구 |

## A-16 문서 뷰어

**클래스** `LicenseDocumentViewController`

제목은 열람 중인 문서명이며, 본문은 `UITextView`로 표시합니다.
번들 리소스를 읽지 못하면 대체 텍스트를 보여줍니다.

---

## 공통 팝업

원본 SDK의 팝업 스토리보드를 그대로 사용합니다.

| 화면 | 식별자 |
|---|---|
| 오류 다이얼로그 | `ErrorDialogViewController` |
| 확인 1버튼 | `OneButtonDialogViewController` |
| 확인 2버튼 | `TwoButtonDialogViewController` |
| 입력 팝업 | `InputPopUpViewController` |
| 로딩 | `ActivityIndicatorViewController` |
| PIN 입력 | `PincodeViewController` (PIN.storyboard) |

진본 화면 대부분은 이들 대신 `UIAlertController`를 직접 사용합니다.
