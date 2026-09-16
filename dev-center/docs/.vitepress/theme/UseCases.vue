<template>
  <div class="use-cases-page">
    <!-- Hero -->
    <section class="uc-hero">
      <div class="uc-hero-inner">
        <span class="uc-label">Use Cases</span>
        <h1 class="uc-hero-title"><span>영상의 진위가 중요한</span> <span>모든 순간에</span></h1>
        <p class="uc-hero-desc">
          <span>딥페이크, 무단 복제, 조작 영상이 늘어나는 시대.</span>
          <span>진본은 등록 영상과의 관계, 등록자와 등록 시점을 확인합니다.</span>
        </p>
      </div>
    </section>

    <section class="uc-section">
      <div class="uc-inner">
        <h2 class="uc-section-title">검증 결과가 의미하는 것</h2>
        <p>사전에 등록된 영상과 비교한 결과와 등록 증거를 제공합니다. 등록 이전의 편집과 영상 속 사건의 사실성 및 AI 생성 여부 그리고 제작자와 저작권자 여부는 보증하지 않습니다. 등록 시각은 촬영 시각과 다릅니다.</p>
        <p>파일 정확 일치와 유사도 기준 통과는 구분해서 해석해야 합니다. <a href="/verification-status">검증 상태와 한계 보기</a></p>
      </div>
    </section>

    <!-- Stats -->
    <section class="uc-stats">
      <div class="uc-stats-inner">
        <div class="uc-stat">
          <span class="uc-stat-number">4</span>
          <span class="uc-stat-unit">개 채널</span>
          <span class="uc-stat-desc">앱과 웹 및 확장과 카카오톡</span>
        </div>
        <div class="uc-stat-divider"></div>
        <div class="uc-stat">
          <span class="uc-stat-number">2</span>
          <span class="uc-stat-unit">중 해시</span>
          <span class="uc-stat-desc">파일 + 지각해시</span>
        </div>
        <div class="uc-stat-divider"></div>
        <div class="uc-stat">
          <span class="uc-stat-number">0</span>
          <span class="uc-stat-unit">개 원본 저장</span>
          <span class="uc-stat-desc">해시만 남기고 즉시 삭제</span>
        </div>
      </div>
    </section>

    <!-- Cases -->
    <section class="uc-section">
      <div class="uc-inner">
        <span class="uc-label">Scenarios</span>
        <h2 class="uc-section-title">누가, 어떤 상황에서 사용하나요?</h2>

        <!-- Case 1: 언론사 -->
        <div class="uc-card">
          <div class="uc-card-header">
            <div class="uc-card-icon uc-card-icon-red">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v16a2 2 0 0 1-2 2Zm0 0a2 2 0 0 1-2-2v-9c0-1.1.9-2 2-2h2"/><path d="M18 14h-8"/><path d="M15 18h-5"/><path d="M10 6h8v4h-8V6Z"/></svg>
            </div>
            <div>
              <h3>언론사와 팩트체크 기관</h3>
              <span class="uc-card-tag">보도 신뢰성</span>
            </div>
          </div>
          <div class="uc-card-scenario">
            <div class="uc-scenario-quote">
              <span class="uc-quote-mark">"</span>
              <p>제보 영상이 도착했는데, 편집되거나 합성된 건 아닌지 확인할 방법이 없습니다.</p>
            </div>
          </div>
          <div class="uc-card-body">
            <div class="uc-comparison">
              <div class="uc-comp-col uc-comp-before">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-before"></span>
                  <span>기존 방식</span>
                </div>
                <ul>
                  <li>제보 영상의 원본 여부를 육안이나 메타데이터에 의존해 판단</li>
                  <li>영상이 여러 채널을 거치며 재인코딩되면 추적 불가</li>
                  <li>딥페이크 기술 발전으로 전문가도 구별 어려움</li>
                </ul>
              </div>
              <div class="uc-comp-col uc-comp-after">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-after"></span>
                  <span>진본 도입 후</span>
                </div>
                <ul>
                  <li>취재원이 촬영 즉시 진본 앱으로 등록 &rarr; <strong>블록체인에 지문 기록</strong></li>
                  <li>편집국에서 웹 또는 Chrome 확장으로 <strong>원본 일치 여부 즉시 확인</strong></li>
                  <li>VC 보증서로 <strong>등록자와 등록 시점</strong>까지 확인 가능</li>
                </ul>
              </div>
            </div>
          </div>
          <div class="uc-card-channels">
            <span class="uc-channel-chip uc-chip-primary">iOS 앱으로 등록</span>
            <span class="uc-channel-chip">웹에서 검증</span>
            <span class="uc-channel-chip">Chrome 확장으로 검증</span>
          </div>
        </div>

        <!-- Case 2: 크리에이터 -->
        <div class="uc-card">
          <div class="uc-card-header">
            <div class="uc-card-icon uc-card-icon-purple">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2" ry="2"/></svg>
            </div>
            <div>
              <h3>영상 제작자와 크리에이터</h3>
              <span class="uc-card-tag">영상 등록 사실 증명</span>
            </div>
          </div>
          <div class="uc-card-scenario">
            <div class="uc-scenario-quote">
              <span class="uc-quote-mark">"</span>
              <p>내가 만든 영상이 다른 채널에 무단으로 올라갔는데, 내가 언제 등록한 영상인지 보여주고 싶어요.</p>
            </div>
          </div>
          <div class="uc-card-body">
            <div class="uc-comparison">
              <div class="uc-comp-col uc-comp-before">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-before"></span>
                  <span>기존 방식</span>
                </div>
                <ul>
                  <li>업로드 날짜만으로 원본 소유를 주장하지만 플랫폼마다 기준이 다름</li>
                  <li>재인코딩이나 크기 조정을 거치면 원본과 파일이 달라져 직접 비교 불가</li>
                  <li>저작권 분쟁 시 객관적 증거 부족</li>
                </ul>
              </div>
              <div class="uc-comp-col uc-comp-after">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-after"></span>
                  <span>진본 도입 후</span>
                </div>
                <ul>
                  <li>플랫폼 업로드 전 진본 앱으로 등록 &rarr; <strong>등록 시점이 블록체인에 확정</strong></li>
                  <li>영상과 음성 지문으로 재인코딩하거나 크기를 조정한 <strong>등록 영상 후보와 유사도 비교</strong></li>
                  <li>DID 보증서로 <strong>등록자 본인임을 제3자에게 증명</strong></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="uc-card-channels">
            <span class="uc-channel-chip uc-chip-primary">iOS 앱으로 등록</span>
            <span class="uc-channel-chip">웹에서 검증</span>
          </div>
        </div>

        <!-- Case 3: 기업과 법적 증거 -->
        <div class="uc-card">
          <div class="uc-card-header">
            <div class="uc-card-icon uc-card-icon-green">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
            </div>
            <div>
              <h3>기업과 법적 증거</h3>
              <span class="uc-card-tag">증거 무결성</span>
            </div>
          </div>
          <div class="uc-card-scenario">
            <div class="uc-scenario-quote">
              <span class="uc-quote-mark">"</span>
              <p>현장 기록 영상을 법원에 제출했는데, 상대측이 '편집된 영상'이라며 증거력을 부인합니다.</p>
            </div>
          </div>
          <div class="uc-card-body">
            <div class="uc-comparison">
              <div class="uc-comp-col uc-comp-before">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-before"></span>
                  <span>기존 방식</span>
                </div>
                <ul>
                  <li>CCTV와 회의 녹화 파일의 무결성을 증명할 표준화된 방법 없음</li>
                  <li>파일 복사 과정에서 변조 의혹이 제기되면 반박 어려움</li>
                  <li>타임스탬프 조작 가능성으로 증거 능력 약화</li>
                </ul>
              </div>
              <div class="uc-comp-col uc-comp-after">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-after"></span>
                  <span>진본 도입 후</span>
                </div>
                <ul>
                  <li>녹화 직후 진본에 등록 &rarr; <strong>해시가 블록체인에 불변 기록</strong></li>
                  <li>분쟁 시 영상 파일을 검증하면 <strong>바이트 단위 동일성 즉시 확인</strong></li>
                  <li>모바일 신분증 기반 본인확인으로 <strong>등록자의 본인확인 상태를 함께 표시</strong></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="uc-card-channels">
            <span class="uc-channel-chip uc-chip-primary">iOS 앱으로 등록</span>
            <span class="uc-channel-chip">웹에서 검증</span>
          </div>
        </div>

        <!-- Case 4: 일반 사용자 -->
        <div class="uc-card">
          <div class="uc-card-header">
            <div class="uc-card-icon uc-card-icon-yellow">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <div>
              <h3>일반 사용자와 시청자</h3>
              <span class="uc-card-tag">등록 영상과의 일치 확인</span>
            </div>
          </div>
          <div class="uc-card-scenario">
            <div class="uc-scenario-quote">
              <span class="uc-quote-mark">"</span>
              <p>SNS에서 퍼진 영상이 등록된 영상과 일치하는지 확인할 수 있을까요?</p>
            </div>
          </div>
          <div class="uc-card-body">
            <div class="uc-comparison">
              <div class="uc-comp-col uc-comp-before">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-before"></span>
                  <span>기존 방식</span>
                </div>
                <ul>
                  <li>영상의 출처를 확인할 수단 없이 댓글이나 감에 의존</li>
                  <li>조작 여부를 판단하려면 전문 도구와 지식 필요</li>
                  <li>가짜 영상이 빠르게 확산되어도 개인이 할 수 있는 일이 없음</li>
                </ul>
              </div>
              <div class="uc-comp-col uc-comp-after">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-after"></span>
                  <span>진본 도입 후</span>
                </div>
                <ul>
                  <li>YouTube나 Instagram을 시청하면서 Chrome 확장으로 <strong>버튼 하나로 검증</strong></li>
                  <li>카카오톡 챗봇에 URL만 보내면 <strong>설치 없이 간편하게 확인</strong></li>
                  <li>로그인 없이 누구나 사용할 수 있고 <strong>기술 지식이 필요하지 않음</strong></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="uc-card-channels">
            <span class="uc-channel-chip">Chrome 확장으로 검증</span>
            <span class="uc-channel-chip">카카오톡으로 검증</span>
            <span class="uc-channel-chip">웹에서 검증</span>
          </div>
        </div>

        <!-- Case 5: 플랫폼 -->
        <div class="uc-card">
          <div class="uc-card-header">
            <div class="uc-card-icon uc-card-icon-blue">
              <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <div>
              <h3>플랫폼과 소셜 미디어</h3>
              <span class="uc-card-tag">콘텐츠 신뢰도</span>
            </div>
          </div>
          <div class="uc-card-scenario">
            <div class="uc-scenario-quote">
              <span class="uc-quote-mark">"</span>
              <p>사용자가 올리는 영상의 출처와 진위를 플랫폼이 직접 판별하기엔 비용과 한계가 큽니다.</p>
            </div>
          </div>
          <div class="uc-card-body">
            <div class="uc-comparison">
              <div class="uc-comp-col uc-comp-before">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-before"></span>
                  <span>기존 방식</span>
                </div>
                <ul>
                  <li>신고 기반 사후 대응으로 피해가 확산된 뒤에야 조치</li>
                  <li>자체 탐지 시스템 구축에 막대한 비용</li>
                  <li>사용자에게 영상의 신뢰도를 전달할 수단 없음</li>
                </ul>
              </div>
              <div class="uc-comp-col uc-comp-after">
                <div class="uc-comp-label">
                  <span class="uc-comp-dot uc-dot-after"></span>
                  <span>진본 도입 후</span>
                </div>
                <ul>
                  <li>진본 API 연동으로 업로드 시점에 <strong>자동으로 등록 여부 확인</strong></li>
                  <li>검증된 영상에 인증 배지를 표시해 <strong>시청자에게 신뢰도 전달</strong></li>
                  <li>원본 미저장 정책으로 <strong>개인정보 부담 없이 도입</strong> 가능</li>
                </ul>
              </div>
            </div>
          </div>
          <div class="uc-card-channels">
            <span class="uc-channel-chip uc-chip-primary">API 연동</span>
          </div>
        </div>
      </div>
    </section>

    <!-- How it works summary -->
    <section class="uc-flow-section">
      <div class="uc-inner">
        <span class="uc-label">How it works</span>
        <h2 class="uc-section-title">세 단계로 완성되는 검증</h2>
        <div class="uc-flow">
          <div class="uc-flow-step">
            <div class="uc-flow-num">1</div>
            <h4>등록</h4>
            <p>크리에이터가 iOS 앱으로 영상을 등록하면 해시가 블록체인에 기록됩니다.</p>
          </div>
          <div class="uc-flow-connector">
            <div class="uc-flow-line"></div>
            <svg class="uc-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <div class="uc-flow-step">
            <div class="uc-flow-num">2</div>
            <h4>검증</h4>
            <p>누구나 웹과 확장 또는 카카오톡으로 등록 영상과의 일치 여부를 확인합니다.</p>
          </div>
          <div class="uc-flow-connector">
            <div class="uc-flow-line"></div>
            <svg class="uc-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
          </div>
          <div class="uc-flow-step">
            <div class="uc-flow-num">3</div>
            <h4>신뢰</h4>
            <p>블록체인 기록과 DID 보증서로 등록 사실을 확인할 수 있는 증거를 남깁니다.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="uc-cta">
      <div class="uc-inner">
        <h2>영상의 진위, 지금 바로 확인하세요</h2>
        <p>로그인 없이 누구나 검증할 수 있습니다.</p>
        <div class="uc-cta-actions">
          <a href="/downloads" class="btn btn-primary">시작하기</a>
          <a href="/developers/guide/introduction" class="btn btn-secondary">개발자 센터</a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ─── Base ─── */
