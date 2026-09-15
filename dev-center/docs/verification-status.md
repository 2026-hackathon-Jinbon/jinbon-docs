---
layout: page
title: 검증 상태
description: 진본·콘텐츠 유사·미인증·확인 중 — 네 가지 판정의 의미, 승인 기준, 그리고 보증하지 않는 범위.
---

<div class="vs-page">
  <section class="vs-hero">
    <div class="vs-hero-inner">
      <span class="vs-label">Verification Status</span>
      <h1 class="vs-hero-title">영상 검증 상태</h1>
      <p class="vs-hero-desc"><span>진본은 제출 영상을 "진짜/가짜"로 단정하지 않습니다.</span> <span>등록 원본과의 관계를 확인하고, 콘텐츠 일치 정도를 판단합니다.</span></p>
    </div>
  </section>
  <section class="vs-section">
    <div class="vs-inner">
      <span class="vs-label">Four States</span>
      <h2 class="vs-section-title">사용자에게 표시하는 네 가지 상태</h2>
      <div class="vs-status-grid">
        <div class="vs-status-card vs-authentic">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
          </div>
          <span class="vs-chip vs-chip-green">진본</span>
          <h3>비교·등록 증거 기준 통과</h3>
          <p>파일 정확 일치 또는 영상·음성 유사도 기준 통과에 더해 등록 증거가 유효함</p>
          <code class="vs-code">AUTHENTICATED</code>
        </div>
        <div class="vs-status-card vs-similar">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          </div>
          <span class="vs-chip vs-chip-yellow">콘텐츠 유사</span>
          <h3>원본 후보를 찾음</h3>
          <p>등록 후보는 찾았지만 유사도 승인 기준 미달 또는 비교 정보 부족</p>
          <code class="vs-code">CONTENT_SIMILAR</code>
        </div>
        <div class="vs-status-card vs-unverified">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><line x1="15" y1="9" x2="9" y2="15"></line><line x1="9" y1="9" x2="15" y2="15"></line></svg>
          </div>
          <span class="vs-chip vs-chip-gray">미인증</span>
          <h3>진본 승인 불가</h3>
          <p>등록 원본이 없거나, 등록이 취소됐거나, 보증서가 유효하지 않음</p>
          <code class="vs-code">NOT_AUTHENTICATED</code>
        </div>
        <div class="vs-status-card vs-pending">
          <div class="vs-status-icon">
            <svg width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          </div>
          <span class="vs-chip vs-chip-blue">확인 중</span>
          <h3>일시적으로 판정 불가</h3>
          <p>외부 장애 또는 온체인 무결성 검증 실패. 상세 사유에 따라 재시도하거나 운영자 확인</p>
          <code class="vs-code">UNAVAILABLE</code>
        </div>
      </div>
      <div class="vs-note">등록 기록과 콘텐츠 판정은 별개입니다. 후보의 등록자 정보나 유효한 VC가 표시되어도 제출 영상 전체의 무변조를 뜻하지 않습니다.</div>
    </div>
  </section>
  <section class="vs-section vs-section-alt">
    <div class="vs-inner">
      <span class="vs-label">Assurance Scope</span>
      <h2 class="vs-section-title">같은 배지라도 일치 근거는 다릅니다</h2>
      <div class="vs-note">
        <dl class="vs-note-list">
          <dt>파일 정확 일치</dt>
          <dd>등록 파일과 SHA-256이 같습니다. 오디오가 없는 파일도 등록 증거가 유효하면 승인됩니다.</dd>
          <dt>유사도 기준 통과</dt>
          <dd>샘플로 비교한 영상·음성 지문이 기준을 충족합니다. 전체 프레임·음성의 무변조를 확정하지 않습니다.</dd>
          <dt>일부 구간 대응</dt>
          <dd>등록 원본의 대응 시간대를 함께 확인해야 합니다. 생략된 앞뒤 맥락까지 보증하지 않습니다.</dd>
        </dl>
      </div>
      <div class="vs-note">등록 원본은 비교 기준으로 등록된 파일을 뜻합니다. 촬영 원본 여부, 영상 속 사건의 사실성, AI 생성 여부, 제작자·저작권자 여부는 보증하지 않습니다. 등록 시각은 촬영 시각과 다릅니다.</div>
    </div>
  </section>
  <section class="vs-section">
    <div class="vs-inner">
      <span class="vs-label">What We Compare</span>
      <h2 class="vs-section-title">무엇을, 어떻게 대조하는가</h2>
      <p class="vs-section-desc">파일 해시가 다르면 <strong>1초 간격 대표 프레임과 음성 지문</strong>을 등록 후보와 각각 비교합니다. 모든 프레임을 검사하는 방식은 아닙니다.</p>
      <div class="vs-track-demo">
        <div class="vs-track-row">
          <span class="vs-track-label">등록 원본</span>
          <div class="vs-track">
            <span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span><span class="vs-seg vs-seg-ref"></span>
          </div>
        </div>
        <div class="vs-track-row">
          <span class="vs-track-label">제출 영상</span>
          <div class="vs-track">
            <span class="vs-seg vs-seg-gap"></span><span class="vs-seg vs-seg-gap"></span><span class="vs-seg vs-seg-gap"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-ok"></span><span class="vs-seg vs-seg-gap"></span><span class="vs-seg vs-seg-gap"></span><span class="vs-seg vs-seg-gap"></span>
          </div>
        </div>
        <div class="vs-track-row vs-track-row-axis">
          <span class="vs-track-label"></span>
          <div class="vs-track vs-track-axis">
            <span class="vs-axis-span">원본 3~9초 구간에 대응 · 순서 보존</span>
          </div>
        </div>
        <div class="vs-track-caption">제출본이 원본의 어느 위치에 대응하는지 슬라이딩으로 찾습니다. 쇼츠도 후보 검색·유사도 기준·등록 증거 검증을 통과하면 <strong>승인될 수 있습니다.</strong></div>
      </div>
      <div class="vs-threshold-grid">
        <div class="vs-threshold">
          <div class="vs-threshold-head">
            <h4>영상 세그먼트</h4>
            <span class="vs-threshold-value">≥ 95%</span>
          </div>
          <div class="vs-bar"><div class="vs-bar-fill vs-bar-green" style="width:95%"></div></div>
          <p>1초 간격 대표 프레임 해시의 대응 비율. 한 시간 오프셋에서 일정한 간격으로 비교합니다.</p>
        </div>
        <div class="vs-threshold">
          <div class="vs-threshold-head">
            <h4>음성 세그먼트</h4>
            <span class="vs-threshold-value">≥ 90%</span>
          </div>
          <div class="vs-bar"><div class="vs-bar-fill vs-bar-green" style="width:90%"></div></div>
          <p>1초 간격 스펙트로그램 해시의 대응 비율. 음성이 없으면 <strong>유사도 경로로는 승인하지 않습니다.</strong> 파일 정확 일치는 별도입니다.</p>
        </div>
      </div>
      <div class="vs-note">이 수치는 유사도 경로의 승인 기준이며 정확도나 조작 탐지율이 아닙니다. 일부 불일치를 허용하고, 샘플 사이의 편집이나 작은 변화는 놓칠 수 있습니다. 각각의 영상·음성이 원본에서 같은 시간대의 조합인지까지는 확인하지 않습니다.</div>
    </div>
  </section>
  <section class="vs-section">
    <div class="vs-inner">
      <span class="vs-label">Decision Flow</span>
      <h2 class="vs-section-title">상태가 결정되는 흐름</h2>
      <div class="vs-flow">
        <div class="vs-flow-step">
          <div class="vs-flow-num">1</div>
          <h4>원본 검색</h4>
          <p>파일 해시가 같으면 3단계로 이동합니다. 다르면 지각해시로 후보를 찾습니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-gray">후보 없음 → 미인증</span>
          </div>
        </div>
        <div class="vs-flow-connector">
          <div class="vs-flow-line"></div>
          <svg class="vs-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
        <div class="vs-flow-step">
          <div class="vs-flow-num">2</div>
          <h4>영상·음성 대조</h4>
          <p>파일이 다른 경우 대표 프레임·음성 지문의 대응 비율을 확인합니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-green">모두 통과 → 진본 후보</span>
            <span class="vs-branch vs-branch-yellow">일부 통과 → 콘텐츠 유사</span>
          </div>
        </div>
        <div class="vs-flow-connector">
          <div class="vs-flow-line"></div>
          <svg class="vs-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
        <div class="vs-flow-step">
          <div class="vs-flow-num">3</div>
          <h4>등록 증거 검증</h4>
          <p>온체인 서명 재대조와 VC 보증서를 확인합니다</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-gray">VC 미발급·무효 → 미인증</span>
            <span class="vs-branch vs-branch-blue">체인 검증 실패·외부 장애 → 확인 중</span>
          </div>
        </div>
        <div class="vs-flow-connector">
          <div class="vs-flow-line"></div>
          <svg class="vs-flow-chevron" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"></polyline></svg>
        </div>
        <div class="vs-flow-step">
          <div class="vs-flow-num">4</div>
          <h4>최종 판정</h4>
          <p>콘텐츠 일치와 등록 증거를 모두 통과한 경우에만 진본</p>
          <div class="vs-flow-branch">
            <span class="vs-branch vs-branch-green">전부 통과 → 진본</span>
          </div>
        </div>
      </div>
      <div class="vs-note">콘텐츠가 일치해도 <strong>등록 증거가 무너지면 진본이 아닙니다.</strong> 3단계 결과가 2단계 판정을 덮어씁니다.</div>
    </div>
  </section>
  <section class="vs-section vs-section-alt">
    <div class="vs-inner">
      <span class="vs-label">Examples</span>
      <h2 class="vs-section-title">대표 사례</h2>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-green">
          <span class="vs-chip vs-chip-green">진본</span>
          <span>콘텐츠 비교·등록 증거 기준 통과</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">등록 파일 그대로 제출</div>
          <div class="vs-case-detail">파일 SHA-256 일치 + 등록 증거 검증 통과 → 등록자·등록 시각 표시</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">YouTube 재인코딩·해상도 변경</div>
          <div class="vs-case-detail">후보 검색·영상·음성 비교 기준과 등록 증거 검증을 통과한 경우</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">긴 원본에서 30초를 잘라낸 쇼츠</div>
          <div class="vs-case-detail">후보 검색·영상·음성 비교 기준과 등록 증거 검증을 통과하면 승인. 원본 대응 구간을 표시하며 맥락은 별도 확인</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-yellow">
          <span class="vs-chip vs-chip-yellow">콘텐츠 유사</span>
          <span>등록 후보와의 비교 기준 미달 또는 정보 부족</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">영상은 같고 음성만 교체</div>
          <div class="vs-case-detail">영상 커버리지는 통과하지만 음성 커버리지 미달 → 진본으로 승격하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">얼굴·입모양을 변경 (딥페이크)</div>
          <div class="vs-case-detail">샘플에 변화가 반영돼 승인 기준에 미달한 경우. 얼굴·입모양 변경의 탐지를 보장하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">여러 원본을 이어 붙이거나 장면 삽입</div>
          <div class="vs-case-detail">대응 비율이 승인 기준에 미달한 경우. 불일치 구간은 삽입·편집의 확정 증거가 아님</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">자막·로고만 추가된 영상</div>
          <div class="vs-case-detail">승인 기준에 미달하면 콘텐츠 유사. 작은 자막·로고는 지문에 충분히 반영되지 않을 수 있음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">오디오 트랙이 없는 영상</div>
          <div class="vs-case-detail">파일이 다른 경우 음성 비교 불가로 유사도 승인 보류. 파일 정확 일치와 유효한 등록 증거가 있으면 승인 가능</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-gray">
          <span class="vs-chip vs-chip-gray">미인증</span>
          <span>등록 증거가 없거나 유효하지 않음</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">등록 원본을 찾지 못함</div>
          <div class="vs-case-detail">미등록 = 가짜라는 뜻은 아님. 검증된 VC는 노출하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">등록자가 영상을 비활성화</div>
          <div class="vs-case-detail">온체인 기록은 남지만 진본으로 표시하지 않음</div>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">보증서 미발급 · 폐기 · 클레임 불일치</div>
          <div class="vs-case-detail">블록체인 등록은 확인되지만 등록자 신원 보증이 성립하지 않음</div>
        </div>
      </div>
      <div class="vs-case-group">
        <div class="vs-case-header vs-case-header-blue">
          <span class="vs-chip vs-chip-blue">확인 중</span>
          <span>현재 판정 불가</span>
        </div>
        <div class="vs-case-item">
          <div class="vs-case-scenario">블록체인·Verifier 장애</div>
          <div class="vs-case-detail">외부 장애는 재시도 안내. 온체인 무결성 불일치도 같은 상태로 반환되므로 message·notice의 운영자 확인 안내를 함께 표시</div>
        </div>
      </div>
    </div>
  </section>
