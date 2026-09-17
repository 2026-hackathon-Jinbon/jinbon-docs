<template>
  <div class="home-page">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-inner">
        <span class="hero-badge">Blockchain Video Verification</span>
        <h1 class="hero-title">
          <span>등록 영상과 일치하는지</span>
          <span>누가 언제 등록했는지 확인하세요.</span>
        </h1>
        <p class="hero-desc">
          진본은 영상의 디지털 지문을 블록체인에 기록해
          제출 영상과의 관계 및 누가 언제 등록했는지를 확인하는 서비스입니다.
        </p>
        <p class="hero-note">영상 속 사건의 사실성과 AI 생성 여부 및 제작자와 저작권자 여부는 보증하지 않습니다.</p>
        <div class="hero-actions">
          <a href="/downloads" class="btn btn-primary">영상 검증하기</a>
          <a href="/use-cases" class="btn btn-secondary">사용 사례 보기</a>
        </div>
        <p class="hero-hint">검증은 로그인 없이 웹과 Chrome 확장 또는 카카오톡에서 바로 할 수 있습니다.</p>
      </div>
    </section>

    <!-- How it works -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">How it works</span>
        <h2 class="section-title">두 가지 질문으로 영상을 검증합니다</h2>
        <div class="proof-grid">
          <div class="proof-card">
            <div class="proof-icon">
              <svg aria-hidden="true" focusable="false" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h3>영상 비교</h3>
            <p class="proof-question">등록 파일 또는 등록 지문과 얼마나 일치하는가?</p>
            <p class="proof-answer">파일 해시로 정확한 일치를 확인합니다. 파일이 다르면 영상과 음성 지문으로 유사도를 비교합니다. 블록체인의 등록 기록도 별도로 확인합니다.</p>
            <span class="proof-tech">OmniOne Chain</span>
          </div>
          <div class="proof-card">
            <div class="proof-icon">
              <svg aria-hidden="true" focusable="false" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3>등록 사실 확인</h3>
            <p class="proof-question">누가 언제 등록했는가?</p>
            <p class="proof-answer">모바일 신분증으로 본인확인을 마친 등록자는 DID 기반 보증서(VC)를 발급받아 등록 사실을 제3자에게 증명할 수 있습니다.</p>
            <span class="proof-tech">Open DID + OmniOne CX</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Hash -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">Core Technology</span>
        <h2 class="section-title">두 종류의 해시로 만드는 하나의 지문</h2>
        <div class="hash-flow">
          <div class="hash-step">
            <div class="hash-num">1</div>
            <div>
              <h3>fineHash</h3>
              <p>파일 전체의 SHA-256.<br/>바이트 단위로 동일한 원본인지 확인합니다.</p>
            </div>
          </div>
          <div class="hash-step">
            <div class="hash-num">2</div>
            <div>
              <h3>perceptualHash</h3>
              <p>프레임별 DCT 기반 지각해시.<br/>재인코딩하거나 크기를 조정한 영상의 유사 후보를 찾습니다.</p>
            </div>
          </div>
          <div class="hash-step hash-step-result">
            <div class="hash-num hash-num-dark">3</div>
            <div>
              <h3>merkleRoot</h3>
              <p>두 해시를 결합한 SHA-256.<br/>블록체인에 기록되는 대표 지문입니다.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Verification technology -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">Verification Technology</span>
        <h2 class="section-title">영상과 음성을 따로 대조합니다</h2>
        <p class="section-desc">파일이 다르면 지각해시로 유사 후보를 찾은 뒤 <strong>1초 간격의 대표 프레임과 음성 지문</strong>을 비교합니다. 이는 샘플 기반 유사도 평가이며 전체 영상의 무변조를 확정하는 검사는 아닙니다.</p>
        <div class="pipeline">
          <div class="pipeline-step">
            <span class="pipeline-stage">1차</span>
            <h3>후보 선별</h3>
            <p>파일 해시가 같으면 파일 일치를 확인하고 등록 증거 검증으로 넘어갑니다. 다르면 16프레임 지각해시로 후보를 찾습니다.</p>
          </div>
          <div class="pipeline-step pipeline-step-key">
            <span class="pipeline-stage pipeline-stage-key">2차</span>
            <h3>구간 대조</h3>
            <p>영상과 음성 지문을 각각 일정한 시간 간격으로 맞춰보며 <strong>대응 비율</strong>을 계산합니다.</p>
            <div class="pipeline-metrics">
              <span class="metric"><em>영상 커버리지</em><b class="metric-num">≥ 95%</b></span>
              <span class="metric"><em>음성 커버리지</em><b class="metric-num">≥ 90%</b></span>
              <span class="metric"><em>대조 방식</em><b>일정한 시간 간격</b></span>
            </div>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-stage">3차</span>
            <h3>등록 증거</h3>
            <p>서명을 재계산해 DB와 온체인 양쪽에 대조합니다. 이어서 VC 보증서가 등록 당시 정보와 결속됐는지 확인합니다.</p>
          </div>
        </div>
        <div class="detect-panel">
          <h3 class="detect-title">비교에서 차이가 나타날 수 있는 사례</h3>
          <ul class="detect-list">
            <li><strong>음성만 교체</strong><span>음성 지문의 대응 비율이 낮아질 수 있습니다</span></li>
            <li><strong>얼굴이나 입모양 변경</strong><span>대표 프레임에 변화가 반영되면 차이가 나타날 수 있습니다</span></li>
            <li><strong>장면 삽입</strong><span>대응하지 않는 샘플 구간을 표시합니다. 삽입 여부를 확정하지는 않습니다</span></li>
            <li><strong>구간 순서 바꾸기</strong><span>같은 시간 간격으로 맞지 않는 구간은 대응 비율을 낮출 수 있습니다</span></li>
          </ul>
          <p class="detect-note"><strong>재인코딩본이나 연속 쇼츠</strong>도 후보 검색과 비교 기준 및 등록 증거 검증을 통과하면 승인될 수 있습니다. 짧은 편집과 작은 화면 변화 또는 일부 음성 교체는 놓칠 수 있습니다. 일부 구간의 대응이 전체 맥락을 보증하지는 않습니다.</p>
        </div>
      </div>
    </section>

    <!-- Verdict -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">Verification</span>
        <h2 class="section-title">검증 결과</h2>
        <p class="section-desc">등록 기록과 콘텐츠 상태를 함께 확인해 네 가지로 표시합니다.</p>
        <div class="verdict-grid">
          <div class="verdict-item verdict-success">
            <span class="verdict-code">진본</span>
            <span class="verdict-desc">파일 일치 또는 유사도 기준을 충족하며 등록 증거도 유효함</span>
          </div>
          <div class="verdict-item verdict-warn">
            <span class="verdict-code">콘텐츠 유사</span>
            <span class="verdict-desc">등록 후보는 찾았지만 유사도 승인 기준 미달 또는 비교 정보 부족</span>
          </div>
          <div class="verdict-item verdict-neutral">
            <span class="verdict-code">미인증</span>
            <span class="verdict-desc">등록 원본이 없거나 등록이 취소됐거나 보증서가 유효하지 않음</span>
          </div>
          <div class="verdict-item verdict-pending">
            <span class="verdict-code">확인 중</span>
            <span class="verdict-desc">외부 장애 또는 온체인 무결성 검증 실패로 상세 사유 확인 필요</span>
          </div>
        </div>
        <p class="verdict-note">진본 배지는 <strong>콘텐츠 비교와 등록 증거 검증을 모두 통과</strong>했다는 뜻입니다. 파일 정확 일치와 유사도 기준 통과는 보증 수준이 다릅니다. <a href="/verification-status">판정별 의미와 한계 보기</a></p>
      </div>
    </section>

    <!-- System -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">System</span>
        <h2 class="section-title">네 개의 접점을 잇는 하나의 백엔드</h2>
        <div class="channel-grid">
          <div class="channel-card">
            <div class="channel-icon">
              <svg aria-hidden="true" focusable="false" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            </div>
            <h3>iOS 앱 <span class="channel-status">배포 준비 중</span></h3>
            <span class="channel-badge channel-badge-code">jinbon-ios</span>
            <p>회원가입부터 DID/Wallet 관리와 <strong>영상 등록</strong> 및 VC 보증서 보관까지 지원</p>
            <span class="channel-tech">Swift / UIKit / DIDWalletSDK</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg aria-hidden="true" focusable="false" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <h3>검증 웹</h3>
            <span class="channel-badge channel-badge-code">jinbon-web</span>
            <p>파일 업로드로 영상 검증. <strong>로그인 불필요.</strong></p>
            <span class="channel-tech">Next.js 16 / React 19 / Tailwind CSS</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg aria-hidden="true" focusable="false" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <h3>Chrome 확장</h3>
            <span class="channel-badge channel-badge-code">jinbon-extension</span>
            <p>YouTube와 Instagram 영상 페이지에서 <strong>버튼 하나로 검증.</strong> URL 기반이라 파일 다운로드가 필요 없습니다.</p>
            <span class="channel-tech">Manifest V3 / JavaScript</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg aria-hidden="true" focusable="false" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <h3>카카오톡 챗봇 <span class="channel-status">채널 추가 가능</span></h3>
            <span class="channel-badge">카카오톡 채널</span>
            <p>카카오톡 대화창에서 영상 URL을 보내면 <strong>즉시 검증 결과를 응답.</strong> 검증 응답은 백엔드 배포 후 동작합니다.</p>
            <span class="channel-tech">카카오톡 채널 / 챗봇</span>
          </div>
          <div class="channel-card channel-card-primary">
            <div class="channel-icon">
              <svg aria-hidden="true" focusable="false" width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
            </div>
            <div class="channel-body">
              <h3>백엔드 API</h3>
              <span class="channel-badge channel-badge-code">jinbon-backend</span>
              <p>등록과 검증 및 인증의 <strong>중심 허브.</strong> 위 네 개 접점이 모두 여기로 모입니다. 인증과 회원 및 영상 검증 REST API를 제공합니다.</p>
              <span class="channel-tech">Java 21 / Spring Boot / PostgreSQL / Redis</span>
            </div>
          </div>
        </div>
        <p class="section-cta"><a href="/downloads">채널별 시작 방법 보기</a></p>
      </div>
    </section>

    <!-- Quick links -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">Documentation</span>
        <h2 class="section-title">문서 바로가기</h2>
        <div class="links-grid">
          <a href="/developers/architecture/overview" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            </div>
            <div>
              <h3>시스템 아키텍처</h3>
              <p>전체 구성도와 계층별 책임 및 포트 맵과 데이터 흐름</p>
            </div>
          </a>
          <a href="/developers/api/conventions" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </div>
            <div>
              <h3>API 레퍼런스</h3>
              <p>인증과 회원 및 영상 검증 엔드포인트<br/>요청/응답 예시와 에러 코드</p>
            </div>
          </a>
          <a href="/developers/flows/video-register" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <div>
              <h3>핵심 플로우</h3>
              <p>영상 등록과 검증<br/>가입/로그인 및 VC 발급 시퀀스</p>
            </div>
          </a>
          <a href="/developers/data/model" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
            </div>
            <div>
              <h3>데이터 모델</h3>
              <p>DB 스키마와 스마트 컨트랙트 및 Redis 키 구조</p>
            </div>
          </a>
          <a href="/developers/security/overview" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            </div>
            <div>
              <h3>보안</h3>
              <p>CI 보호와 SSRF 방어 및 인증 정책과 키 관리</p>
            </div>
          </a>
          <a href="/developers/guide/concepts" class="link-card">
            <div class="link-card-icon">
              <svg aria-hidden="true" focusable="false" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            </div>
            <div>
              <h3>핵심 개념</h3>
              <p>용어 정리와 설계 원칙 및 장애 격리 정책</p>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- Design principles -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">Principles</span>
        <h2 class="section-title">설계 원칙</h2>
        <div class="principles-grid">
          <div class="principle">
            <h3>원본 미저장</h3>
            <p>영상 원본은 서버에 남기지 않습니다. 해시 계산 후 임시 파일을 즉시 삭제합니다.</p>
          </div>
          <div class="principle">
            <h3>개인정보 최소화</h3>
            <p>CI는 HMAC-SHA256 해시만 보관합니다. 평문 CI는 어떤 경로로도 저장되지 않습니다.</p>
          </div>
          <div class="principle">
            <h3>등록과 발급의 분리</h3>
            <p>VC 발급이 실패해도 블록체인 등록은 유지됩니다. 나중에 재발급이 가능합니다.</p>
          </div>
          <div class="principle">
            <h3>동일 파일 중복 방어</h3>
            <p>파일 SHA-256 조회와 DB unique 제약으로 동일 파일의 중복 등록을 막습니다. 유사도만으로 등록 권리나 소유권을 판단하지 않습니다.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Closing CTA -->
    <section class="cta">
      <div class="cta-inner">
        <h2 class="cta-title">영상을 검증하거나 등록해 보세요</h2>
        <p class="cta-desc">
          검증은 로그인 없이 파일 업로드만으로 가능합니다.
          등록은 iOS 앱에서 본인확인을 마친 뒤 진행합니다.
        </p>
        <div class="hero-actions">
          <a href="/downloads" class="btn btn-primary">시작하기</a>
          <a href="/developers/guide/introduction" class="btn btn-secondary">개발자 문서</a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ─── Base ─── */
