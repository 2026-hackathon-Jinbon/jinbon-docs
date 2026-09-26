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
| `host_permissions` | 로컬 주소, 배포 API 호스트, YouTube·Instagram |
| `content_scripts` | YouTube·Instagram 전체 경로, `document_idle` |

기본 백엔드 주소는 `http://localhost:8070`입니다. 팝업에서 주소를 바꿀 수 있지만, 해당 호스트가 `manifest.json`의 `host_permissions`에도 포함되어 있어야 합니다.

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

`displayStatus`를 보고 제목과 색상을 결정하며, 값이 없는 이전 응답은 `authentic`으로 구분합니다. 현재 제목은 ‘진본 확인’, ‘원본 불일치’, ‘등록 기록 없음’, ‘확인 불가’입니다. 조건은 [웹의 결과 표시](/developers/architecture/component-web#result-display)와 같습니다.

패널에는 확인 방식, 등록자 표시명, 등록 증거의 검증 여부, 등록 시각을 표시합니다. `CONTENT_SIMILAR` 결과에서 영상·음성 비교 정보가 모두 있고 불일치 구간이 확인되면 해당 사유를 안내합니다.

`PARTIAL_SIMILAR` 분기는 이전 응답을 위한 코드이며 현재 백엔드는 이 표시 상태를 반환하지 않습니다. 모든 삽입값은 `escapeHtml()`을 거칩니다.
