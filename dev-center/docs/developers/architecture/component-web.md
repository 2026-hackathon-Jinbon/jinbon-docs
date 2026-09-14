# 웹 구조

저장소: `jinbon-web` · 목적: 로그인 없이 영상 파일을 올려 진본 여부 확인

## 파일 구성

```
app/
  layout.tsx     메타데이터와 공통 레이아웃
  page.tsx       검증 화면 전체 (단일 컴포넌트)
  globals.css    디자인 시스템과 반응형 스타일
worker/
  index.ts       Cloudflare Workers 엔트리
public/          정적 파일
```

화면은 `app/page.tsx`의 `Home` 하나뿐입니다. `"use client"` 지시자가 붙어 전체가 클라이언트 컴포넌트로 동작합니다.

## 실행 스택

| 항목 | 값 |
|---|---|
| 프레임워크 | Next.js 16.2.6 (App Router) |
| 런타임 | React 19.2.6 |
| 배포 대상 | Cloudflare Workers |
| 스타일 | Tailwind CSS 4.2.1 |

```bash
cp .env.example .env.local
npm install
npm run dev     # http://localhost:8071
```

## 상태 관리

외부 상태 라이브러리 없이 `useState` 6개와 `useMemo` 1개로 동작합니다.

| 상태 | 용도 |
|---|---|
| `file` | 선택된 영상 파일 |
| `previewUrl` | 미리보기 주소 |
| `isDragging` | 드래그 오버 시각 효과 |
| `isVerifying` | 검증 요청 진행 중 |
| `error` | 오류 문구 |
| `result` | 백엔드 검증 응답 |
| `resultTone` | 결과 톤 (`authentic` / `unknown` / `warning` / `neutral`) |

## 백엔드 호출

```ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8070";

const formData = new FormData();
formData.append("file", file);
await fetch(`${API_BASE_URL}/api/verify`, { method: "POST", body: formData });
```

파일 업로드 검증만 사용합니다. URL 검증은 웹에서 쓰지 않습니다.

## 클라이언트 측 검사

| 조건 | 오류 문구 |
|---|---|
| `type`이 `video/`로 시작하지 않음 | 영상 파일만 선택할 수 있습니다. |
| 크기가 100MB 초과 | 파일 크기는 최대 100MB까지 가능합니다. |

## 결과 톤 계산

```ts
if (!result) return "neutral";
if (result.authentic && result.active) return "authentic";
if (result.verdict === "NOT_REGISTERED") return "unknown";
return "warning";
```

톤에 따라 색과 문구, 도장 아이콘이 달라집니다.

::: warning verdict 타입 불일치
`page.tsx`의 `VerificationVerdict` 유니언에 `AUTHENTIC_EXACT`, `AUTHENTIC_SIMILAR`가 남아 있지만 백엔드는 `EXACT_MATCH`, `SAME_CONTENT` 등을 반환합니다. `| string`이 있어 깨지지는 않지만, `CERTIFICATE_INVALID` 같은 상태가 `warning` 하나로 뭉뚱그려집니다.
:::