.use-cases-page {
  /* --jb-blue: 표면 위 텍스트·아이콘용 / --jb-blue-solid: 흰 글자를 올리는 채움 배경용 */
  --jb-blue: #2457E6;
  --jb-blue-solid: #2457E6;
  --jb-blue-solid-hover: #1a45c4;
  --jb-blue-light: #EEF4FF;
  --jb-blue-border: #C3D3FC;
  --jb-ink: #111827;
  --jb-text: #374151;
  /* 웜그레이 카드(#F7F6F3) 위에서 #6B7280은 4.47:1로 근소 미달 → 한 단계 진하게 */
  --jb-text-secondary: #646B78;
  --jb-text-tertiary: #646B78;
  --jb-border: #E5E7EB;
  --jb-bg: #FFFFFF;
  --jb-bg-alt: #F9FAFB;
  --jb-bg-warm: #F7F6F3;
  --jb-green: #047857;
  --jb-green-bg: #ECFDF5;
  --jb-red: #DC2626;
  --jb-red-bg: #FEF2F2;
  --jb-purple: #7C3AED;
  --jb-purple-bg: #F5F3FF;
  --jb-yellow: #B45309;
  --jb-yellow-bg: #FFFBEB;
  --jb-comp-before-bg: #F7F6F3;
  --jb-comp-before-border: #E8E5DF;
  --jb-comp-before-dot: #9CA3AF;
  --jb-comp-after-bg: #EEF4FF;
  --jb-comp-after-border: #C3D3FC;
  --jb-comp-after-dot: #2457E6;
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
}

