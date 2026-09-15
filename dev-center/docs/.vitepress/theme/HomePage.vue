<template>
  <div class="home-page">
    <!-- Hero -->
    <section class="hero">
      <div class="hero-inner">
        <span class="hero-badge">Blockchain Video Verification</span>
        <h1 class="hero-title">
          등록 영상과 일치하는지,<br />누가 언제 등록했는지 확인하세요.
        </h1>
        <p class="hero-desc">
          진본은 영상의 디지털 지문을 블록체인에 기록하고,
          제출 영상과의 관계 및 누가 언제 등록했는지를 확인하는 서비스입니다.
        </p>
        <p class="hero-desc">영상 속 사건의 사실성, AI 생성 여부, 제작자·저작권자 여부는 보증하지 않습니다.</p>
        <div class="hero-actions">
          <a href="/use-cases" class="btn btn-primary">사용 사례 보기</a>
          <a href="/downloads" class="btn btn-secondary">시작하기</a>
        </div>
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
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h3>영상 비교</h3>
            <p class="proof-question">등록 파일 또는 등록 지문과 얼마나 일치하는가?</p>
            <p class="proof-answer">파일 해시로 정확한 일치를 확인하고, 파일이 다르면 영상·음성 지문으로 유사도를 비교합니다. 블록체인의 등록 기록도 별도로 확인합니다.</p>
            <span class="proof-tech">OmniOne Chain</span>
          </div>
          <div class="proof-card">
            <div class="proof-icon">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
            </div>
            <h3>등록 사실 확인</h3>
            <p class="proof-question">누가 언제 등록했는가?</p>
            <p class="proof-answer">모바일 신분증으로 본인확인을 마친 등록자가 DID 기반 보증서(VC)를 발급받아, 등록 사실을 제3자에게 증명할 수 있습니다.</p>
            <span class="proof-tech">Open DID + OmniOne CX</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Hash -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">Core Technology</span>
        <h2 class="section-title">두 종류의 해시, 하나의 지문</h2>
        <div class="hash-flow">
          <div class="hash-step">
            <div class="hash-num">1</div>
            <div>
              <h4>fineHash</h4>
              <p>파일 전체의 SHA-256.<br/>바이트 단위로 동일한 원본인지 확인합니다.</p>
            </div>
          </div>
          <div class="hash-step">
            <div class="hash-num">2</div>
            <div>
              <h4>perceptualHash</h4>
              <p>프레임별 DCT 기반 지각해시.<br/>재인코딩·리사이즈된 영상의 유사 후보를 찾습니다.</p>
            </div>
          </div>
          <div class="hash-step hash-step-result">
            <div class="hash-num hash-num-dark">3</div>
            <div>
              <h4>merkleRoot</h4>
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
        <p class="section-desc">파일이 다르면 지각해시로 유사 후보를 찾고, <strong>1초 간격의 대표 프레임과 음성 지문</strong>을 비교합니다. 이는 샘플 기반 유사도 평가이며 전체 영상의 무변조를 확정하는 검사는 아닙니다.</p>
        <div class="pipeline">
          <div class="pipeline-step">
            <span class="pipeline-stage">1차</span>
            <h4>후보 선별</h4>
            <p>파일 해시가 같으면 파일 일치를 확인하고 등록 증거 검증으로 넘어갑니다. 다르면 16프레임 지각해시로 후보를 찾습니다.</p>
          </div>
          <div class="pipeline-step pipeline-step-key">
            <span class="pipeline-stage pipeline-stage-key">2차</span>
            <h4>구간 대조</h4>
            <p>영상·음성 지문을 각각 일정한 시간 간격으로 맞춰보며 <strong>대응 비율</strong>을 계산합니다.</p>
            <div class="pipeline-metrics">
              <span class="metric"><em>영상</em> 커버리지 ≥ 95%</span>
              <span class="metric"><em>음성</em> 커버리지 ≥ 90%</span>
              <span class="metric"><em>방식</em> 일정한 시간 간격으로 대조</span>
            </div>
          </div>
          <div class="pipeline-step">
            <span class="pipeline-stage">3차</span>
            <h4>등록 증거</h4>
            <p>서명을 재계산해 DB와 온체인 양쪽에 대조하고, VC 보증서가 등록 당시 정보와 결속됐는지 확인합니다.</p>
          </div>
        </div>
        <div class="detect-panel">
          <h4 class="detect-title">비교에서 차이가 나타날 수 있는 사례</h4>
          <ul class="detect-list">
            <li><strong>음성만 교체</strong><span>음성 지문의 대응 비율이 낮아질 수 있습니다</span></li>
            <li><strong>얼굴·입모양 변경</strong><span>대표 프레임에 변화가 반영되면 차이가 나타날 수 있습니다</span></li>
            <li><strong>장면 삽입</strong><span>대응하지 않는 샘플 구간을 표시합니다. 삽입 여부를 확정하지는 않습니다</span></li>
            <li><strong>구간 순서 바꾸기</strong><span>같은 시간 간격으로 맞지 않는 구간은 대응 비율을 낮출 수 있습니다</span></li>
          </ul>
          <p class="detect-note"><strong>재인코딩본이나 연속 쇼츠</strong>도 후보 검색·비교 기준·등록 증거 검증을 통과하면 승인될 수 있습니다. 짧은 편집, 작은 화면 변화, 일부 음성 교체는 놓칠 수 있으며, 일부 구간의 대응이 전체 맥락을 보증하지는 않습니다.</p>
        </div>
      </div>
    </section>

    <!-- Verdict -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">Verification</span>
        <h2 class="section-title">검증 결과</h2>
        <p class="section-desc">등록 기록과 콘텐츠 상태를 함께 확인해 네 가지로 표시합니다.</p>
        <div class="verdict-grid">
          <div class="verdict-item verdict-success">
            <span class="verdict-code">진본</span>
            <span class="verdict-desc">파일 일치 또는 유사도 기준을 충족하고, 등록 증거도 유효함</span>
          </div>
          <div class="verdict-item verdict-warn">
            <span class="verdict-code">콘텐츠 유사</span>
            <span class="verdict-desc">등록 후보는 찾았지만 유사도 승인 기준 미달 또는 비교 정보 부족</span>
          </div>
          <div class="verdict-item verdict-neutral">
            <span class="verdict-code">미인증</span>
            <span class="verdict-desc">등록 원본이 없거나 보증서가 유효하지 않음</span>
          </div>
          <div class="verdict-item verdict-pending">
            <span class="verdict-code">확인 중</span>
            <span class="verdict-desc">외부 장애 또는 등록 기록 검증 실패 &mdash; 상세 사유 확인 필요</span>
          </div>
        </div>
        <p class="verdict-note">진본 배지는 <strong>콘텐츠 비교와 등록 증거 검증을 모두 통과</strong>했다는 뜻입니다. 파일 정확 일치와 유사도 기준 통과는 보증 수준이 다릅니다. <a href="/verification-status">판정별 의미와 한계 보기</a></p>
      </div>
    </section>

    <!-- System -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">System</span>
        <h2 class="section-title">네 개의 접점, 하나의 백엔드</h2>
        <div class="channel-grid">
          <div class="channel-card">
            <div class="channel-icon">
              <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            </div>
            <h3>iOS 앱</h3>
            <span class="channel-badge">jinbon-ios</span>
            <p>회원가입, DID/Wallet 관리, <strong>영상 등록</strong>, VC 보증서 보관</p>
            <span class="channel-tech">Swift &middot; UIKit &middot; DIDWalletSDK</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <h3>검증 웹</h3>
            <span class="channel-badge">jinbon-web</span>
            <p>파일 업로드로 영상 검증. <strong>로그인 불필요.</strong></p>
            <span class="channel-tech">Next.js 16 &middot; React 19 &middot; Tailwind CSS</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <h3>Chrome 확장</h3>
            <span class="channel-badge">jinbon-extension</span>
            <p>YouTube, Instagram 시청 중 <strong>자동 검증.</strong> 검증 기준을 통과한 영상엔 진본 배지.</p>
            <span class="channel-tech">Manifest V3 &middot; JavaScript</span>
          </div>
          <div class="channel-card">
            <div class="channel-icon">
              <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <h3>카카오톡 챗봇</h3>
            <span class="channel-badge">카카오톡 채널</span>
            <p>카카오톡 대화창에서 영상 URL을 보내면 <strong>즉시 검증 결과를 응답.</strong></p>
            <span class="channel-tech">카카오톡 채널 &middot; 챗봇</span>
          </div>
          <div class="channel-card channel-card-primary">
            <div class="channel-icon">
              <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
            </div>
            <h3>백엔드 API</h3>
            <span class="channel-badge">jinbon-backend</span>
            <p>등록, 검증, 인증의 <strong>중심 허브.</strong> 19개 REST 엔드포인트.</p>
            <span class="channel-tech">Java 21 &middot; Spring Boot &middot; PostgreSQL &middot; Redis</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick links -->
    <section class="section">
      <div class="section-inner">
        <span class="section-label">Documentation</span>
        <h2 class="section-title">문서 바로가기</h2>
        <div class="links-grid">
          <a href="/developers/architecture/overview" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            </div>
            <div>
              <h4>시스템 아키텍처</h4>
              <p>전체 구성도, 계층별 책임, 포트 맵, 데이터 흐름</p>
            </div>
          </a>
          <a href="/developers/api/conventions" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
            </div>
            <div>
              <h4>API 레퍼런스</h4>
              <p>19개 엔드포인트, 요청/응답 예시, 에러 코드</p>
            </div>
          </a>
          <a href="/developers/flows/video-register" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </div>
            <div>
              <h4>핵심 플로우</h4>
              <p>영상 등록, 검증, 가입/로그인, VC 발급 시퀀스</p>
            </div>
          </a>
          <a href="/developers/data/model" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>
            </div>
            <div>
              <h4>데이터 모델</h4>
              <p>DB 스키마, 스마트 컨트랙트, Redis 키 구조</p>
            </div>
          </a>
          <a href="/developers/security/overview" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            </div>
            <div>
              <h4>보안</h4>
              <p>CI 보호, SSRF 방어, 인증 정책, 키 관리</p>
            </div>
          </a>
          <a href="/developers/guide/concepts" class="link-card">
            <div class="link-card-icon">
              <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            </div>
            <div>
              <h4>핵심 개념</h4>
              <p>용어 정리, 설계 원칙, 장애 격리 정책</p>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- Design principles -->
    <section class="section section-alt">
      <div class="section-inner">
        <span class="section-label">Principles</span>
        <h2 class="section-title">설계 원칙</h2>
        <div class="principles-grid">
          <div class="principle">
            <h4>원본 미저장</h4>
            <p>영상 원본은 서버에 남기지 않습니다. 해시 계산 후 임시 파일을 즉시 삭제합니다.</p>
          </div>
          <div class="principle">
            <h4>개인정보 최소화</h4>
            <p>CI는 HMAC-SHA256 해시만 보관합니다. 평문 CI는 어떤 경로로도 저장되지 않습니다.</p>
          </div>
          <div class="principle">
            <h4>등록과 발급의 분리</h4>
            <p>VC 발급이 실패해도 블록체인 등록은 유지됩니다. 나중에 재발급이 가능합니다.</p>
          </div>
          <div class="principle">
            <h4>동일 파일 중복 방어</h4>
            <p>파일 SHA-256 조회와 DB unique 제약으로 동일 파일의 중복 등록을 막습니다. 유사도만으로 등록 권리나 소유권을 판단하지 않습니다.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ─── Base ─── */
