# 백엔드 구조

저장소: `jinbon-backend` · 패키지 루트: `com.jinbon`

## 패키지 구성

```text
src/main/java/com/jinbon/
├── domain/
│   ├── auth/         가입·로그인·JWT·CI 해시
│   ├── member/       회원·등록자 표시명
│   ├── video/        등록·검증·지문 비교
│   └── kakao/        챗봇 요청·콜백
├── global/
│   ├── common/       공통 응답
│   ├── config/       보안·외부 연동 설정
│   └── error/        에러 코드·예외 처리
└── infra/
    ├── blockchain/   블록체인 호출
    ├── download/     URL 영상 다운로드
    ├── omnione/      모바일 신분증 검증
    ├── opendid/      보증서 발급·검증
    └── redis/        검증 캐시·인증 토큰 저장
```

인증·영상 API는 `XxxApi` 인터페이스에 Swagger 정의를, `XxxController`에 요청 처리를 둡니다. `domain/*/port`는 외부 연동에 필요한 인터페이스를 정의하고 `infra`가 이를 구현합니다.

## 핵심 서비스

| 서비스 | 책임 | 동작 상세 |
|---|---|---|
| `VideoRegisterService` | 중복 확인, DB·블록체인 등록, VC 발급 준비 | [영상 등록](/developers/flows/video-register) |
| `VideoVerifyService` | 파일·URL 입력, 캐시, 등록 증거 확인, 최종 판정 | [영상 검증](/developers/flows/video-verify) |
| `MediaFingerprintService` | 파일·URL 공통 지문 생성 | [지문 종류](/developers/guide/concepts) |
| `VideoContentMatchService` | 등록 후보 선택, 영상·음성 구간 비교 | [비교 기준](/developers/flows/video-verify#match-criteria) |
| `PerceptualHashService` | 대표 화면의 DCT 지각해시 | [후보 검색](/developers/flows/video-verify#candidate-search) |
| `HashService` · `SignatureService` | 파일 해시, 등록 대표값, 서버 HMAC 계산 | [등록 증거](/developers/flows/video-verify#registration-evidence) |

## 구현 시 알아둘 점

- **등록 순서:** `saveAndFlush()`로 파일 해시의 unique 제약을 확인한 뒤 블록체인에 전송합니다. 동시 요청의 중복 트랜잭션을 방지하기 위한 순서입니다.
- **후보 검색 비용:** `findByActiveTrue()`로 활성 영상 전체를 메모리에 올려 비교합니다. 현재 별도 검색 인덱스는 없습니다.
- **대표 화면 지문:** JavaCV의 `FFmpegFrameGrabber`로 프레임을 추출하고, 32×32 DCT의 8×8 저주파 영역으로 64비트 해시를 만듭니다.
- **파일 해시:** `generateFineHash(InputStream)`이 8KB 버퍼로 스트리밍 SHA-256을 계산합니다.
- **서명 키:** 영상 HMAC에 JWT secret을 함께 씁니다. 키 변경 영향은 [보안 문서](/developers/security/overview)를 참고하세요.

HTTP 응답과 인증 방식은 [공통 규약](/developers/api/conventions), 입력 제한은 [검증 API](/developers/api/verify#input-limits)에서 확인할 수 있습니다.
