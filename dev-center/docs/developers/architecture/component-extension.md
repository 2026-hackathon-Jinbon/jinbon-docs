# Chrome 확장 프로그램 구조

저장소: `jinbon-extension` · 목적: YouTube·Instagram 시청 중 즉시 진본 확인

## 파일 구성

```
manifest.json      Manifest V3 선언
src/
  content.js       페이지에 버튼·패널 주입, 결과 렌더링
  content.css      주입 UI 스타일
  background.js    서비스 워커. 백엔드 호출 담당
  popup.html       백엔드 주소 설정 화면
  popup.js         설정 저장·불러오기
```

빌드 도구 없이 소스를 그대로 Chrome에 `압축해제된 확장 프로그램 로드`로 설치합니다.

## manifest 요약

| 항목 | 값 |
|---|---|
| `manifest_version` | 3 |
| `permissions` | `storage`, `activeTab` |
| `host_permissions` | `http://localhost:8070/*`, YouTube |
| `content_scripts` | YouTube·Instagram 전체 경로, `document_idle` |

::: warning host_permissions 하드코딩
`localhost:8070`이 고정되어 있어, 다른 서버를 쓰려면 manifest도 함께 수정해야 합니다.
:::

## 동작 흐름

1. `content.js`가 영상 페이지에 검증 버튼 주입
2. 클릭 시 URL을 정규화해 `background.js`에 메시지 전송
3. `background.js`가 `POST /api/verify/url`로 백엔드 호출
4. 결과를 `content.js`가 패널로 렌더링

## SPA 대응

YouTube는 페이지 이동 시 문서를 새로 불러오지 않습니다. 1초 간격 폴링으로 URL 변화를 감지합니다.

## URL 정규화

| 입력 | 출력 |
|---|---|
| `youtube.com/watch?v=ID&list=…&t=…` | `https://www.youtube.com/watch?v=ID` |
| `youtube.com/shorts/ID` | `https://www.youtube.com/shorts/ID` |
| Instagram `/p`, `/reel`, `/tv` | 해당 경로 유지 |
| 그 외 | `location.href` 그대로 |

재생목록·타임스탬프 등 부가 파라미터를 떼어내 같은 영상이 같은 캐시 키를 쓰도록 합니다.

## 결과 표시

판정을 두 갈래로 나눕니다: `진본으로 확인됨` (success) / `진본 확인 안 됨` (warning).

패널에 들어가는 항목:

| 행 | 조건 |
|---|---|
| 판정 | `verdict`가 있을 때 |
| 유사도 거리 | `similarityDistance`가 숫자일 때 |
| 영상 ID | `videoId`가 있을 때 |
| 등록 시각 | `registeredAt`이 있을 때 |
| 블록체인 | 항상 (`검증됨` / `미검증`) |
| VC | 항상 (`검증됨` / `미검증`) |

모든 삽입값은 `escapeHtml()`을 거칩니다.
