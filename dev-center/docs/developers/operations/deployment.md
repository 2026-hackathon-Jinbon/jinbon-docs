# 배포 가이드 (AWS EC2)

로컬에서 돌던 진본 스택을 EC2 한 대에 올려 **테스트 환경**을 구성하는 절차입니다.

## 무엇을 직접 띄우고, 무엇을 연결만 하는가

가장 먼저 구분해야 할 부분입니다. 외부 벤더 서비스는 **띄우는 것이 아니라 아웃바운드로 연결**합니다.

| 구성 요소 | 위치 | 배포 시 할 일 |
|---|---|---|
| jinbon-backend | 자체 | EC2에서 구동 |
| PostgreSQL 16.4 · Redis 7 | 자체 | `docker-compose.yml`로 구동 |
| Open DID 서버 7종 + Besu | 자체 | Orchestrator로 구동 |
| Open DID용 PostgreSQL | 자체 | `postgre-opendid` 컨테이너 |
| **OmniOne Chain** | **벤더** | `stage-chainapi.omnione.net` 아웃바운드 허용 |
| **OmniOne CX** | **벤더** | `cx.raonsecure.co.kr:18543` 아웃바운드 허용 |

::: tip 체인은 직접 띄우지 않습니다
영상 등록용 OmniOne Chain은 라온시큐어가 운영하는 스테이징 서비스입니다. 스마트 컨트랙트도 이미 배포되어 `CONTRACT_ADDRESS`에 주소가 들어 있습니다. EC2에서는 아웃바운드만 열면 됩니다.

Open DID가 쓰는 Hyperledger Besu는 이와 **별개의 체인**이며, 이쪽은 Orchestrator가 로컬에 띄웁니다.
:::

## TLS는 백엔드에만 필요합니다

Open DID 7개 포트에 각각 인증서를 붙일 필요가 없습니다. 누가 무엇을 호출하는지 보면 명확합니다.

| 호출자 | 대상 | 프로토콜 |
|---|---|---|
| 검증 웹 · Chrome 확장 · 카카오톡 챗봇 | **백엔드만** | HTTPS 필요 |
| 백엔드 | Open DID TAS · Issuer | 서버 내부 HTTP |
| iOS 앱 (개발 빌드) | Open DID 6종 | HTTP (ATS 예외) |

즉 **`api.도메인` 하나에만 TLS를 걸면 됩니다.** Open DID는 사설/공인 IP 위에서 HTTP로 두어도 됩니다.

::: warning Open DID는 IP 기반입니다
`docker/opendid/update-ip.sh`는 설정 파일과 **DB 레코드 안의 IP 문자열**까지 정규식으로 치환합니다. 도메인 이름은 처리하지 못합니다.

따라서 Open DID는 **고정 IP 위에서 운영해야 합니다.** EC2 재시작으로 퍼블릭 IP가 바뀌면 전체 재설정이 필요하므로 **Elastic IP를 반드시 할당**하세요.
:::

## 인스턴스 사양

| 항목 | 값 |
|---|---|
| 인스턴스 | **t3.large** (2 vCPU / 8 GB) |
| 디스크 | gp3 **50 GB 이상** (Besu 체인 데이터) |
| IP | **Elastic IP 필수** |
| 리전 | ap-northeast-2 (서울) |

### 메모리 예산

JVM이 9개 뜹니다 — Open DID 7종(TAS · Issuer · Verifier · API · CA · Wallet · Demo), Besu, 백엔드. 여기에 PostgreSQL 2벌과 Redis가 더해집니다.

::: warning 힙 제한은 선택이 아닙니다
Spring Boot는 `-Xmx`가 없으면 기본 힙을 **물리 메모리의 1/4**로 잡습니다. 8 GB 머신에서 JVM마다 2 GB씩 요구하면 9개가 서로 메모리를 빼앗아 OOM이 납니다.

Open DID 서버는 Orchestrator의 `jars/start.sh`가 `java -jar`로 띄우며 힙 옵션이 없습니다. 벤더 스크립트를 고치는 대신 **환경변수로 거세요.**

```bash
# Open DID 기동 전 — 이 셸에서 뜨는 모든 JVM에 적용
export JAVA_TOOL_OPTIONS="-Xmx512m"

# 백엔드는 명령행에서 직접 지정 (JAVA_TOOL_OPTIONS보다 우선)
java -Xmx1g -jar build/libs/*.jar
```
:::