.dark .use-cases-page {
  --jb-ink: #F9FAFB;
  --jb-text: #D1D5DB;
  --jb-text-secondary: #9CA3AF;
  --jb-text-tertiary: #9CA3AF;
  --jb-border: #374151;
  --jb-bg: #111827;
  --jb-bg-alt: #1F2937;
  --jb-bg-warm: #1C1917;
  /* 강조색을 함께 뒤집지 않으면 어두운 배경 위 어두운 글자가 됨 */
  --jb-blue: #7AA3F5;
  --jb-blue-solid: #3B6CF0;
  --jb-blue-solid-hover: #2E5DE0;
  --jb-blue-light: #1E293B;
  --jb-blue-border: #334155;
  --jb-green: #34D399;
  --jb-green-bg: #064E3B;
  --jb-red: #F87171;
  --jb-red-bg: #450A0A;
  --jb-purple: #C4B5FD;
  --jb-purple-bg: #2E1065;
  --jb-yellow: #FBBF24;
  --jb-yellow-bg: #78350F;
  --jb-comp-before-bg: #1C1917;
  --jb-comp-before-border: #292524;
  --jb-comp-before-dot: #6B7280;
  --jb-comp-after-bg: #172554;
  --jb-comp-after-border: #1E3A8A;
  --jb-comp-after-dot: #60A5FA;
}

