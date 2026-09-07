# 알려진 이슈

문서를 쓰면서 코드와 코드, 코드와 문서를 대조해 확인한 불일치입니다.
모두 **실제 파일을 읽고 확인한 것**이며, 추정에는 그렇다고 표시했습니다.

심각도 기준
- **높음** — 사용자에게 잘못된 결과가 보이거나 기능이 동작하지 않음
- **중간** — 동작하지만 표현이 부정확하거나 운영 위험
- **낮음** — 문서·주석 수준의 불일치

---

## 1. 백엔드 테스트가 컴파일되지 않음 — 높음

**위치** `jinbon-backend/src/test/java/com/jinbon/domain/video/service/` (git 미추적)

`./gradlew test`가 컴파일 오류 6건으로 중단됩니다.

```
VideoRegisterServiceTest.java:44  생성자 인자 9개 (실제 12개)
VideoVerifyServiceTest.java:35,64 생성자 인자 7개 (실제 9개)
VideoRegisterServiceTest.java:54  hashService.buildReRegistrationMerkleRoot — 없는 메서드
VideoRegisterServiceTest.java:56  hashService.buildReRegistrationMerklePath — 없는 메서드
VideoVerifyServiceTest.java:77    perceptualHashService.generateRotationFingerprints — 없는 메서드
```

이 두 파일을 제외하면 커밋된 테스트 5개는 컴파일·통과합니다(확인함).

**영향** CI를 붙이면 즉시 실패. 로컬에서도 테스트 실행 불가.

**조치 방향** 참조하는 기능(재등록 머클루트, 회전 핑거프린트)을 구현하거나,
두 파일을 현재 시그니처에 맞게 수정하거나, 커밋에서 제외합니다.

---

## 2. 웹이 구버전 verdict 값을 전제하고 있음 — 중간

**위치** `jinbon-web/app/page.tsx:5-10`

```ts
type VerificationVerdict =
  | "AUTHENTIC_EXACT"      // 백엔드가 더 이상 반환하지 않음
  | "AUTHENTIC_SIMILAR"    // 백엔드가 더 이상 반환하지 않음
  | "REGISTERED_BUT_REVOKED"
  | "NOT_REGISTERED"
  | string;
```

백엔드의 실제 값은 `EXACT_MATCH`, `SAME_CONTENT`, `SIMILAR_MATCH`,
`REGISTERED_BUT_REVOKED`, `CERTIFICATE_INVALID`, `NOT_REGISTERED`, `VERIFICATION_UNAVAILABLE` 7종입니다.

유니언 끝의 `| string` 덕분에 타입 오류는 나지 않고,
화면 분기도 `authentic`·`active`·`NOT_REGISTERED`만 보므로 **표시가 깨지지는 않습니다.**

다만 `CERTIFICATE_INVALID`(보증서 무효)와 `VERIFICATION_UNAVAILABLE`(일시 장애)이
모두 `주의가 필요한 영상입니다` 하나로 뭉쳐집니다. 성격이 전혀 다른 두 상태입니다.

**조치 방향** 타입을 7종으로 갱신하고 최소한 "확인 불가"와 "보증서 문제"를 구분합니다.

---

## 3. 확장이 Netflix를 지원한다고 표시하지만 동작하지 않음 — 중간

**위치** `jinbon-extension/manifest.json`, `README.md`, `src/content.js:31`
vs `jinbon-backend`의 `VideoVerifyService.ALLOWED_VIDEO_HOSTS`

확장은 Netflix 시청 페이지에 버튼을 띄우고 URL을 백엔드로 보냅니다.
백엔드의 허용 호스트는 다음뿐입니다.

```java
Set.of("youtube.com", "youtu.be", "instagram.com", "tiktok.com",
       "twitter.com", "x.com", "vimeo.com")
```

Netflix URL은 `VIDEO_DOWNLOAD_FAILED`(VF002, 400)로 거부되고
패널에 `확인 실패`가 표시됩니다.

또한 확장은 `instagram.com`·`tiktok.com` 등 백엔드가 지원하는 다른 사이트에는
버튼을 띄우지 않습니다. 양쪽 지원 목록이 서로 어긋나 있습니다.

**조치 방향** 두 목록을 일치시키거나, Netflix를 지원 대상에서 빼고
확장의 대상 사이트를 백엔드 허용 목록에 맞춥니다.

---