| 구성 | 할당 |
|---|---|
| Open DID 7 × 512 MB | 3.5 GB |
| 백엔드 | 1.0 GB |
| Besu | 1.5 GB |
| PostgreSQL 2벌 | 0.8 GB |
| Redis | 0.1 GB |
| OS·여유 | 0.5 GB |
| **합계** | **≈ 7.4 GB** |

8 GB에 들어가지만 여유가 크지 않습니다. 시연 직전 메모리가 부족하면 **중지 → 인스턴스 유형 변경 → 시작**으로 t3.xlarge(16 GB)로 올릴 수 있습니다. 5분이면 되고, Elastic IP를 쓰므로 IP가 유지되어 Open DID 재설정도 필요 없습니다.

### 비용

EC2는 **실행 중인 시간만** 과금됩니다. 안 쓸 때 중지하면 인스턴스 요금은 발생하지 않습니다.

| 사용 패턴 | t3.large 대략치 |
|---|---|
| 작업·시연 때만 (8h × 10일) | 약 $10 |
| 일주일 24시간 | 약 $19 |
| 한 달 24시간 | 약 $83 |

::: tip 중지 중에도 나가는 비용
- **EBS 50 GB** — 월 약 $5 (중지해도 계속)
- **Elastic IP** — 실행 중인 인스턴스에 연결돼 있으면 무료지만, **인스턴스를 중지하면 시간당 과금**됩니다 (월 3~4천원 수준)

Open DID가 IP에 묶여 있어 EIP를 해제할 수는 없습니다.
:::

위 단가는 서울 리전 온디맨드 대략치입니다. 실제 청구액은 AWS 요금 페이지에서 확인하세요. 해커톤에서 AWS 크레딧을 제공한다면 먼저 확인해 보시기 바랍니다.

### 보안 그룹

| 방향 | 포트 | 소스 | 용도 |
|---|---|---|---|
| 인바운드 | 22 | 내 IP | SSH |
| 인바운드 | 80 · 443 | 0.0.0.0/0 | 백엔드 (TLS 종단) |
| 인바운드 | 8090–8095 | 개발자 IP | Open DID (iOS 개발 빌드용) |
| 아웃바운드 | 전체 | — | OmniOne Chain · CX 연동 |

Open DID 포트를 전체 공개할 이유는 없습니다. iOS 개발 빌드에서 접근할 IP만 여세요.

## prod 프로파일 (필수)

::: danger 프로파일을 지정하지 않으면 Swagger가 공개됩니다
`SecurityConfig`는 **프로파일이 비어 있으면 개발 모드로 간주**합니다.

```java
boolean isDev = environment.getActiveProfiles().contains("dev")
        || environment.getActiveProfiles().length == 0;

if (isDev) {
    auth.requestMatchers("/swagger-ui/**", "/v3/api-docs/**").permitAll()
        .requestMatchers("/auth.html").permitAll();
}
```

`SPRING_PROFILES_ACTIVE`를 설정하지 않은 채 배포하면 Swagger UI와 `auth.html`이 인터넷에 열립니다. `dev`라는 값 역시 같은 분기를 타므로 **배포 서버에 `dev`를 주면 안 됩니다.**
:::

`src/main/resources/application-prod.yml`에 배포 서버용 동작을 모아두었습니다.

```yaml
spring:
  jpa:
    hibernate:
      ddl-auto: validate      # 기본 update — 스키마 자동 변경 방지
    show-sql: false           # SQL 로그에 데이터 노출 방지
    properties:
      hibernate:
        format_sql: false

cors:
  allowed-origins: ${CORS_ALLOWED_ORIGINS:}

logging:
  level:
    com.jinbon: INFO          # 기본 DEBUG
    org.hibernate.SQL: WARN
```

```bash
SPRING_PROFILES_ACTIVE=prod java -jar build/libs/*.jar
```

호스트·포트·시크릿 같은 **값**은 `.env`에, 환경에 따라 달라지는 **동작**은 이 프로파일에 둡니다. 두 방식을 섞으면 어느 설정이 적용됐는지 추적하기 어려워집니다.

::: warning 빈 DB로 시작할 때는 최초 1회 스키마 생성이 필요합니다
`ddl-auto: validate`는 스키마가 이미 있을 때만 통과합니다. 빈 DB에서는 `Schema-validation` 오류로 기동이 중단됩니다.