/* ─── Hero ─── */
.uc-hero {
  background: linear-gradient(180deg, var(--jb-blue-light) 0%, var(--jb-bg) 100%);
  border-bottom: 1px solid var(--jb-border);
  padding: 80px 24px 64px;
  text-align: center;
}

.uc-hero-inner { max-width: 680px; margin: 0 auto; }

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
  font-size: 40px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 20px;
  letter-spacing: -0.02em;
  line-height: 1.25;
}

/* <br> 대신 절 단위 inline-block — 좁은 화면에서도 자연스럽게 흐름 */
.uc-hero-title span,
.uc-hero-desc span {
  display: inline-block;
}

.uc-hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0;
}

/* ─── Stats ─── */
.uc-stats {
  border-bottom: 1px solid var(--jb-border);
  padding: 40px 24px;
  background: var(--jb-bg);
}

.uc-stats-inner {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 48px;
}

.uc-stat { text-align: center; }

.uc-stat-number {
  font-size: 40px;
  font-weight: 800;
  color: var(--jb-blue);
  letter-spacing: -0.03em;
  line-height: 1;
}

.uc-stat-unit {
  font-size: 16px;
  font-weight: 600;
  color: var(--jb-ink);
  margin-left: 2px;
}

.uc-stat-desc {
  display: block;
  font-size: 13px;
  color: var(--jb-text-secondary);
  margin-top: 4px;
}