/* 공용 --jb-* 토큰은 custom.css의 :root/.dark에 있습니다. */
.home-page {
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
  /* word-break: keep-all은 custom.css에서 전역 적용 */
}

/* ─── Hero ─── */
.hero {
  background: linear-gradient(180deg, var(--jb-blue-light) 0%, var(--jb-bg) 100%);
  border-bottom: 1px solid var(--jb-border);
  padding: 80px 24px 72px;
  text-align: center;
}

.hero-inner {
  max-width: 680px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 100px;
  background: var(--jb-bg);
  border: 1px solid var(--jb-blue-border);
  color: var(--jb-blue);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.02em;
  margin-bottom: 24px;
}

.hero-title {
  font-size: 40px;
  font-weight: 700;
  line-height: 1.25;
  color: var(--jb-ink);
  margin: 0 0 20px;
  letter-spacing: -0.02em;
}

/* <br> 대신 절 단위 inline-block — 넓은 화면에선 절 사이에서 끊기고,
   좁은 화면에선 절 내부에서 자연스럽게 흐름 */
.hero-title span {
  display: inline-block;
}

.hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0 0 18px;
}

/* 면책 문구 — 본문과 동급으로 읽히면 안 되므로 작은 주석 카드로 분리 */
.hero-note {
  display: inline-block;
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--jb-text-secondary);
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 10px;
  padding: 10px 18px;
  margin: 0 0 32px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.hero-hint {
  font-size: 13px;
  color: var(--jb-text-secondary);
  margin: 16px 0 0;
}