프로파일을 빼고 띄우면 Swagger가 열리므로, **prod는 유지한 채 환경변수로 한 번만 덮어쓰세요.**

```bash
# 최초 1회 — 스키마 생성
SPRING_PROFILES_ACTIVE=prod \
SPRING_JPA_HIBERNATE_DDL_AUTO=update \
java -jar build/libs/*.jar

# 이후 — 평소 기동
SPRING_PROFILES_ACTIVE=prod java -jar build/libs/*.jar
```

Spring의 relaxed binding이 `SPRING_JPA_HIBERNATE_DDL_AUTO`를 `spring.jpa.hibernate.ddl-auto`로 매핑하므로 파일을 고칠 필요가 없습니다.
:::

### localhost 하드코딩에 대하여

`application.yml`의 아래 설정은 환경변수로 뺄 수 없습니다.

```yaml
  data:
    redis:
      host: localhost
      port: 6380
opendid:
  tas-server-url: http://localhost:8090
  issuer-server-url: http://localhost:8091
```

다만 **단일 인스턴스 구성에서는 그대로 두어도 동작합니다.** 백엔드는 `docker-compose`에 포함되어 있지 않고 호스트에서 `java -jar`로 실행되며, Redis와 Open DID도 같은 EC2에 올라가므로 `localhost`가 정확히 맞는 주소입니다.

환경변수로 분리해야 하는 경우는 두 가지입니다.

- 백엔드를 **컨테이너로 실행**할 때 — 컨테이너 안의 `localhost`는 자기 자신을 가리킵니다
- Open DID나 Redis를 **다른 인스턴스로 분리**할 때

## 환경 변수

`.env.example`을 기준으로 `.env`를 만듭니다. 값은 저장소에 커밋되지 않습니다(`.gitignore` 처리 완료).

```bash
DB_HOST=localhost
DB_PORT=5432
DB_PASSWORD=...
SERVER_PORT=8070

# 벤더 서비스 — 로컬 값 그대로
OMNIONE_CX_URL=https://cx.raonsecure.co.kr:18543
BLOCKCHAIN_RPC_URL=https://stage-chainapi.omnione.net
BLOCKCHAIN_API_TOKEN=...
CONTRACT_ADDRESS=0x...
WALLET_ADDRESS=0x...
KEYSTORE_PASSWORD=...

# Open DID (같은 EC2에서 구동되므로 URL 설정 불필요)
OPENDID_ENABLED=true

JWT_SECRET=...
CI_HMAC_SECRET=...

# 운영에서는 반드시 지정 (미설정 시 전체 허용)
CORS_ALLOWED_ORIGINS=https://웹도메인,chrome-extension://<확장ID>
```

::: danger JWT_SECRET을 새로 만들지 마세요
`JWT_SECRET`은 **JWT 서명과 영상 서명에 함께 쓰입니다.** 값을 바꾸면 기존에 등록된 모든 영상의 서명 재계산이 달라져 **검증이 전부 `확인 중`(`VERIFICATION_UNAVAILABLE`)이 됩니다.**

`CI_HMAC_SECRET`도 변경 금지입니다. 회원 중복 확인·로그인·DID 복구가 모두 깨집니다.

로컬 데이터를 살려서 시연할 계획이라면 **로컬 `.env`의 시크릿을 그대로 옮기세요.**

빈 DB로 새로 시작하는 경우에는 새 값을 생성해도 됩니다. 다만 한 번 영상을 등록한 뒤에는 같은 제약이 그대로 적용됩니다.
:::

`omnione-chain-keystore.json`도 git에 없으므로 별도로 복사해야 합니다. `WALLET_ADDRESS`·`CONTRACT_ADDRESS`와 **동일한 배포 지갑**이어야 합니다.

## 배포 절차

### 1. 인스턴스 준비

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk docker.io docker-compose-v2 git nodejs npm caddy
sudo usermod -aG docker $USER   # 재로그인 필요
```

::: warning Node.js와 docker-compose 셰임이 필요합니다
- **Node.js** — Besu 컨트랙트를 hardhat으로 배포합니다 (`shells/Besu/start.sh`가 `npm install`·`npx hardhat run` 실행)
- **`docker-compose`(하이픈)** — Orchestrator 스크립트가 v1 문법을 씁니다. Compose v2만 설치하면 `command not found`로 실패합니다.

```bash
printf '#!/bin/sh\nexec docker compose "$@"\n' | sudo tee /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
:::

