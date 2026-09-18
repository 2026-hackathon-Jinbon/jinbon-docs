# 진본 (JinBon)

> **공유하기 전, 영상의 출처를 확인하세요.**

진본은 **누가 언제 등록한 영상인지, 등록 영상과 어떻게 일치하는지 확인하는 서비스**입니다. 영상의 디지털 지문(해시)을 블록체인에 기록하고, 등록 기록과 DID 보증서(VC)를 대조합니다. 사전에 등록된 영상을 기준으로 비교하며, 등록 기록이 없다는 이유만으로 가짜 영상이라고 판단하지 않습니다.

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