/* ─── Buttons ─── */
.btn {
  display: inline-flex;
  align-items: center;
  padding: 12px 28px;
  border-radius: 10px;
  font-size: 15px;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.15s ease, border-color 0.15s ease,
    color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
}

.btn-primary {
  background: var(--jb-blue-solid);
  color: #fff;
}

.btn-primary:hover {
  background: var(--jb-blue-solid-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(36, 87, 230, 0.3);
}

.btn-secondary {
  background: var(--jb-bg);
  color: var(--jb-ink);
  border: 1px solid var(--jb-border);
}

.btn-secondary:hover {
  border-color: var(--jb-blue-border);
  color: var(--jb-blue);
}

/* ─── Section ─── */
.section {
  padding: 72px 24px;
}

.section-alt {
  background: var(--jb-bg-alt);
}

.section-inner {
  max-width: 960px;
  margin: 0 auto;
}

.section-label {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--jb-blue);
  margin-bottom: 8px;
}

.section-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 12px;
  letter-spacing: -0.01em;
}

.section-desc {
  font-size: 16px;
  color: var(--jb-text-secondary);
  margin: 0 0 32px;
  line-height: 1.6;
}

.section-desc code {
  background: var(--jb-blue-light);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 14px;
  color: var(--jb-blue);
}

