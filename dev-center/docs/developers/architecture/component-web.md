# 웹 구조

저장소: `jinbon-web` · 목적: 로그인 없이 파일 또는 영상 URL로 등록 기록과 비교 결과 확인

## 파일 구성

```text
app/
  layout.tsx     메타데이터와 공통 레이아웃
  page.tsx       파일·URL 입력과 검증 결과 화면
  globals.css    디자인 시스템과 반응형 스타일
worker/
  index.ts       Cloudflare Workers 엔트리
public/          정적 파일
```

`app/page.tsx`는 클라이언트 컴포넌트입니다. 파일과 URL 입력 모드를 전환하고, 검증 요청의 진행 상태와 결과를 표시합니다.

## 실행 스택

| 항목 | 값 |
|---|---|
| 프레임워크 | Next.js 16.2.6 / React 19.2.6 |
| 실행·빌드 | vinext / Vite |
| 배포 구성 | Cloudflare Workers |
| 스타일 | Tailwind CSS 4.2.1 |

```bash
cp .env.example .env.local
npm install
npm run dev     # http://localhost:8071
```

## 입력과 상태 관리

컴포넌트 내부에서 입력 모드, 선택한 파일, URL, 미리보기 주소, 드래그 상태, 요청 진행 상태, 오류와 검증 결과를 관리합니다.

| 입력 | 검사·처리 |
|---|---|
| 파일 | 영상 MIME 유형과 최대 100MB 크기를 확인하고 `multipart/form-data`로 전송 |
| URL | URL 형식과 지원 플랫폼 등을 확인하고 JSON으로 전송 |

지원 플랫폼과 입력 방식의 차이는 [URL·파일 검증 차이](/developers/guide/verification-methods)를 참고하세요.

## 백엔드 호출

`NEXT_PUBLIC_API_BASE_URL`로 검증 API 주소를 지정합니다.

```ts
// 파일 검증
const formData = new FormData();
formData.append("file", file);
await fetch(`${API_BASE_URL}/api/verify`, {
  method: "POST",
  body: formData,
});

// URL 검증
await fetch(`${API_BASE_URL}/api/verify/url`, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ url }),
});
```

요청·응답 형식과 제한은 [검증 API](/developers/api/verify)에 정리되어 있습니다.

## 결과 표시 {#result-display}

`displayStatus`로 기본 결과를 구분하고 `verdict`로 확인 방식과 세부 문구를 결정합니다.

현재 `app/page.tsx`는 아래 순서로 제목을 결정합니다.

| 조건 | 제목 |
|---|---|
| `displayStatus=AUTHENTICATED` | 진본 확인 |
| `verdict=NOT_REGISTERED` | 등록 기록 없음 |
| 콘텐츠 유사 결과이며 영상·음성 비교 정보가 모두 있고, 어느 한쪽에 불일치 구간이 있음 | 원본 불일치 |
| 그 외 | 확인 불가 |

`UNAVAILABLE`은 별도 색상으로 표시합니다. 비교 정보가 부족한 경우에도 ‘확인 불가’가 나올 수 있으므로 제목과 서버의 상세 메시지를 함께 읽어야 합니다.

확인 방식은 `EXACT_MATCH`일 때 “원본 파일 정확 일치”, `SIMILAR_MATCH` 또는 레거시 `SAME_CONTENT`일 때 “영상·음성 비교”로 표시합니다. 두 방식의 확인 범위는 다릅니다.

등록 시점과 등록자 표시명, 블록체인·보증서 확인 결과, 서버가 반환한 상세 안내를 함께 표시합니다. 표시명은 기관 소속·직함의 인증을 뜻하지 않습니다. 자세한 응답은 [검증 API](/developers/api/verify)를 참고하세요.
