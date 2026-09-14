---
layout: page
---

<div class="vs-page">
  <section class="vs-hero">
    <div class="vs-hero-inner">
      <span class="vs-label">Verification Status</span>
      <h1 class="vs-hero-title">영상 검증 상태</h1>
      <p class="vs-hero-desc">진본은 제출 영상을 "진짜/가짜"로 단정하지 않습니다.<br>등록 원본과의 관계를 확인하고, 콘텐츠 일치 정도를 판단합니다.</p>
    </div>
  </section>
  <section class="vs-section">
    <div class="vs-inner">
      <span class="vs-label">Three States</span>
      <h2 class="vs-section-title">사용자에게 표시하는 세 가지 상태</h2>
      <div class="vs-status-grid">
        <div class="vs-status-card vs-authentic">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          </div>
          <span class="vs-chip vs-chip-green">진본</span>
          <h3>원본과 같은 콘텐츠</h3>
          <p>원본 전체 또는 특정 구간이 영상·음성·시간 순서 검증을 통과</p>
        </div>
        <div class="vs-status-card vs-similar">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          </div>
          <span class="vs-chip vs-chip-yellow">콘텐츠 유사</span>
          <h3>원본 후보를 찾음</h3>
          <p>등록 원본과 연결되지만, 전체 무변조를 확정하지 못함</p>
        </div>
        <div class="vs-status-card vs-unverified">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>
          </div>
          <span class="vs-chip vs-chip-red">미인증</span>
          <h3>진본 승인 불가</h3>
          <p>등록 원본이 없거나 음성·얼굴·자막·장면 변경이 확인됨</p>
        </div>
      </div>
      <div class="vs-note">등록 기록과 콘텐츠 판정은 별개입니다. 콘텐츠가 변경되어도 유효한 VC가 있으면 등록자 정보는 표시할 수 있습니다.</div>
    </div>
  </section>
  <section class="vs-section vs-section-alt">
    <div class="vs-inner">
      <span class="vs-label">Decision Flow</span>
      <h2 class="vs-section-title">상태가 결정되는 흐름</h2>
      <div class="vs-flow">
        <div class="vs-flow-step">
          <div class="vs-flow-num">1</div>
          <h4>원본 검색</h4>
          <p>fineHash·pHash로 등록 원본 후보를 찾습니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-red">후보 없음 → 미인증</span>
          </div>
        </div>
        <div class="vs-flow-connector">
          <div class="vs-flow-line"></div>
          <svg class="vs-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
        <div class="vs-flow-step">
          <div class="vs-flow-num">2</div>
          <h4>등록 증거 검증</h4>
          <p>블록체인 기록·VC·서명 무결성을 확인합니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-red">증거 불충분 → 미인증</span>
          </div>
        </div>
        <div class="vs-flow-connector">
          <div class="vs-flow-line"></div>
          <svg class="vs-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
        <div class="vs-flow-step">
          <div class="vs-flow-num">3</div>
          <h4>콘텐츠 비교</h4>
          <p>원본 후보와 음성 지문을 비교합니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-green">모두 일치 → 진본</span>
            <span class="vs-branch vs-branch-yellow">일부 일치 → 콘텐츠 유사</span>
            <span class="vs-branch vs-branch-red">변경 확인 → 미인증</span>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section class="vs-section">
    <div class="vs-inner">
      <span class="vs-label">Examples</span>
      <h2 class="vs-section-title">대표 사례</h2>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-green">
          <span class="vs-chip vs-chip-green">진본</span>
          <span>원본과 같은 콘텐츠</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">등록 파일 그대로 제출</div>
          <div class="vs-case-detail">파일 SHA-256 일치 → 등록자·등록 시각 표시</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">YouTube 재인코딩·해상도 변경</div>
          <div class="vs-case-detail">영상·음성·시간 순서 일치 → 등록자·등록 시각 표시</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-green">
          <span class="vs-chip vs-chip-green">진본</span>
          <span>원본 구간 인증</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">긴 원본에서 30초를 잘라낸 쇼츠</div>
          <div class="vs-case-detail">영상·음성·시간 순서가 모두 일치하면 진본. 원본 구간과 타임코드 표시</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-yellow">
          <span class="vs-chip vs-chip-yellow">콘텐츠 유사</span>
          <span>원본과 일부 연결</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">자막·로고만 추가된 영상</div>
          <div class="vs-case-detail">오버레이 영역과 원본 트랙 분리 검증. 정책상 진본 승격 가능</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">오디오 트랙이 없는 영상</div>
          <div class="vs-case-detail">음성 비교 불가. 진본으로 자동 승인하지 않음</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-red">
          <span class="vs-chip vs-chip-red">미인증</span>
          <span>변경이 확인된 콘텐츠</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">영상은 같고 음성만 교체</div>
          <div class="vs-case-detail">음성 구간 원본과 불일치. 등록 증명과 판정을 구분 표시</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">얼굴·입모양을 변경 (딥페이크)</div>
          <div class="vs-case-detail">국소 영상 불일치. 제출 영상은 진본으로 승인하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">여러 원본을 이어 붙이거나 장면 삽입</div>
          <div class="vs-case-detail">구간 순서·대응하지 않는 장면을 확인. 제출 영상은 진본으로 승인하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">등록 원본을 찾지 못함</div>
          <div class="vs-case-detail">미등록 = 가짜라는 뜻은 아님. 검증된 VC는 노출하지 않음</div>
        </div>
      </div>
    </div>
  </section>