/* ─── Proof Cards ─── */
.proof-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 32px;
}

.proof-card {
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 14px;
  padding: 28px;
}

.proof-icon {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.proof-card h3 {
  font-size: 18px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 6px;
}

.proof-question {
  font-size: 15px;
  color: var(--jb-blue);
  font-weight: 500;
  margin: 0 0 12px;
}

.proof-answer {
  font-size: 14px;
  line-height: 1.65;
  color: var(--jb-text-secondary);
  margin: 0 0 16px;
}

.proof-tech {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 6px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  font-size: 12px;
  font-weight: 600;
}

/* ─── Hash Flow ─── */
.hash-flow {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 32px;
  align-items: start;
}

.hash-step {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 12px;
  padding: 20px 24px;
}

.hash-step-result {
  border-color: var(--jb-blue-border);
  background: var(--jb-blue-light);
}

.hash-num {
  flex-shrink: 0;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  font-size: 14px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hash-num-dark {
  background: var(--jb-blue-solid);
  color: #fff;
}

.hash-step h3 {
  font-size: 15px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 4px;
  font-family: "SF Mono", "Fira Code", monospace;
}

.hash-step p {
  font-size: 14px;
  color: var(--jb-text-secondary);
  margin: 0;
  line-height: 1.55;
}

/* ─── Verification Pipeline ─── */
.pipeline {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 28px;
  /* stretch면 metric이 있는 2차 카드 높이에 1·3차가 끌려가 빈 공간이 생김 */
  align-items: start;
}

.pipeline-step {
  padding: 22px 20px;
  border: 1px solid var(--jb-border);
  border-radius: 14px;
  background: var(--jb-bg);
}

.pipeline-step-key {
  border-color: var(--jb-blue-border);
  background: var(--jb-blue-light);
}

.pipeline-stage {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.06em;
  padding: 3px 9px;
  border-radius: 999px;
  background: var(--jb-gray-bg);
  color: var(--jb-neutral-fg);
  margin-bottom: 12px;
}

.pipeline-stage-key {
  background: var(--jb-blue-solid);
  color: #fff;
}

.pipeline-step h3 {
  font-size: 16px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 8px;
}

.pipeline-step p {
  font-size: 13.5px;
  color: var(--jb-text-secondary);
  line-height: 1.65;
  margin: 0;
}

.pipeline-step p strong { color: var(--jb-ink); }

.pipeline-metrics {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-top: 14px;
}

/* 한글은 본문 폰트, 수치만 모노 — 한글이 모노 폴백을 타면 자간이 벌어짐 */
.metric {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 12px;
  font-weight: 600;
  color: var(--jb-blue);
  background: var(--jb-bg);
  border: 1px solid var(--jb-blue-border);
  border-radius: 6px;
  padding: 5px 9px;
}

.metric em {
  font-style: normal;
  font-weight: 500;
  color: var(--jb-text-secondary);
  white-space: nowrap;
}

.metric b {
  font-weight: 600;
  margin-left: auto;
}

.metric-num {
  font-family: "SF Mono", "Fira Code", monospace;
  font-variant-numeric: tabular-nums;
}

/* ─── Detection panel ─── */
.detect-panel {
  margin-top: 16px;
  padding: 24px;
  border: 1px solid var(--jb-border);
  border-radius: 14px;
  background: var(--jb-bg);
}

.detect-title {
  font-size: 15px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 16px;
}

.detect-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  list-style: none;
  padding: 0;
  margin: 0 0 18px;
}

.detect-list li {
  display: flex;
  flex-direction: column;
  gap: 3px;
  padding: 12px 14px;
  border-radius: 10px;
  background: var(--jb-bg-alt);
  border: 1px solid var(--jb-border);
}

.detect-list strong {
  font-size: 14px;
  font-weight: 600;
  color: var(--jb-ink);
}

.detect-list span {
  font-size: 13px;
  color: var(--jb-text-secondary);
  line-height: 1.55;
}

.detect-note {
  font-size: 13.5px;
  color: var(--jb-text-secondary);
  line-height: 1.7;
  margin: 0;
  padding-top: 16px;
  border-top: 1px solid var(--jb-border);
}

.detect-note strong { color: var(--jb-ink); }

/* ─── Verdict ─── */
/* auto-fill은 960px에서 3열이 되어 4번째 항목만 고아로 떨어짐 */
.verdict-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-top: 24px;
}

