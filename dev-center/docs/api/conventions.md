# 공통 규약

기본 주소: `http://localhost:8070`
Swagger UI: `http://localhost:8070/swagger-ui/index.html` (개발 프로필에서만)

## 응답 포맷

모든 응답은 `CommonResponse<T>`로 감쌉니다.

**성공**
```json
{
  "status": 200,
  "message": "Success",
  "data": { }
}
```

**실패**
```json
{
  "status": 409,
  "code": "V004",
  "message": "동일한 영상이 다른 계정에 이미 등록되어 있습니다."
}
```

`null` 필드는 직렬화에서 제외됩니다 (`@JsonInclude(NON_NULL)`).

## 인증

인증이 필요한 API는 헤더에 액세스 토큰을 넣습니다.

```
Authorization: Bearer {accessToken}
```

| 토큰 | 만료 |
|---|---|
| accessToken | 30분 |
| refreshToken | 7일 |

## 업로드 제한

| 항목 | 제한 |
|---|---|
| 파일 크기 | 100MB |
| 요청 전체 | 110MB |
| 초과 시 | `C002` (413) |

## 엔드포인트 목록

| Method | Path | 설명 | 인증 |
|---|---|---|---|
| POST | `/api/auth/token` | OmniOne CX 세션 토큰 발급 | — |
| POST | `/api/auth/app/request` | WebToApp 딥링크 생성 | — |
| POST | `/api/auth/app/verify` | 신분증 검증 + 로그인 | — |
| POST | `/api/auth/did/rebind` | 앱 재설치 후 DID 재연결 | 재연결 토큰 |
| POST | `/api/auth/refresh` | 토큰 갱신 | 리프레시 토큰 |
| POST | `/api/auth/logout` | 로그아웃 | 리프레시 토큰 |
| POST | `/api/signup/token` | 가입용 세션 토큰 발급 | — |
| POST | `/api/signup/app/request` | 가입용 딥링크 생성 | — |
| POST | `/api/signup/app/verify` | 본인확인 + PENDING 회원 생성 | — |
| POST | `/api/signup/did/complete` | DID 연결 + 가입 완료 | 가입 토큰 |
| POST | `/api/videos` | 영상 등록 및 VC 발급 준비 | ISSUER |
| GET | `/api/videos` | 내 영상 목록 | O |
| GET | `/api/videos/{videoId}` | 영상 상세 | O (본인) |
| POST | `/api/videos/{videoId}/vc/prepare` | VC 발급 준비·재개 | O (본인) |
| POST | `/api/videos/{videoId}/vc/complete` | VC 발급 완료 연결 | O (본인) |
| PATCH | `/api/videos/{videoId}/deactivate` | 영상 비활성화 | O (본인) |
| POST | `/api/verify` | 파일 업로드 검증 | — |
| POST | `/api/verify/url` | URL 기반 검증 | — |
