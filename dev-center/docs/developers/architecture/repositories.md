# 저장소 구조

수정하려는 기능에 따라 다음 저장소에서 시작하면 됩니다. 전체 연결 관계는 [시스템 구성](/developers/architecture/overview)을 참고하세요.

| 저장소 | 주요 코드 위치 | 담당 기능 |
|---|---|---|
| [jinbon-backend](/developers/architecture/component-backend) | `src/main/java/com/jinbon/` | 인증, 영상 등록·검증 API, 챗봇, 외부 연동 |
| [jinbon-ios](/developers/architecture/component-ios) | `source/DIDCA/` | 본인확인, DID·Wallet, 영상 등록, 보증서 보관 |
| [jinbon-web](/developers/architecture/component-web) | `app/page.tsx` | 파일·URL 입력, 검증 결과 화면 |
| [jinbon-extension](/developers/architecture/component-extension) | `src/content.js`, `src/background.js` | YouTube·Instagram 검증 버튼, URL 검증 요청 |
| `jinbon-docs` | `dev-center/docs/` | 서비스 소개, 개발자 문서 |

## 백엔드에서 기능 찾기

| 작업 | 패키지 |
|---|---|
| 가입·로그인·토큰 | `domain/auth` |
| 회원·등록자 표시명 | `domain/member` |
| 등록·중복 확인·지문 비교·판정 | `domain/video` |
| 블록체인 호출 | `infra/blockchain` |
| 보증서 발급·검증 | `infra/opendid` |
| URL 영상 다운로드 | `infra/download` |
| 공통 응답·예외·보안 설정 | `global` |
