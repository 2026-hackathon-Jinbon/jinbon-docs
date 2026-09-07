# 웹 구조

저장소: `jinbon-web` · 목적: 로그인 없이 영상 파일을 올려 진본 여부를 확인

## 파일 구성

```
app/
  layout.tsx     메타데이터와 공통 레이아웃
  page.tsx       검증 화면 전체 (단일 컴포넌트)
  globals.css    디자인 시스템과 반응형 스타일
worker/
  index.ts       Cloudflare Workers 엔트리
tests/
  rendered-html.test.mjs   빌드 결과 HTML 렌더링 검사
public/          정적 파일
```

화면은 `app/page.tsx`의 기본 export `Home` 하나뿐입니다.
`"use client"` 지시자가 붙어 있어 전체가 클라이언트 컴포넌트로 동작합니다.

## 실행 스택

| 항목 | 값 |
|---|---|
| 프레임워크 | Next.js 16.2.6 (App Router) |
| 런타임 | React 19.2.6 |
| 번들러 | `vinext` 0.0.50 (Vite 8 기반) |
| 배포 대상 | Cloudflare Workers (`wrangler` 4.92.0) |
| 스타일 | Tailwind CSS 4.2.1 + `globals.css` |
| Node | 22.13.0 이상 |

```bash
cp .env.example .env.local
npm install
npm run dev     # http://localhost:8071
npm run test    # build 후 렌더링 테스트
npm run lint
```

## 상태 관리

외부 상태 라이브러리 없이 `useState` 6개와 `useMemo` 1개로 화면 전체를 다룹니다.

| 상태 | 용도 |
|---|---|
| `file` | 선택된 영상 파일 |
| `previewUrl` | `URL.createObjectURL`로 만든 미리보기 주소 |
| `isDragging` | 드래그 오버 시각 효과 |
| `isVerifying` | 검증 요청 진행 중 |
| `error` | 사용자에게 보여줄 오류 문구 |
| `result` | 백엔드 검증 응답 |
| `resultTone` (`useMemo`) | 결과 톤 (`authentic` / `unknown` / `warning` / `neutral`) |

`previewUrl`은 `useEffect` 정리 함수에서 `revokeObjectURL`로 해제합니다.

## 백엔드 호출

```ts
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8070";

const formData = new FormData();
formData.append("file", file);
await fetch(`${API_BASE_URL}/api/verify`, { method: "POST", body: formData });
```

- 엔드포인트는 파일 업로드 검증 하나만 사용합니다. URL 검증은 웹에서 쓰지 않습니다.
- 응답의 `data`가 없으면 `payload.message`를 오류로 띄웁니다.
- `Failed to fetch`는 "검증 서버에 연결할 수 없습니다. 백엔드가 8070 포트에서 실행 중인지 확인해 주세요."로 치환합니다.

## 클라이언트 측 검사

서버로 보내기 전에 두 가지를 먼저 확인합니다.

| 조건 | 오류 문구 |
|---|---|
| `type`이 `video/`로 시작하지 않음 | 영상 파일만 선택할 수 있습니다. |
| 크기가 100MB 초과 | 파일 크기는 최대 100MB까지 가능합니다. |

100MB 제한은 백엔드의 `spring.servlet.multipart.max-file-size`와 같은 값입니다.

## 결과 톤 계산

```ts
if (!result) return "neutral";
if (result.authentic && result.active) return "authentic";
if (result.verdict === "NOT_REGISTERED") return "unknown";
return "warning";
```

톤에 따라 결과 패널의 색과 문구, 도장 아이콘(`✓` / `?` / `!`)이 달라집니다.

## 타입 정의와 실제 응답의 차이

`page.tsx`의 `VerificationVerdict` 유니언 타입은 다음과 같이 선언되어 있습니다.

```ts
type VerificationVerdict =
  | "AUTHENTIC_EXACT"
  | "AUTHENTIC_SIMILAR"
  | "REGISTERED_BUT_REVOKED"
  | "NOT_REGISTERED"
  | string;
```

백엔드가 실제로 반환하는 값은 `EXACT_MATCH`, `SAME_CONTENT`, `SIMILAR_MATCH`,
`REGISTERED_BUT_REVOKED`, `CERTIFICATE_INVALID`, `NOT_REGISTERED`, `VERIFICATION_UNAVAILABLE`입니다.
`AUTHENTIC_EXACT`와 `AUTHENTIC_SIMILAR`는 더 이상 나오지 않는 구버전 값입니다.

유니언 끝에 `| string`이 있어 타입 오류는 나지 않고, 화면 분기도 `authentic`·`active`·
`NOT_REGISTERED`만 보므로 **표시 자체는 깨지지 않습니다**. 다만 `CERTIFICATE_INVALID`처럼
구분해 보여줘야 할 상태가 `warning` 하나로 뭉뚱그려집니다.
자세한 내용은 [알려진 이슈](../90-status/open-issues.md)를 참고합니다.

## 개인정보 처리

업로드한 영상은 백엔드가 해시만 계산하고 저장하지 않습니다.
화면에도 "영상 원본은 서버에 저장되지 않습니다."라는 문구를 검증 버튼 옆에 노출합니다.
