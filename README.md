# 진본 (JinBon)

> **공유하기 전, 영상의 출처를 확인하세요.**

진본은 **누가 언제 등록한 영상인지, 등록 영상과 어떻게 일치하는지 확인하는 서비스**입니다. 파일이 정확히 같은지 먼저 확인하고, 파일이 다르면 영상·음성 지문을 비교합니다. 블록체인 등록 기록과 DID 기반 디지털 보증서(VC)도 함께 확인합니다.

현재 영상 등록·검증 흐름을 시연하는 데모입니다. 사전에 등록된 영상을 기준으로 비교하며, 등록 기록이 없다는 이유만으로 가짜 영상이라고 판단하지 않습니다. 등록 영상과의 일치가 영상 내용의 사실성이나 AI 생성 여부를 보증하지는 않습니다.

[홈페이지](https://jinbon-docs.vercel.app) · [영상 검증 웹](https://jinbon-web.vercel.app) · [등록·이용 안내](https://jinbon-docs.vercel.app/downloads) · [개발자 센터](https://jinbon-docs.vercel.app/developers/guide/introduction)

## 구성 저장소

| 저장소 | 역할 | 기술 스택 |
|---|---|---|
| **jinbon-backend** | 등록·검증·인증 API, 카카오톡 챗봇 연동 | Java 21, Spring Boot, PostgreSQL, Redis |
| **jinbon-ios** | 본인확인, DID·Wallet, 영상 등록·파일 검증, 보증서 보관 | Swift, UIKit, DIDWalletSDK |
| **jinbon-web** | 로그인 없이 파일·URL로 영상 검증 | Next.js 16, React 19, vinext / Vite, Tailwind CSS |
| **jinbon-extension** | YouTube·Instagram 페이지에서 URL 검증 요청 | Manifest V3, JavaScript |
| **jinbon-docs** | 홈페이지, 개발자 문서, 발표·시연 자료 | VitePress, Vue, Mermaid |