### 2. 저장소와 비밀값 배치

```bash
git clone <jinbon-backend>
cd jinbon-backend
cp /경로/.env .env                                   # git에 없음
mkdir -p src/main/resources/keystore
cp /경로/omnione-chain-keystore.json src/main/resources/keystore/
```

### 3. 인프라 기동

```bash
docker compose up -d      # postgres 5432, redis 6380
```

### 4. Open DID 기동

::: danger reset-all.sh 전에 PostgreSQL을 직접 띄워야 합니다
`reset-all.sh`는 `postgre-opendid` 컨테이너가 **이미 떠 있다고 가정**합니다. 직접 기동하지 않습니다. 없는 상태로 실행하면 DB 생성이 조용히 실패하고, 이어서 Open DID 서버 7개가 전부 기동에 실패합니다.

```
Connection to 127.0.0.1:5430 refused
  → BeanCreationException: Error creating bean with name 'liquibase'
```

**포트는 반드시 5430입니다.** 서버 JAR 내부 기본값이 5430으로 박혀 있어 다른 포트로 띄우면 위 오류가 납니다.

```bash
cd docker/opendid/did-orchestrator-server/source/did-orchestrator-server/shells/Postgre
POSTGRES_PORT=5430 POSTGRES_USER=omn POSTGRES_PASSWORD=omn POSTGRES_DB=postgres \
  docker-compose up -d
docker ps --filter name=postgre-opendid    # 5430->5432 확인
```
:::

그다음 Orchestrator가 Besu와 7개 서버를 함께 올립니다. **Elastic IP를 인자로 넘기는 것이 핵심입니다.**

```bash
cd ~/jinbon-backend/docker/opendid
export JAVA_TOOL_OPTIONS="-Xmx512m"   # 8GB 인스턴스에서는 필수
setsid nohup bash reset-all.sh <ELASTIC_IP> </dev/null > /tmp/opendid.log 2>&1 &
```

10~20분 걸립니다. `setsid nohup`으로 띄우지 않으면 SSH 세션이 끊길 때 함께 죽습니다.

::: warning pkill로 정리할 때 자기 세션을 죽이지 않도록
`pkill -f "reset-all.sh"`는 **그 명령을 실행 중인 SSH 세션의 명령줄까지 매칭**해 스스로를 종료시킵니다. 대괄호 트릭을 쓰세요.

```bash
pkill -9 -f "[j]ava.*application.yml"
pgrep -f "[r]eset-all.sh"
```
:::

::: danger 서버 설정에 개발 PC의 절대 경로가 박혀 있습니다
`jars/*/application.yml` 7개에는 **로컬에서 기동할 때 기록된 macOS 절대 경로**가 남아 있습니다. `reset-all.sh`는 이를 고치지 않으므로 EC2에서 그대로 기동하면 6개 서버가 전부 죽습니다.

```
java.nio.file.NoSuchFileException:
  /Users/<로컬사용자>/.../shells/Besu/Issuer/blockchain.properties
    → BeanCreationException: 'blockChainServiceImpl' → 'contractApi'
```

`easy-adoption-injector.sh`의 IP 주입도 실제로는 적용되지 않는 경우가 있습니다. 경로와 IP를 함께 직접 치환하는 편이 확실합니다.

```bash
O=~/jinbon-backend/docker/opendid/did-orchestrator-server/source/did-orchestrator-server
for f in $O/jars/*/application.yml; do cp "$f" "$f.bak"; done

sed -i "s|/Users/<로컬사용자>/IdeaProjects/jinbon-backend|/home/ubuntu/jinbon-backend|g; \
        s|<로컬IP>|<ELASTIC_IP>|g" $O/jars/*/application.yml

# 확인 — 둘 다 0이어야 함
grep -l "/Users/" $O/jars/*/application.yml | wc -l
grep -l "<로컬IP>" $O/jars/*/application.yml | wc -l
```

치환 후 서버를 재기동합니다.