.verdict-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  border-radius: 10px;
  border: 1px solid var(--jb-border);
  background: var(--jb-bg);
}

.verdict-code {
  font-size: 12px;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 6px;
  white-space: nowrap;
  flex-shrink: 0;
  /* 폭을 고정해야 카드마다 설명 시작 위치가 맞음 */
  min-width: 76px;
  text-align: center;
}

.verdict-success .verdict-code {
  background: var(--jb-green-bg);
  color: var(--jb-green);
}

.verdict-neutral .verdict-code {
  background: var(--jb-gray-bg);
  color: var(--jb-neutral-fg);
}

.verdict-warn .verdict-code {
  background: var(--jb-yellow-bg);
  color: var(--jb-yellow);
}

.verdict-pending .verdict-code {
  background: var(--jb-blue-light);
  color: var(--jb-blue);
}

.verdict-desc {
  font-size: 14px;
  color: var(--jb-text);
}

.verdict-note {
  margin: 20px 0 0;
  padding: 16px 20px;
  /* 섹션이 section-alt가 되었으므로 bg-alt를 쓰면 배경에 묻힘 */
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 10px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
}

.verdict-note strong { color: var(--jb-ink); }

.verdict-note a {
  color: var(--jb-blue);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
  white-space: nowrap;
}