.home-page {
  --jb-blue: #2457E6;
  --jb-blue-light: #EEF4FF;
  --jb-blue-border: #C3D3FC;
  --jb-ink: #111827;
  --jb-text: #374151;
  --jb-text-secondary: #6B7280;
  --jb-border: #E5E7EB;
  --jb-bg: #FFFFFF;
  --jb-bg-alt: #F9FAFB;
  --jb-green: #059669;
  --jb-green-bg: #ECFDF5;
  --jb-yellow: #D97706;
  --jb-yellow-bg: #FFFBEB;
  --jb-gray-bg: #F3F4F6;
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
}

.dark .home-page {
  --jb-ink: #F9FAFB;
  --jb-text: #D1D5DB;
  --jb-text-secondary: #9CA3AF;
  --jb-border: #374151;
  --jb-bg: #111827;
  --jb-bg-alt: #1F2937;
  --jb-blue-light: #1E293B;
  --jb-blue-border: #334155;
  --jb-green-bg: #064E3B;
  --jb-yellow-bg: #78350F;
  --jb-gray-bg: #1F2937;
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

.hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0 0 36px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
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
  transition: all 0.15s ease;
}

.btn-primary {
  background: var(--jb-blue);
  color: #fff;
}

.btn-primary:hover {
  background: #1a45c4;
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
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 32px;
  max-width: 560px;
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
  background: var(--jb-blue);
  color: #fff;
}