```bash
pkill -9 -f "[j]ava.*application.yml"; sleep 2
export JAVA_TOOL_OPTIONS="-Xmx512m"
for dp in "TA:8090" "Issuer:8091" "Verifier:8092" "API:8093" "CA:8094" "Wallet:8095"; do
  D="${dp%%:*}"; P="${dp##*:}"
  bash $O/jars/start.sh "$(ls $O/jars/$D/*.jar | head -1)" "$P" "$O/jars/$D/application.yml"
done
```

Demo 서버(8099)는 시연에 쓰지 않으면 띄우지 않아도 됩니다.
:::

::: warning 2 vCPU에서는 부팅이 오래 걸립니다
JVM 6개가 동시에 뜨면 load average가 15까지 올라가 기동에 수 분이 걸립니다. 로그가 갱신되고 있으면 멈춘 것이 아니니 기다리세요. **시연 직전에 재부팅하지 마세요.**
:::

이미 구성된 환경의 IP만 바꿀 때는:

```bash
sh update-ip.sh <ELASTIC_IP>     # 설정 + DB 레코드 + iOS 설정 일괄 교체
```

`update-ip.sh`가 수행하는 일:

1. Open DID 서버 프로세스 종료
2. `easy-adoption-injector.sh`로 `application.yml` IP 교체
3. `issuer` · `tas` · `verifier` · `cas` · `wallet` **5개 DB의 모든 문자열 컬럼에서 IP 치환**
4. iOS `URLs.swift` · `Dev.xcconfig` 갱신 후 서버 재시작 · 상태 점검

::: danger reset-all.sh의 7~8단계는 현재 API와 맞지 않습니다
VC 네임스페이스·스키마·발급 프로파일 생성 요청이 **경로와 페이로드 모두 어긋나** 실패합니다. 게다가 스크립트가 모든 실패를 `(may already exist)`로 출력해 성공처럼 보입니다.

| 항목 | 스크립트가 보내는 값 | 실제 API |
|---|---|---|
| 네임스페이스 본문 | `{namespaceId, name, ref, schemaClaims}` | `{namespace, items}` |
| VC 스키마 경로 | `/issuer/admin/v1/vc-schema` | `/issuer/admin/v1/vc-schemas` |
| `namespaces` | `["ns-jinbon-video-01"]` | `[1]` — 숫자 DB id |
| `vcSchemaId` (프로파일) | 문자열 | `Long` — 숫자 DB id |

DTO는 Issuer JAR에서 직접 확인할 수 있습니다.

```bash
J=$O/jars/Issuer/did-issuer-server-2.0.0.jar
jar xf "$J" BOOT-INF/classes/org/omnione/did/issuer/v1/admin/dto/vc/VcSchemaReqDto.class
javap -p -cp BOOT-INF/classes org.omnione.did.issuer.v1.admin.dto.vc.VcSchemaReqDto
```

네임스페이스는 아래 형태로 보내면 생성됩니다.

```json
{
  "namespace": { "id": "ns-jinbon-video-01", "name": "VideoAuthenticity", "ref": "<ISSUER>/issuer/api/v1/vc/vcplan-jinbon-01" },
  "items": [ { "id": "videoHash", "caption": "영상 해시", "type": "text", "format": "plain", "hideValue": false } ]
}
```
:::

::: danger 엔티티 온보딩은 reset-all.sh가 하지 않습니다
네임스페이스까지 만들어도 VC 스키마 등록은 다음 오류로 막힙니다.

```
Issuer → SSRVISS000900: received unknown data from the Tas
TAS    → Finding Entity by DID: null / Entity not found for did null
```

Open DID는 각 엔티티(TAS·Issuer·Verifier·CA·Wallet)가 DID를 생성해 체인에 앵커링하고 **TAS에 등록**하는 온보딩을 거쳐야 합니다. `reset-all.sh`는 DB를 드롭하면서 이 등록 상태까지 지우지만, 다시 만들어주지는 않습니다.

**따라서 `reset-all.sh`만으로는 신규 환경을 완성할 수 없습니다.** 두 가지 방법이 있습니다.

- **기존 DB 이관(권장)** — 동작하는 환경의 `tas`·`issuer`·`verifier`·`cas`·`wallet` DB를 덤프해 복원한 뒤 `update-ip.sh <새IP>`로 IP만 교체합니다. 등록 상태가 보존됩니다. `update-ip.sh`가 DB 레코드의 IP까지 치환하도록 작성된 것이 이 워크플로를 전제합니다.
- **Orchestrator로 재온보딩** — `did-orchestrator-server-2.0.0.jar`(9001)를 띄워 UI에서 엔티티를 등록합니다. 보안 그룹에 9001 개방이 필요합니다.
:::

