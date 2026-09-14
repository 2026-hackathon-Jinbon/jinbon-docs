<template>
  <div class="use-cases-page">
    <!-- Hero -->
    <section class="uc-hero">
      <div class="uc-hero-inner">
        <span class="uc-label">Use Cases</span>
        <h1 class="uc-hero-title">누가 진본을 사용하나요?</h1>
        <p class="uc-hero-desc">
          영상의 진위가 중요한 모든 곳에서 진본이 신뢰를 만듭니다.
        </p>
      </div>
    </section>

    <!-- Cases -->
    <section class="uc-section">
      <div class="uc-inner">
        <div class="uc-case">
          <div class="uc-case-icon">
            <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/></svg>
          </div>
          <div class="uc-case-content">
            <h2>언론사 · 팩트체크 기관</h2>
            <p class="uc-case-problem">딥페이크와 편집 영상이 범람하는 환경에서, 보도에 사용하는 영상이 원본 그대로인지 확인하기 어렵습니다.</p>
            <div class="uc-case-solution">
              <h4>진본으로 해결</h4>
              <ul>
                <li>취재원이 촬영 즉시 진본 앱으로 영상을 등록하면 블록체인에 지문이 기록됩니다.</li>
                <li>편집국은 웹이나 Chrome 확장으로 <strong>수신 영상이 등록된 원본과 일치하는지</strong> 즉시 검증합니다.</li>
                <li>VC 보증서로 <strong>누가 언제 등록했는지</strong>까지 확인할 수 있어 출처 추적이 가능합니다.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="uc-case">
          <div class="uc-case-icon">
            <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2" ry="2"/></svg>
          </div>
          <div class="uc-case-content">
            <h2>영상 제작자 · 크리에이터</h2>
            <p class="uc-case-problem">자신이 만든 콘텐츠가 무단 복제·재편집되어도, 원본 소유를 입증할 객관적인 방법이 없습니다.</p>
            <div class="uc-case-solution">
              <h4>진본으로 해결</h4>
              <ul>
                <li>영상 업로드 전에 진본 앱으로 등록하면, <strong>등록 시점과 등록자가 블록체인에 기록</strong>됩니다.</li>
                <li>제3자가 같은 영상을 올리더라도 진본 검증을 통해 <strong>먼저 등록한 원본 소유자</strong>를 확인할 수 있습니다.</li>
                <li>재인코딩이나 리사이즈를 거쳐도 지각해시로 <strong>같은 콘텐츠임을 탐지</strong>합니다.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="uc-case">
          <div class="uc-case-icon">
            <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <div class="uc-case-content">
            <h2>기업 · 법적 증거</h2>
            <p class="uc-case-problem">CCTV, 회의 녹화, 현장 기록 영상이 법적 분쟁에서 증거로 채택되려면 변조되지 않았음을 입증해야 합니다.</p>
            <div class="uc-case-solution">
              <h4>진본으로 해결</h4>
              <ul>
                <li>녹화 직후 진본에 등록하면 <strong>해시가 블록체인에 불변 기록</strong>됩니다.</li>
                <li>분쟁 시 영상 파일을 검증하면, 등록 당시의 파일과 <strong>바이트 단위로 동일한지</strong> 즉시 확인됩니다.</li>
                <li>DID 기반 본인확인으로 <strong>등록자의 신원까지 보증</strong>되어 증거 능력을 높입니다.</li>
              </ul>
            </div>
          </div>
        </div>

        <div class="uc-case">
          <div class="uc-case-icon">
            <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <div class="uc-case-content">
            <h2>플랫폼 · 소셜 미디어</h2>
            <p class="uc-case-problem">사용자가 업로드하는 영상의 출처와 진위를 플랫폼이 직접 판별하기 어렵습니다.</p>
            <div class="uc-case-solution">
              <h4>진본으로 해결</h4>
              <ul>
                <li>진본 API를 연동하면 업로드 시점에 <strong>자동으로 등록 여부를 확인</strong>할 수 있습니다.</li>
                <li>진본 인증 배지를 표시해 시청자에게 <strong>영상의 신뢰도를 시각적으로 전달</strong>합니다.</li>
                <li>Chrome 확장으로 YouTube, Instagram 영상을 <strong>시청 중 바로 검증</strong>하거나, 카카오톡 챗봇으로 URL을 보내 <strong>간편하게 검증</strong>할 수 있습니다.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="uc-cta">
      <div class="uc-inner">
        <h2>진본을 시작하세요</h2>
        <p>영상의 진위가 중요한 곳이라면 어디든 진본이 함께합니다.</p>
        <div class="uc-cta-actions">
          <a href="/downloads" class="btn btn-primary">다운로드</a>
          <a href="/developers/guide/introduction" class="btn btn-secondary">개발자 센터</a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.use-cases-page {
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
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
}

.dark .use-cases-page {
  --jb-ink: #F9FAFB;
  --jb-text: #D1D5DB;
  --jb-text-secondary: #9CA3AF;
  --jb-border: #374151;
  --jb-bg: #111827;
  --jb-bg-alt: #1F2937;
  --jb-blue-light: #1E293B;
  --jb-blue-border: #334155;
  --jb-green-bg: #064E3B;
}

.uc-hero {
  background: linear-gradient(180deg, var(--jb-blue-light) 0%, var(--jb-bg) 100%);
  border-bottom: 1px solid var(--jb-border);
  padding: 72px 24px 56px;
  text-align: center;
}

.uc-hero-inner { max-width: 640px; margin: 0 auto; }

.uc-label {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--jb-blue);
  margin-bottom: 12px;
}

.uc-hero-title {
  font-size: 36px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 16px;
  letter-spacing: -0.02em;
}

.uc-hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0;
}

.uc-section { padding: 64px 24px; }
.uc-inner { max-width: 800px; margin: 0 auto; }

.uc-case {
  display: flex;
  gap: 24px;
  padding: 36px 0;
  border-bottom: 1px solid var(--jb-border);
}

.uc-case:last-child { border-bottom: none; }

.uc-case-icon {
  flex-shrink: 0;
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  display: flex;
  align-items: center;
  justify-content: center;
}

.uc-case-content h2 {
  font-size: 22px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 10px;
}

.uc-case-problem {
  font-size: 15px;
  color: var(--jb-text-secondary);
  line-height: 1.65;
  margin: 0 0 16px;
}

.uc-case-solution {
  background: var(--jb-bg-alt);
  border: 1px solid var(--jb-border);
  border-radius: 12px;
  padding: 20px 24px;
}

.uc-case-solution h4 {
  font-size: 14px;
  font-weight: 700;
  color: var(--jb-blue);
  margin: 0 0 10px;
}

.uc-case-solution ul {
  margin: 0;
  padding-left: 20px;
}

.uc-case-solution li {
  font-size: 14px;
  color: var(--jb-text);
  line-height: 1.7;
  margin-bottom: 6px;
}

.uc-case-solution li:last-child { margin-bottom: 0; }

.uc-cta {
  background: var(--jb-blue-light);
  border-top: 1px solid var(--jb-border);
  padding: 56px 24px;
  text-align: center;
}

.uc-cta h2 {
  font-size: 28px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 8px;
}

.uc-cta p {
  font-size: 16px;
  color: var(--jb-text-secondary);
  margin: 0 0 28px;
}

.uc-cta-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
}

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

@media (max-width: 768px) {
  .uc-hero { padding: 48px 20px 40px; }
  .uc-hero-title { font-size: 28px; }
  .uc-section { padding: 40px 20px; }
  .uc-case { flex-direction: column; gap: 16px; }
}
</style>
