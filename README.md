# 진본 (JinBon)

> **등록 영상과의 일치, 등록자와 등록 시점을 확인합니다.**

진본은 영상의 디지털 지문(해시)을 블록체인에 기록하고, 누가 언제 등록했는지를 DID 보증서(VC)로 증명하는 **영상 진위 검증 서비스**입니다. 원본 영상은 서버에 저장하지 않으며, 해시만 계산한 뒤 즉시 삭제합니다.

**자세한 내용은 [진본 홈페이지](https://jinbon-docs.vercel.app)를 확인하세요.**

## 저장소 구조

| 저장소 | 역할 | 기술 스택 |
|---|---|---|
| **jinbon-backend** | 등록, 검증, 인증 API 허브 | Java 21, Spring Boot, PostgreSQL, Redis |
| **jinbon-ios** | 등록자용 Wallet 앱 | Swift, UIKit, DIDWalletSDK |
| **jinbon-web** | 파일 업로드 영상 검증 | Next.js 16, React 19, Tailwind CSS |
| **jinbon-extension** | YouTube·Instagram 즉시 검증 | Manifest V3, JavaScript |

## 문서

이 저장소(`jinbon-docs`)는 진본의 기술 문서와 시각 자료를 관리합니다.

- **[홈페이지](https://jinbon-docs.vercel.app)** — 제품 소개, 사용 사례, 개발자 센터
- **[시각 자료](visual/01-service-at-a-glance.md)** — 서비스 흐름 다이어그램
- **발표자료/** — 해커톤 제안서 (예선·결선)