.verdict-note a::after {
  content: " →";
  text-decoration: none;
  display: inline-block;
}

.verdict-note a:hover {
  text-decoration-thickness: 2px;
}

/* ─── Channel Grid ─── */
.channel-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 32px;
}

.channel-card {
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 14px;
  padding: 24px;
}

/* "네 개의 접점, 하나의 백엔드" — 허브는 전폭으로 두어야 구조가 레이아웃으로 읽힘 */
.channel-card-primary {
  border-color: var(--jb-blue-border);
  background: var(--jb-blue-light);
  grid-column: 1 / -1;
  display: flex;
  align-items: flex-start;
  gap: 20px;
}

.channel-card-primary .channel-icon {
  flex-shrink: 0;
  margin-bottom: 0;
}

.channel-body {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.channel-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.channel-card-primary .channel-icon {
  background: var(--jb-blue-solid);
  color: #fff;
}

.channel-card h3 {
  font-size: 17px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 6px;
}

.channel-badge {
  display: inline-block;
  font-size: 12px;
  color: var(--jb-text-secondary);
  margin-bottom: 10px;
}

/* 아직 설치·응답이 안 되는 채널을 제목 옆에 표시 — Downloads 페이지와 어긋나지 않게 */
.channel-status {
  display: inline-block;
  vertical-align: middle;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.02em;
  padding: 3px 8px;
  border-radius: 999px;
  background: var(--jb-gray-bg);
  color: var(--jb-neutral-fg);
  white-space: nowrap;
}

/* 저장소명(영문)만 모노 — "카카오톡 채널"은 본문 폰트 유지 */
.channel-badge-code {
  font-family: "SF Mono", "Fira Code", monospace;
}

.channel-card p {
  font-size: 14px;
  color: var(--jb-text);
  margin: 0 0 12px;
  line-height: 1.6;
}

.channel-tech {
  font-size: 12px;
  color: var(--jb-text-secondary);
}

/* ─── Section CTA ─── */
.section-cta {
  margin: 24px 0 0;
  font-size: 14px;
}

.section-cta a {
  color: var(--jb-blue);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 3px;
  text-decoration-thickness: 1px;
}

.section-cta a::after {
  content: " →";
  text-decoration: none;
  display: inline-block;
}

.section-cta a:hover { text-decoration-thickness: 2px; }

/* ─── Link Cards ─── */
.links-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
  margin-top: 32px;
}