</div>

<style>
.vs-page {
  /* --vs-blue: 표면 위 텍스트용 / --vs-blue-solid: 흰 글자를 올리는 채움 배경용 */
  --vs-blue: #2457E6;
  --vs-blue-solid: #2457E6;
  --vs-blue-light: #EEF4FF;
  --vs-blue-border: #C3D3FC;
  --vs-ink: #111827;
  --vs-text: #374151;
  --vs-text-2: #6B7280;
  --vs-text-3: #9CA3AF;
  --vs-border: #E5E7EB;
  --vs-bg: #FFFFFF;
  --vs-bg-alt: #F9FAFB;
  --vs-green: #047857;
  --vs-green-bg: #ECFDF5;
  --vs-green-border: #A7F3D0;
  --vs-yellow: #B45309;
  --vs-yellow-bg: #FFFBEB;
  --vs-yellow-border: #FDE68A;
  /* 미인증은 "가짜"가 아니라 "등록 기록 없음"이므로 경고(빨강)가 아닌 중립(회색) */
  --vs-gray: #4B5563;
  --vs-gray-bg: #F3F4F6;
  --vs-gray-border: #D1D5DB;
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
  /* 강조색도 함께 뒤집지 않으면 어두운 배경 위 어두운 글자가 되어 대비가 무너짐 */
  --vs-blue: #7AA3F5;
  --vs-blue-solid: #3B6CF0;
  --vs-green: #34D399;
  --vs-green-bg: #064E3B;
  --vs-green-border: #065F46;
  --vs-yellow: #FBBF24;
  --vs-yellow-bg: #78350F;
  --vs-yellow-border: #92400E;
  --vs-gray: #9CA3AF;
  --vs-gray-bg: #1F2937;
  --vs-gray-border: #374151;
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
  margin: 0 0 16px;
  letter-spacing: -0.01em;
}
.vs-section-desc {
  font-size: 16px;
  line-height: 1.7;
  color: var(--vs-text-2);
  margin: 0 0 32px;
}
.vs-section-desc strong { color: var(--vs-ink); }
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
.vs-note strong { color: var(--vs-ink); }
/* <br>로 나열하던 3개 항목을 정의 목록으로 — 스크린리더가 항목 구조를 읽음 */
.vs-note-list { margin: 0; }
.vs-note-list dt {
  display: inline;
  font-weight: 700;
  color: var(--vs-ink);
}
.vs-note-list dt::after { content: ":"; }
.vs-note-list dd { display: inline; margin: 0 0 0 4px; }
.vs-note-list dd::after { content: ""; display: block; }
.vs-section-alt .vs-note { background: var(--vs-bg); }
.vs-status-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-top: 20px;
}
.vs-status-card {
  display: flex;
  flex-direction: column;
  background: var(--vs-bg);
  border: 1px solid var(--vs-border);
  border-radius: 16px;
  padding: 24px 20px;
  text-align: center;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.vs-status-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,0.06); }
