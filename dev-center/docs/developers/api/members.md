# 등록자 프로필 API

검증 결과에 노출되는 **등록자 표시명**을 관리합니다. JWT 인증이 필요합니다.

시청자는 등록자를 DID 문자열이 아니라 표시명(기관명·직함)으로 봅니다.
검증 응답의 `registrantName`이 이 값이며, 표시명이 없으면 모바일 신분증에서 확인한 실명이 노출됩니다.

## GET /api/members/me

```json
{
  "memberId": 1,
  "name": "홍길동",
  "displayName": "기획재정부 대변인실",
  "publicName": "기획재정부 대변인실",
  "userDid": "did:omn:abc123"
}
```

| 필드 | 설명 |
|---|---|
| `name` | 모바일 신분증 본인확인에서 확인한 실명 |
| `displayName` | 등록자가 설정한 표시명. 없으면 `null` |
| `publicName` | 검증 결과에 실제로 노출되는 이름 (`displayName` → 없으면 `name`) |

## PATCH /api/members/me/display-name

```json
{ "displayName": "기획재정부 대변인실" }
```

최대 100자. 비우면 실명으로 돌아갑니다. **응답** — `GET /api/members/me`와 동일

**에러** — `M001` 404: 회원 없음