.hash-step h4 {
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
  color: var(--jb-text-secondary);
  margin-bottom: 12px;
}

.pipeline-stage-key {
  background: var(--jb-blue);
  color: #fff;
}

.pipeline-step h4 {
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

.metric {
  font-family: "SF Mono", "Fira Code", monospace;
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
  color: var(--jb-text-secondary);
  margin-right: 6px;
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
.verdict-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
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
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  white-space: nowrap;
  flex-shrink: 0;
}

.verdict-success .verdict-code {
  background: var(--jb-green-bg);
  color: var(--jb-green);
}

.verdict-neutral .verdict-code {
  background: var(--jb-gray-bg);
  color: var(--jb-text-secondary);
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
  background: var(--jb-bg-alt);
  border: 1px solid var(--jb-border);
  border-radius: 10px;
  font-size: 14px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
}

.verdict-note strong { color: var(--jb-ink); }

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

.channel-card-primary {
  border-color: var(--jb-blue-border);
  background: var(--jb-blue-light);
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
  background: var(--jb-blue);
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
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 12px;
  color: var(--jb-text-secondary);
  margin-bottom: 10px;
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
  transition: all 0.15s ease;
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

.link-card h4 {
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

.principle h4 {
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

/* ─── Responsive ─── */
@media (max-width: 960px) {
  .pipeline { grid-template-columns: 1fr; }
  .links-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .hero { padding: 56px 20px 48px; }
  .hero-title { font-size: 28px; }
  .hero-desc { font-size: 16px; }
  .section { padding: 48px 20px; }
  .section-title { font-size: 24px; }
  .proof-grid,
  .channel-grid,
  .principles-grid,
  .pipeline,
  .detect-list { grid-template-columns: 1fr; }
  .links-grid { grid-template-columns: 1fr; }
  .verdict-grid { grid-template-columns: 1fr; }
}
</style>