</div>

<style>
.vs-page {
  --vs-blue: #2457E6;
  --vs-blue-light: #EEF4FF;
  --vs-blue-border: #C3D3FC;
  --vs-ink: #111827;
  --vs-text: #374151;
  --vs-text-2: #6B7280;
  --vs-text-3: #9CA3AF;
  --vs-border: #E5E7EB;
  --vs-bg: #FFFFFF;
  --vs-bg-alt: #F9FAFB;
  --vs-green: #059669;
  --vs-green-bg: #ECFDF5;
  --vs-green-border: #A7F3D0;
  --vs-yellow: #D97706;
  --vs-yellow-bg: #FFFBEB;
  --vs-yellow-border: #FDE68A;
  --vs-red: #DC2626;
  --vs-red-bg: #FEF2F2;
  --vs-red-border: #FECACA;
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
}
.dark .vs-page {
  --vs-ink: #F9FAFB;
  --vs-text: #D1D5DB;
  --vs-text-2: #9CA3AF;
  --vs-text-3: #6B7280;
  --vs-border: #374151;
  --vs-bg: #111827;
  --vs-bg-alt: #1F2937;
  --vs-blue-light: #1E293B;
  --vs-blue-border: #334155;
  --vs-green-bg: #064E3B;
  --vs-green-border: #065F46;
  --vs-yellow-bg: #78350F;
  --vs-yellow-border: #92400E;
  --vs-red-bg: #450A0A;
  --vs-red-border: #7F1D1D;
}
.vs-hero {
  background: linear-gradient(180deg, var(--vs-blue-light) 0%, var(--vs-bg) 100%);
  border-bottom: 1px solid var(--vs-border);
  padding: 80px 24px 64px;
  text-align: center;
}
.vs-hero-inner { max-width: 680px; margin: 0 auto; }
.vs-label {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--vs-blue);
  margin-bottom: 12px;
}
.vs-hero-title {
  font-size: 40px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0 0 20px;
  letter-spacing: -0.02em;
  line-height: 1.25;
}
.vs-hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--vs-text-2);
  margin: 0;
}
.vs-section { padding: 72px 24px; }
.vs-section-alt { background: var(--vs-bg-alt); border-top: 1px solid var(--vs-border); border-bottom: 1px solid var(--vs-border); }
.vs-inner { max-width: 880px; margin: 0 auto; }
.vs-section-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0 0 36px;
  letter-spacing: -0.01em;
}
.vs-note {
  margin-top: 28px;
  padding: 16px 20px;
  background: var(--vs-bg-alt);
  border: 1px solid var(--vs-border);
  border-radius: 10px;
  font-size: 14px;
  color: var(--vs-text-2);
  line-height: 1.7;
}
.vs-section-alt .vs-note { background: var(--vs-bg); }
.vs-status-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.vs-status-card {
  background: var(--vs-bg);
  border: 1px solid var(--vs-border);
  border-radius: 16px;
  padding: 28px 24px;
  text-align: center;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.vs-status-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
.vs-authentic:hover { border-color: var(--vs-green-border); }
.vs-similar:hover { border-color: var(--vs-yellow-border); }
.vs-unverified:hover { border-color: var(--vs-red-border); }
.vs-status-icon {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}
.vs-authentic .vs-status-icon { background: var(--vs-green-bg); color: var(--vs-green); }
.vs-similar .vs-status-icon { background: var(--vs-yellow-bg); color: var(--vs-yellow); }
.vs-unverified .vs-status-icon { background: var(--vs-red-bg); color: var(--vs-red); }
.vs-chip {
  display: inline-flex;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  margin-bottom: 10px;
}
.vs-chip-green { color: #18794e; background: #dcfce7; }
.vs-chip-yellow { color: #9a6700; background: #fef3c7; }
.vs-chip-red { color: #b42318; background: #fee4e2; }
.dark .vs-chip-green { color: #4ade80; background: #064E3B; }
.dark .vs-chip-yellow { color: #fbbf24; background: #78350F; }
.dark .vs-chip-red { color: #f87171; background: #450A0A; }
.vs-status-card h3 {
  font-size: 17px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0 0 8px;
}
.vs-status-card p {
  font-size: 14px;
  color: var(--vs-text-2);
  line-height: 1.6;
  margin: 0;
}
.vs-flow {
  display: flex;
  align-items: flex-start;
  gap: 0;
}
.vs-flow-step {
  flex: 1;
  text-align: center;
  padding: 0 12px;
}
.vs-flow-num {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--vs-blue);
  color: #fff;
  font-size: 17px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}
.vs-flow-step h4 {
  font-size: 16px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0 0 6px;
}
.vs-flow-step > p {
  font-size: 13px;
  color: var(--vs-text-2);
  margin: 0 0 12px;
  line-height: 1.6;
}
.vs-flow-branch {
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: center;
}
.vs-branch {
  display: inline-flex;
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 11px;
  font-weight: 600;
}
.vs-branch-green { color: #18794e; background: #dcfce7; }
.vs-branch-yellow { color: #9a6700; background: #fef3c7; }
.vs-branch-red { color: #b42318; background: #fee4e2; }
.dark .vs-branch-green { color: #4ade80; background: #064E3B; }
.dark .vs-branch-yellow { color: #fbbf24; background: #78350F; }
.dark .vs-branch-red { color: #f87171; background: #450A0A; }
.vs-flow-connector {
  display: flex;
  align-items: center;
  margin-top: 14px;
  flex-shrink: 0;
}
.vs-flow-line { width: 20px; height: 2px; background: var(--vs-border); }
.vs-flow-chevron { color: var(--vs-text-3); flex-shrink: 0; }
.vs-case-group {
  background: var(--vs-bg);
  border: 1px solid var(--vs-border);
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 16px;
}
.vs-case-group:last-child { margin-bottom: 0; }
.vs-case-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 24px;
  font-size: 15px;
  font-weight: 700;
  color: var(--vs-ink);
  border-bottom: 1px solid var(--vs-border);
}
.vs-case-header-green { background: var(--vs-green-bg); }
.vs-case-header-yellow { background: var(--vs-yellow-bg); }
.vs-case-header-red { background: var(--vs-red-bg); }
.vs-case-item {
  display: flex;
  align-items: baseline;
  gap: 16px;
  padding: 14px 24px;
  border-bottom: 1px solid var(--vs-border);
}
.vs-case-item:last-child { border-bottom: none; }
.vs-case-scenario {
  flex: 0 0 auto;
  min-width: 200px;
  font-size: 14px;
  font-weight: 600;
  color: var(--vs-ink);
}
.vs-case-detail {
  font-size: 13px;
  color: var(--vs-text-2);
  line-height: 1.6;
}
@media (max-width: 768px) {
  .vs-hero { padding: 56px 20px 48px; }
  .vs-hero-title { font-size: 28px; }
  .vs-hero-desc { font-size: 16px; }
  .vs-section { padding: 48px 20px; }
  .vs-section-title { font-size: 24px; margin-bottom: 28px; }
  .vs-status-grid { grid-template-columns: 1fr; }
  .vs-flow { flex-direction: column; align-items: center; gap: 8px; }
  .vs-flow-connector { transform: rotate(90deg); }
  .vs-case-item { flex-direction: column; gap: 4px; }
  .vs-case-scenario { min-width: 0; }
}
</style>