.uc-stat-divider {
  width: 1px;
  height: 40px;
  background: var(--jb-border);
  flex-shrink: 0;
}

/* ─── Section ─── */
.uc-section { padding: 72px 24px; }
.uc-inner { max-width: 880px; margin: 0 auto; }

.uc-section-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 40px;
  letter-spacing: -0.01em;
}

/* ─── Cards ─── */
.uc-card {
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 16px;
  padding: 36px;
  margin-bottom: 20px;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.uc-card:hover {
  border-color: var(--jb-blue-border);
  box-shadow: 0 8px 32px rgba(36, 87, 230, 0.06);
}

.uc-card:last-child { margin-bottom: 0; }

.uc-card-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}

.uc-card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.uc-card-icon-red { background: var(--jb-red-bg); color: var(--jb-red); }
.uc-card-icon-purple { background: var(--jb-purple-bg); color: var(--jb-purple); }
.uc-card-icon-green { background: var(--jb-green-bg); color: var(--jb-green); }
.uc-card-icon-yellow { background: var(--jb-yellow-bg); color: var(--jb-yellow); }
.uc-card-icon-blue { background: var(--jb-blue-light); color: var(--jb-blue); }

.uc-card-header h3 {
  font-size: 20px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 2px;
}

.uc-card-tag {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  color: var(--jb-text-tertiary);
  letter-spacing: 0.02em;
}

/* ─── Scenario quote ─── */
.uc-card-scenario {
  margin-bottom: 28px;
}

.uc-scenario-quote {
  position: relative;
  background: var(--jb-bg-alt);
  border-radius: 12px;
  padding: 20px 24px 20px 44px;
}

.uc-quote-mark {
  position: absolute;
  left: 16px;
  top: 10px;
  font-size: 32px;
  font-weight: 800;
  color: var(--jb-blue);
  opacity: 0.35;
  line-height: 1;
  font-family: Georgia, serif;
}

.uc-scenario-quote p {
  font-size: 15px;
  color: var(--jb-text-secondary);
  line-height: 1.7;
  margin: 0;
  font-style: italic;
}

/* ─── Comparison (Before / After) ─── */
.uc-card-body { margin-bottom: 24px; }

.uc-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.uc-comp-col {
  border-radius: 12px;
  padding: 22px 24px;
}

.uc-comp-before {
  background: var(--jb-comp-before-bg);
  border: 1px solid var(--jb-comp-before-border);
}

.uc-comp-after {
  background: var(--jb-comp-after-bg);
  border: 1px solid var(--jb-comp-after-border);
}

.uc-comp-label {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 14px;
}