### 5. 백엔드 기동

```bash
./gradlew bootJar

# 빈 DB라면 최초 1회만 — 스키마 생성
SPRING_PROFILES_ACTIVE=prod SPRING_JPA_HIBERNATE_DDL_AUTO=update \
  java -Xmx1g -jar build/libs/*.jar

# 평소 기동
SPRING_PROFILES_ACTIVE=prod nohup java -Xmx1g -jar build/libs/*.jar > backend.log 2>&1 &
```

::: tip 빈 DB로 시작하면 시연 데이터를 새로 만들어야 합니다
등록된 영상이 하나도 없으므로 모든 검증이 `미인증`으로 나옵니다. `진본` 판정을 보여주려면 **EC2 환경에 연결된 iOS 앱으로 영상을 먼저 등록**해야 하며, 이때 Open DID 전체와 OmniOne CX 본인확인이 모두 동작해야 합니다.

시연 직전이 아니라 **환경 구성 직후에 등록을 마쳐두세요.**
:::

### 6. TLS

```
# Caddyfile
api.도메인 {
    reverse_proxy localhost:8070
}
```

```bash
sudo caddy run --config Caddyfile
```

Let's Encrypt 인증서를 자동 발급합니다. 도메인 A 레코드가 Elastic IP를 가리키고 있어야 합니다.

## 클라이언트 설정 변경

| 대상 | 변경 내용 |
|---|---|
| **Chrome 확장** | `manifest.json`의 `host_permissions`에서 `localhost:8070` → `https://api.도메인` |
| **검증 웹** | API base URL → `https://api.도메인` |
| **카카오톡 챗봇** | 스킬 서버 콜백 URL 등록 (**HTTPS 필수**) |
| **iOS 앱** | `update-ip.sh`가 자동 갱신 · ATS 예외 확인 |

## 기동 후 점검

```bash
# Open DID 7종
for p in 8090 8091 8092 8093 8094 8095 8099; do
  printf "%s " $p; curl -s -o /dev/null -w "%{http_code}\n" http://<ELASTIC_IP>:$p
done

# 백엔드
curl -s -o /dev/null -w "%{http_code}\n" https://api.도메인/api/verify

# 외부 연동 (EC2에서)
curl -sI https://stage-chainapi.omnione.net | head -1
curl -sI https://cx.raonsecure.co.kr:18543 | head -1
```

검증 판정이 `확인 중`으로만 나온다면 `JWT_SECRET` 변경 또는 OmniOne Chain 연결 실패를 먼저 의심하세요.

## 자주 겪는 문제

| 증상 | 원인 |
|---|---|
| 모든 검증이 `확인 중` | `JWT_SECRET`이 바뀌어 영상 서명 재계산 불일치 |
| 모든 검증이 `미인증` | `OPENDID_ENABLED=false` → VC 미발급(`CERTIFICATE_MISSING`) |
| 등록 실패 | OmniOne Chain 아웃바운드 차단 또는 토큰 만료 |
| 웹·확장에서 CORS 오류 | `CORS_ALLOWED_ORIGINS` 미설정 또는 오리진 누락 |
| 재부팅 후 전체 장애 | Elastic IP 미할당 — 퍼블릭 IP 변경 |
| 기동 실패 | `CI_HMAC_SECRET` 미설정 (보안 정책상 기동 차단) |
| 서버가 임의로 죽음 · OOM Killer | `-Xmx` 미설정으로 JVM들이 메모리 초과 요구 |
| 기동 실패 (`Schema-validation`) | `ddl-auto: validate` + 빈 DB — 최초 1회 `update` 필요 |
| Swagger가 외부에 보임 | `SPRING_PROFILES_ACTIVE=prod` 미설정 |

## 범위와 한계

이 문서는 **테스트·시연 환경** 기준입니다. 운영 환경으로 가려면 추가로 필요합니다.

- Open DID 서버의 systemd 서비스화 (현재는 `nohup` 기반 스크립트)
- DB 백업 · Besu 데이터 볼륨 스냅샷
- 시크릿을 `.env` 파일이 아닌 AWS Secrets Manager 등으로 이전
- 백엔드 이중화 (현재 단일 인스턴스 · Redis 캐시 의존)