## 4. 영상 서명 키가 JWT 시크릿과 동일 — 중간

**위치** `jinbon-backend/.../SignatureService.java`

```java
SecretKeySpec keySpec = new SecretKeySpec(
    jwtProperties.getSecret().getBytes(UTF_8), "HmacSHA256");
```

영상 서명(`HMAC-SHA256(issuerDid + merkleRoot)`)이 JWT 서명 키를 그대로 씁니다.

검증 시 서명을 **재계산해서** DB·온체인 값과 대조하므로,
`JWT_SECRET`을 바꾸면 **기존에 등록된 모든 영상의 검증이 실패**하고
`VERIFICATION_UNAVAILABLE`이 됩니다.

즉 토큰 키 로테이션이 사실상 불가능합니다.
두 키는 수명 주기와 노출 범위가 다르므로 분리하는 편이 안전합니다.

참고로 `CI_HMAC_SECRET`은 이미 별도 키로 분리되어 있고,
`application.yml`에 "JWT_SECRET과 반드시 다른 독립 비밀키"라고 명시되어 있습니다.
영상 서명 키에는 같은 원칙이 적용되지 않았습니다.

**조치 방향** `VIDEO_SIGNATURE_SECRET`을 별도로 두되,
기존 데이터 호환을 위해 서명에 키 버전을 함께 기록하는 방식을 검토합니다.

---

## 5. `.env.example`과 `application.yml`의 기본값이 반대 — 중간

| 파일 | `OPENDID_ENABLED` 기본값 |
|---|---|
| `application.yml` | `true` |
| `.env.example` | `false` |

`.env.example`을 복사해 시작하면 **Open DID가 꺼진 상태로 기동**됩니다.
선택과제 1이 동작하지 않는 상태이므로, 처음 실행하는 사람이
"VC가 발급되지 않는다"고 오해하기 쉽습니다.

**조치 방향** 두 기본값을 맞추거나, `.env.example`에 의도를 주석으로 명시합니다.

---

## 6. 확장 README가 존재하지 않는 스크립트를 안내 — 중간

**위치** `jinbon-extension/README.md`

```bash
cd /Users/se00/Documents/projects/jinbon/jinbon-backend
./scripts/run-local.sh
```

두 가지 문제가 있습니다.

- **다른 사람의 로컬 경로**가 하드코딩되어 있습니다.
- `jinbon-backend/scripts/` 디렉터리와 `run-local.sh`가 **존재하지 않습니다**(확인함).

백엔드의 실제 실행 방법은 `docker compose up -d` 후 `./gradlew bootRun`입니다.

**조치 방향** README를 실제 실행 절차로 수정하거나 `scripts/run-local.sh`를 추가합니다.

---

## 7. 활성 프로필 미지정 시 Swagger가 공개됨 — 중간

**위치** `jinbon-backend/.../SecurityConfig.java`

```java
boolean isDev = activeProfiles.contains("dev") || activeProfiles.length == 0;
```

프로필을 지정하지 않으면 개발 모드로 간주되어
`/swagger-ui/**`, `/v3/api-docs/**`, `/auth.html`이 인증 없이 열립니다.

`./gradlew bootRun`을 그냥 실행하는 것이 기본 동작이므로,
같은 방식으로 서버에 올리면 API 문서가 그대로 노출됩니다.

**조치 방향** 기본값을 안전한 쪽(프로필 없으면 운영으로 간주)으로 뒤집거나,
배포 절차에 `SPRING_PROFILES_ACTIVE` 지정을 명시합니다.

---

## 8. 백엔드 README의 verdict 표가 낡음 — 낮음

**위치** `jinbon-backend/README.md`

README는 verdict를 5종으로 설명합니다.

```
EXACT_MATCH, SIMILAR_MATCH, REGISTERED_BUT_REVOKED,
NOT_REGISTERED, VERIFICATION_UNAVAILABLE
```

실제 `VerificationVerdict` enum은 7종이며 `SAME_CONTENT`와 `CERTIFICATE_INVALID`가 빠져 있습니다.

**조치 방향** README 표를 7종으로 갱신합니다.
(이 저장소의 [영상 검증 문서](../20-flows/video-verify.md)에는 7종이 반영되어 있습니다.)

---

## 9. 백엔드 README의 엔드포인트 표에 `vc/prepare` 누락 — 낮음

**위치** `jinbon-backend/README.md`의 API 엔드포인트 표