.link-card {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid var(--jb-border);
  background: var(--jb-bg);
  text-decoration: none;
  transition: background-color 0.15s ease, border-color 0.15s ease,
    color 0.15s ease, transform 0.15s ease, box-shadow 0.15s ease;
}

.link-card:hover {
  border-color: var(--jb-blue-border);
  box-shadow: 0 2px 8px rgba(36, 87, 230, 0.08);
  transform: translateY(-2px);
}

.link-card-icon {
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  display: flex;
  align-items: center;
  justify-content: center;
}

.link-card h3 {
  font-size: 15px;
  font-weight: 600;
  color: var(--jb-ink);
  margin: 0 0 4px;
}

.link-card p {
  font-size: 13px;
  color: var(--jb-text-secondary);
  margin: 0;
  line-height: 1.5;
}

/* ─── Principles ─── */
.principles-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-top: 32px;
}

.principle {
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 12px;
  padding: 24px;
}

.principle h3 {
  font-size: 15px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 8px;
}

.principle p {
  font-size: 14px;
  color: var(--jb-text-secondary);
  margin: 0;
  line-height: 1.6;
}

/* ─── Closing CTA ─── */
/* hero 그라디언트를 뒤집어 페이지를 양끝에서 닫아줌 */
.cta {
  background: linear-gradient(180deg, var(--jb-bg) 0%, var(--jb-blue-light) 100%);
  border-top: 1px solid var(--jb-border);
  padding: 72px 24px 80px;
  text-align: center;
}

.cta-inner {
  max-width: 680px;
  margin: 0 auto;
}

.cta-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 12px;
  letter-spacing: -0.01em;
}

.cta-desc {
  font-size: 16px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0 0 28px;
}

/* ─── Responsive ─── */
@media (max-width: 960px) {
  .pipeline,
  .hash-flow { grid-template-columns: 1fr; }
  .links-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .hero { padding: 56px 20px 48px; }
  .hero-title { font-size: 28px; }
  .hero-desc { font-size: 16px; }
  .section { padding: 48px 20px; }
  .section-title { font-size: 24px; }
  .cta { padding: 48px 20px 56px; }
  .cta-title { font-size: 24px; }
  .proof-grid,
  .channel-grid,
  .principles-grid,
  .pipeline,
  .hash-flow,
  .detect-list { grid-template-columns: 1fr; }
  .links-grid { grid-template-columns: 1fr; }
  .verdict-grid { grid-template-columns: 1fr; }
  /* 좁은 화면에선 허브 카드도 다른 카드와 같은 세로 배치로 */
  .channel-card-primary { flex-direction: column; gap: 0; }
  .channel-card-primary .channel-icon { margin-bottom: 14px; }
}
</style>