.uc-comp-label span {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.uc-comp-before .uc-comp-label span:last-child { color: var(--jb-text-tertiary); }
.uc-comp-after .uc-comp-label span:last-child { color: var(--jb-blue); }

.uc-comp-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.uc-dot-before { background: var(--jb-comp-before-dot); }
.uc-dot-after { background: var(--jb-comp-after-dot); }

.uc-comp-col ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

.uc-comp-col li {
  font-size: 13px;
  line-height: 1.7;
  margin-bottom: 6px;
  padding-left: 20px;
  position: relative;
}

.uc-comp-col li:last-child { margin-bottom: 0; }

/* Before: × marker */
.uc-comp-before li::before {
  content: "\00D7";
  position: absolute;
  left: 0;
  top: 0;
  font-size: 15px;
  font-weight: 700;
  color: var(--jb-comp-before-dot);
  line-height: 1.7;
}

/* After: ✓ marker */
.uc-comp-after li::before {
  content: "\2713";
  position: absolute;
  left: 0;
  top: 0;
  font-size: 13px;
  font-weight: 700;
  color: var(--jb-comp-after-dot);
  line-height: 1.7;
}

.uc-comp-before li { color: var(--jb-text-secondary); }
.uc-comp-after li { color: var(--jb-text); }

.uc-comp-after li strong {
  color: var(--jb-blue);
  font-weight: 600;
}

/* ─── Channel chips ─── */
.uc-card-channels {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 20px;
  border-top: 1px solid var(--jb-border);
}

.uc-channel-chip {
  display: inline-flex;
  align-items: center;
  padding: 5px 14px;
  border-radius: 100px;
  font-size: 12px;
  font-weight: 600;
  background: var(--jb-bg-alt);
  border: 1px solid var(--jb-border);
  color: var(--jb-text-secondary);
  transition: border-color 0.15s ease;
}

.uc-channel-chip:hover {
  border-color: var(--jb-blue-border);
}

.uc-chip-primary {
  background: var(--jb-blue-light);
  border-color: var(--jb-blue-border);
  color: var(--jb-blue);
}

/* ─── Flow ─── */
.uc-flow-section {
  padding: 72px 24px;
  background: var(--jb-bg-alt);
  border-top: 1px solid var(--jb-border);
  border-bottom: 1px solid var(--jb-border);
}

.uc-flow {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  gap: 0;
  margin-top: 40px;
}

.uc-flow-step {
  flex: 1;
  max-width: 240px;
  text-align: center;
  padding: 0 16px;
}

.uc-flow-num {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--jb-blue-solid);
  color: #fff;
  font-size: 17px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.uc-flow-step h4 {
  font-size: 17px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 8px;
}

.uc-flow-step p {
  font-size: 14px;
  color: var(--jb-text-secondary);
  margin: 0;
  line-height: 1.6;
}

.uc-flow-connector {
  display: flex;
  align-items: center;
  gap: 0;
  margin-top: 14px;
  flex-shrink: 0;
}

.uc-flow-line {
  width: 24px;
  height: 2px;
  background: var(--jb-border);
}

.uc-flow-chevron {
  color: var(--jb-text-tertiary);
  flex-shrink: 0;
}

/* ─── CTA ─── */
.uc-cta {
  background: linear-gradient(180deg, var(--jb-bg) 0%, var(--jb-blue-light) 100%);
  padding: 72px 24px;
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

/* ─── Responsive ─── */
@media (max-width: 768px) {
  .uc-hero { padding: 56px 20px 48px; }
  .uc-hero-title { font-size: 28px; }
  .uc-hero-desc { font-size: 16px; }
  .uc-stats-inner { flex-direction: column; gap: 24px; }
  .uc-stat-divider { width: 40px; height: 1px; }
  .uc-section { padding: 48px 20px; }
  .uc-section-title { font-size: 24px; margin-bottom: 28px; }
  .uc-card { padding: 24px; }
  .uc-comparison { grid-template-columns: 1fr; }
  .uc-scenario-quote { padding: 16px 20px 16px 40px; }
  .uc-flow { flex-direction: column; align-items: center; gap: 8px; }
  .uc-flow-connector { transform: rotate(90deg); }
  .uc-flow-step { max-width: 100%; padding: 0; }
}
</style>