`POST /api/videos/{id}/vc/prepare`가 표에 없습니다.
실제로는 `VideoRegisterController`에 구현되어 있고 iOS 앱이 호출합니다.

**조치 방향** 표에 추가합니다.

---

## 10. 카카오 챗봇 채널이 문서에만 존재 — 낮음

**위치** `jinbon-backend/docs/JINBON_FLOW_AND_POLICY.md`의 채널 표

| 채널 | 주요 역할 |
|---|---|
| 카카오 챗봇 | 일반 사용자의 간편한 영상 검증 |

대응하는 저장소나 백엔드 연동 코드가 없습니다.

**조치 방향** 계획 단계임을 표기하거나 표에서 제외합니다.

---

## 11. iOS 개발 설정이 특정 IP에 고정 — 낮음

**위치** `jinbon-ios/source/DIDCA/Configuration/Dev.xcconfig`

모든 서버 주소가 `10.48.200.183`으로 하드코딩되어 있습니다.
다른 개발자나 다른 네트워크에서는 매번 파일을 고쳐야 하고,
고친 내용이 커밋에 섞이기 쉽습니다.

`Prod.xcconfig`는 `*.example.com` 자리표시자 상태이며,
`Info.plist`의 `NSAllowsArbitraryLoads`가 `true`입니다(확인함).
두 파일 주석에 프로덕션 배포 전 수정하라고 적혀 있습니다.

**조치 방향** 로컬 오버라이드용 xcconfig를 `.gitignore`에 넣고 분리합니다.

---

## 12. `issuerDid` 필드명이 실제 의미와 다름 — 낮음

**위치** `VideoVerifyResponse.issuerDid`

이 값은 **영상 등록자의 DID**인데 이름은 "발급자 DID"로 읽힙니다.
DTO 주석에도 "레거시 필드명"이라고 적혀 있습니다.

VC 발급기관 DID는 별도로 `vcIssuerDid`입니다.

웹 화면은 이 값을 `발급자 DID`라는 라벨로 표시하고 있어
사용자에게도 오해를 줄 수 있습니다(iOS는 이 값을 화면에 노출하지 않습니다).

**조치 방향** 신규 필드 `registrantDid`를 병행 제공하고 웹 라벨을 `등록자 DID`로 바꿉니다.

---

## 13. 웹의 "블록체인 검증 네트워크 연결됨"은 정적 문구 — 낮음

**위치** `jinbon-web/app/page.tsx`의 `header-status`

실제 연결 상태를 확인하지 않는 고정 텍스트입니다.
백엔드가 꺼져 있어도 "연결됨"으로 표시됩니다.

**조치 방향** 헬스체크와 연동하거나 문구를 중립적으로 바꿉니다.

---

## 14. 확장이 판정값을 영문으로 노출 — 낮음

**위치** `jinbon-extension/src/content.js`의 `formatVerdict()`

`EXACT_MATCH` → `Exact Match`로 변환할 뿐 한국어로 옮기지 않습니다.
나머지 UI 문구가 모두 한국어인 것과 대비됩니다.

**조치 방향** iOS와 같은 한국어 문구 매핑을 추가합니다.

---

## 종합

| # | 항목 | 심각도 |
|---|---|---|
| 1 | 백엔드 테스트 컴파일 실패 | 높음 |
| 2 | 웹의 구버전 verdict 전제 | 중간 |
| 3 | 확장 Netflix 미동작 | 중간 |
| 4 | 영상 서명 키 = JWT 시크릿 | 중간 |
| 5 | `OPENDID_ENABLED` 기본값 불일치 | 중간 |
| 6 | 확장 README의 잘못된 실행 안내 | 중간 |
| 7 | 프로필 미지정 시 Swagger 공개 | 중간 |
| 8 | README verdict 표 낡음 | 낮음 |
| 9 | README에 `vc/prepare` 누락 | 낮음 |
| 10 | 카카오 챗봇 채널 미구현 | 낮음 |
| 11 | iOS 개발 IP 하드코딩 | 낮음 |
| 12 | `issuerDid` 필드명 | 낮음 |
| 13 | 웹 연결 상태 문구 | 낮음 |
| 14 | 확장 판정 영문 노출 | 낮음 |

우선 처리 순서로는 1번(테스트), 7번(Swagger 노출), 5번(기본값)이
적은 노력으로 효과가 큽니다.