.vs-authentic:hover { border-color: var(--vs-green-border); }
.vs-similar:hover { border-color: var(--vs-yellow-border); }
.vs-unverified:hover { border-color: var(--vs-gray-border); }
.vs-pending:hover { border-color: var(--vs-blue-border); }
.vs-status-icon {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
}
.vs-authentic .vs-status-icon { background: var(--vs-green-bg); color: var(--vs-green); }
.vs-similar .vs-status-icon { background: var(--vs-yellow-bg); color: var(--vs-yellow); }
.vs-unverified .vs-status-icon { background: var(--vs-gray-bg); color: var(--vs-gray); }
.vs-pending .vs-status-icon { background: var(--vs-blue-light); color: var(--vs-blue); }
.vs-chip {
  display: inline-flex;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  margin: 0 auto 10px;
}
.vs-chip-green { color: #18794e; background: #dcfce7; }
.vs-chip-yellow { color: #854D0E; background: #FEF3C7; }
.vs-chip-gray { color: #4B5563; background: #F3F4F6; }
.vs-chip-blue { color: #1943BE; background: #dbeafe; }
.dark .vs-chip-green { color: #4ade80; background: #064E3B; }
.dark .vs-chip-yellow { color: #fbbf24; background: #78350F; }
.dark .vs-chip-gray { color: #D1D5DB; background: #374151; }
.dark .vs-chip-blue { color: #93c5fd; background: #1E3A8A; }
.vs-status-card h3 {
  font-size: 16px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0 0 8px;
}
.vs-status-card p {
  font-size: 13.5px;
  color: var(--vs-text-2);
  line-height: 1.6;
  margin: 0 0 14px;
  flex: 1;
}
.vs-code {
  display: block;
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 11px;
  font-weight: 600;
  color: var(--vs-text-2);
  background: var(--vs-bg-alt);
  border: 1px solid var(--vs-border);
  border-radius: 6px;
  padding: 5px 8px;
  white-space: nowrap;
  overflow-x: auto;
}
.vs-section-alt .vs-code { background: var(--vs-bg); }

/* ─── Track demo ─── */
.vs-track-demo {
  background: var(--vs-bg);
  border: 1px solid var(--vs-border);
  border-radius: 14px;
  padding: 28px 24px 20px;
  margin-bottom: 20px;
}
.vs-track-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}
.vs-track-label {
  flex: 0 0 72px;
  font-size: 13px;
  font-weight: 600;
  color: var(--vs-text-2);
  text-align: right;
}
.vs-track {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 3px;
  flex: 1;
  min-width: 0;
}
.vs-seg {
  height: 28px;
  border-radius: 4px;
  min-width: 0;
}
.vs-seg-ref { background: #dbeafe; border: 1px solid var(--vs-blue-border); }
.dark .vs-seg-ref { background: #1E3A8A; border-color: #2c4a8f; }
.vs-seg-ok { background: #bbf7d0; border: 1px solid var(--vs-green); }
.dark .vs-seg-ok { background: #065F46; border-color: #10b981; }
.vs-seg-gap { background: transparent; border: 1px dashed var(--vs-border); }
.vs-track-row-axis { margin-bottom: 6px; }
.vs-track-axis {
  display: block;
  position: relative;
  height: 22px;
}
.vs-axis-span {
  position: absolute;
  left: calc(25% + 1.5px);
  width: calc(50% - 3px);
  top: 0;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 600;
  color: var(--vs-green);
  border-left: 2px solid var(--vs-green);
  border-right: 2px solid var(--vs-green);
  border-bottom: 2px solid var(--vs-green);
  border-radius: 0 0 6px 6px;
  white-space: nowrap;
}
.vs-track-caption {
  font-size: 13px;
  color: var(--vs-text-2);
  line-height: 1.7;
  padding-left: 88px;
  margin-top: 4px;
}
.vs-track-caption strong { color: var(--vs-ink); }

/* ─── Thresholds ─── */
.vs-threshold-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
.vs-threshold {
  background: var(--vs-bg);
  border: 1px solid var(--vs-border);
  border-radius: 14px;
  padding: 22px 24px;
}
.vs-threshold-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}
.vs-threshold h4 {
  font-size: 15px;
  font-weight: 700;
  color: var(--vs-ink);
  margin: 0;
}
.vs-threshold-value {
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 18px;
  font-weight: 700;
  color: var(--vs-green);
}
.vs-bar {
  height: 8px;
  border-radius: 999px;
  background: var(--vs-bg-alt);
  border: 1px solid var(--vs-border);
  overflow: hidden;
  margin-bottom: 14px;
}
.vs-section-alt .vs-bar { background: var(--vs-bg-alt); }
.vs-bar-fill { height: 100%; border-radius: 999px; }
.vs-bar-green { background: var(--vs-green); }
.vs-threshold p {
  font-size: 13.5px;
  color: var(--vs-text-2);
  line-height: 1.65;
  margin: 0;
}
.vs-threshold p strong { color: var(--vs-ink); }

/* ─── Flow ─── */
.vs-flow {
  display: flex;
  align-items: flex-start;
  gap: 0;
}
.vs-flow-step {
  flex: 1;
  text-align: center;
  padding: 0 10px;
}
.vs-flow-num {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--vs-blue-solid);
  color: #fff;
  font-size: 17px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}
.vs-flow-step h4 {
  font-size: 15px;
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
.vs-branch-yellow { color: #854D0E; background: #FEF3C7; }
.vs-branch-gray { color: #4B5563; background: #F3F4F6; }
.vs-branch-blue { color: #1943BE; background: #dbeafe; }
.dark .vs-branch-green { color: #4ade80; background: #064E3B; }
.dark .vs-branch-yellow { color: #fbbf24; background: #78350F; }
.dark .vs-branch-gray { color: #D1D5DB; background: #374151; }
.dark .vs-branch-blue { color: #93c5fd; background: #1E3A8A; }
.vs-flow-connector {
  display: flex;
  align-items: center;
  margin-top: 14px;
  flex-shrink: 0;
}
.vs-flow-line { width: 16px; height: 2px; background: var(--vs-border); }
.vs-flow-chevron { color: var(--vs-text-3); flex-shrink: 0; }

/* ─── Cases ─── */
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
.vs-case-header .vs-chip { margin: 0; }
.vs-case-header-green { background: var(--vs-green-bg); }
.vs-case-header-yellow { background: var(--vs-yellow-bg); }
.vs-case-header-gray { background: var(--vs-gray-bg); }
.vs-case-header-blue { background: var(--vs-blue-light); }
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
  min-width: 220px;
  font-size: 14px;
  font-weight: 600;
  color: var(--vs-ink);
}
.vs-case-detail {
  font-size: 13px;
  color: var(--vs-text-2);
  line-height: 1.6;
}
@media (max-width: 960px) {
  .vs-status-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 768px) {
  .vs-hero { padding: 56px 20px 48px; }
  .vs-hero-title { font-size: 28px; }
  .vs-hero-desc { font-size: 16px; }
  .vs-section { padding: 48px 20px; }
  .vs-section-title { font-size: 24px; }
  .vs-status-grid { grid-template-columns: 1fr; }
  .vs-threshold-grid { grid-template-columns: 1fr; }
  .vs-flow { flex-direction: column; align-items: center; gap: 8px; }
  .vs-flow-connector { transform: rotate(90deg); }
  .vs-case-item { flex-direction: column; gap: 4px; }
  .vs-case-scenario { min-width: 0; }
  .vs-track-row { flex-direction: column; align-items: stretch; gap: 6px; }
  .vs-track-label { text-align: left; flex: none; }
  .vs-track-caption { padding-left: 0; }
}
</style>
