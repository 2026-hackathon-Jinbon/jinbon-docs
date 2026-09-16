<template>
  <div class="downloads-page">
    <!-- Hero -->
    <section class="dl-hero">
      <div class="dl-hero-inner">
        <span class="dl-label">Get Started</span>
        <h1 class="dl-hero-title">진본 시작하기</h1>
        <p class="dl-hero-desc">
          영상을 등록하거나 검증하는 방법을 선택하세요.
        </p>
      </div>
    </section>

    <!-- Channels -->
    <section class="dl-section">
      <div class="dl-inner">
        <div class="dl-grid">
          <!-- iOS -->
          <div class="dl-card dl-card-primary">
            <div class="dl-card-badge">등록 + 검증</div>
            <div class="dl-card-icon">
              <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            </div>
            <h2>iOS 앱</h2>
            <p class="dl-card-repo">jinbon-ios</p>
            <p class="dl-card-desc">
              회원가입, DID/Wallet 관리, <strong>영상 등록</strong>, VC 보증서 보관까지.
              진본의 모든 기능을 사용할 수 있는 메인 앱입니다.
            </p>
            <div class="dl-card-stack">Swift / UIKit / DIDWalletSDK 2.0.1</div>
            <div class="dl-card-requires">
              <strong>필요 조건:</strong> iOS 기기, OmniOne CX 모바일 신분증
            </div>
            <p class="dl-card-pending"><strong>배포 준비 중</strong><br/>아직 설치할 수 없습니다. 공개 후 이곳에서 설치 방법을 안내합니다.</p>
          </div>

          <!-- Web -->
          <div class="dl-card">
            <div class="dl-card-badge">검증 전용</div>
            <div class="dl-card-icon">
              <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            </div>
            <h2>검증 웹</h2>
            <p class="dl-card-repo">jinbon-web</p>
            <p class="dl-card-desc">
              브라우저에서 영상 파일을 올려 검증하는 채널입니다.
              <strong>로그인 없이</strong> 영상 파일을 선택할 수 있습니다.
            </p>
            <div class="dl-card-stack">Next.js 16 / React 19 / Tailwind CSS</div>
            <div class="dl-card-requires">
              <strong>필요 조건:</strong> 웹 브라우저
            </div>
            <a class="dl-card-link" href="https://jinbon-web.vercel.app" target="_blank" rel="noopener noreferrer">
              웹에서 검증하기<span class="dl-ext" aria-hidden="true">↗</span>
              <span class="sr-only">(새 창)</span>
            </a>
            <p class="dl-card-pending">회사 네트워크에서 검증 서버 연결이 차단되면 네트워크 관리자에게 접속 허용을 요청해 주세요.</p>
          </div>

          <!-- Extension -->
          <div class="dl-card">
            <div class="dl-card-badge">검증 전용</div>
            <div class="dl-card-icon">
              <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </div>
            <h2>Chrome 확장</h2>
            <p class="dl-card-repo">jinbon-extension</p>
            <p class="dl-card-desc">
              YouTube, Instagram에서 영상을 보면서 <strong>버튼 하나로 즉시 검증</strong>.
              URL 기반으로 동작해 파일 다운로드가 필요 없습니다.
            </p>
            <div class="dl-card-stack">Manifest V3 / JavaScript</div>
            <div class="dl-card-requires">
              <strong>필요 조건:</strong> Chrome 브라우저
            </div>
            <a class="dl-card-link" href="/jinbon-extension-0.1.0.zip" download>Chrome 확장 다운로드</a>
            <details class="dl-install">
              <summary>다운로드 후 설치 방법</summary>
              <ol>
                <li>다운로드한 ZIP 파일의 압축을 해제합니다.</li>
                <li>Chrome 주소창에 <code>chrome://extensions</code>를 입력합니다.</li>
                <li>오른쪽 위의 ‘개발자 모드’를 켭니다.</li>
                <li>‘압축해제된 확장 프로그램을 로드합니다’를 누르고 <code>manifest.json</code>이 들어 있는 폴더를 선택합니다.</li>
                <li>YouTube 또는 Instagram 영상 페이지를 새로고침한 뒤 ‘진본 확인’ 버튼을 누릅니다.</li>
              </ol>
              <p>Chrome 웹 스토어를 통한 설치는 아직 제공하지 않습니다. 기존 설치를 업데이트할 때는 새 파일로 교체한 뒤 확장 관리 화면에서 새로고침하세요.</p>
            </details>
          </div>
          <!-- KakaoTalk -->
          <div class="dl-card">
            <div class="dl-card-badge">검증 전용</div>
            <div class="dl-card-icon">
              <svg width="32" height="32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
            </div>
            <h2>카카오톡 챗봇</h2>
            <p class="dl-card-repo">카카오톡 채널</p>
            <p class="dl-card-desc">
              카카오톡 대화창에서 영상 URL을 보내면 <strong>즉시 검증 결과를 응답</strong>합니다.
              별도 설치 없이 누구나 사용할 수 있습니다.
            </p>
            <div class="dl-card-stack">카카오톡 채널 / 챗봇</div>
            <div class="dl-card-requires">
              <strong>필요 조건:</strong> 카카오톡
            </div>
            <a class="dl-card-link" href="https://pf.kakao.com/_xgtNBX"
               target="_blank" rel="noopener noreferrer">
              카카오톡 채널 열기<span class="dl-ext" aria-hidden="true">↗</span>
              <span class="sr-only">(새 창)</span>
            </a>
            <!-- 백엔드 배포 후 이 줄만 삭제하세요 -->
            <p class="dl-card-pending">채널 추가는 지금 가능하며, 검증 응답은 백엔드 배포 후 동작합니다.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How it connects -->
    <section class="dl-section dl-section-alt">
      <div class="dl-inner">
        <h2 class="dl-section-title">채널별 역할</h2>
        <table class="dl-table">
          <thead>
            <tr>
              <th scope="col">채널</th>
              <th scope="col">등록</th>
              <th scope="col">검증</th>
              <th scope="col">로그인</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">iOS 앱</th>
              <td class="dl-yes"><span aria-hidden="true">✓</span><span class="sr-only">가능</span></td>
              <td class="dl-yes"><span aria-hidden="true">✓</span><span class="sr-only">가능</span></td>
              <td>필요</td>
            </tr>
            <tr>
              <th scope="row">검증 웹</th>
              <td class="dl-no"><span aria-hidden="true">×</span><span class="sr-only">불가</span></td>
              <td class="dl-yes"><span aria-hidden="true">✓</span><span class="sr-only">가능</span></td>
              <td>불필요</td>
            </tr>
            <tr>
              <th scope="row">Chrome 확장</th>
              <td class="dl-no"><span aria-hidden="true">×</span><span class="sr-only">불가</span></td>
              <td class="dl-yes"><span aria-hidden="true">✓</span><span class="sr-only">가능</span></td>
              <td>불필요</td>
            </tr>
            <tr>
              <th scope="row">카카오톡 챗봇</th>
              <td class="dl-no"><span aria-hidden="true">×</span><span class="sr-only">불가</span></td>
              <td class="dl-yes"><span aria-hidden="true">✓</span><span class="sr-only">가능</span></td>
              <td>불필요</td>
            </tr>
          </tbody>
        </table>
        <p class="dl-note">위 표는 채널별 기능을 설명합니다. 영상 <strong>등록</strong>을 지원하는 iOS 앱은 배포 준비 중이며 현재 일반 다운로드는 제공하지 않습니다.</p>
      </div>
    </section>

    <!-- Developer CTA -->
    <section class="dl-section">
      <div class="dl-inner" style="text-align: center;">
        <h2 class="dl-section-title">개발자이신가요?</h2>
        <p style="color: var(--jb-text-secondary); margin-bottom: 24px;">
          API 연동, 시스템 아키텍처, 데이터 모델 등 기술 문서를 확인하세요.
        </p>
        <a href="/developers/guide/introduction" class="btn btn-primary">개발자 센터 바로가기</a>
      </div>
    </section>
  </div>
</template>

<style scoped>
.downloads-page {
  /* --jb-blue: 표면 위 텍스트·아이콘용 / --jb-blue-solid: 흰 글자를 올리는 채움 배경용 */
  --jb-blue: #2457E6;
  --jb-blue-solid: #2457E6;
  --jb-blue-solid-hover: #1a45c4;
  --jb-blue-light: #EEF4FF;
  /* 연파랑 카드 위에서는 --jb-text-secondary(#6B7280)가 4.38:1로 AA 미달 */
  --jb-text-on-tint: #5A6373;
  --jb-blue-border: #C3D3FC;
  --jb-ink: #111827;
  --jb-text: #374151;
  --jb-text-secondary: #6B7280;
  --jb-border: #E5E7EB;
  --jb-bg: #FFFFFF;
  --jb-bg-alt: #F9FAFB;
  --jb-green: #047857;
  font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Pretendard", sans-serif;
}

.dark .downloads-page {
  --jb-ink: #F9FAFB;
  --jb-text: #D1D5DB;
  --jb-text-secondary: #9CA3AF;
  --jb-border: #374151;
  --jb-bg: #111827;
  --jb-bg-alt: #1F2937;
  /* 강조색을 함께 뒤집지 않으면 어두운 배경 위 어두운 글자가 됨 */
  --jb-blue: #7AA3F5;
  --jb-blue-solid: #3B6CF0;
  --jb-blue-solid-hover: #2E5DE0;
  --jb-blue-light: #1E293B;
  --jb-text-on-tint: #9CA3AF;
  --jb-blue-border: #334155;
  --jb-green: #34D399;
}

.dl-hero {
  background: linear-gradient(180deg, var(--jb-blue-light) 0%, var(--jb-bg) 100%);
  border-bottom: 1px solid var(--jb-border);
  padding: 72px 24px 56px;
  text-align: center;
}

.dl-hero-inner { max-width: 640px; margin: 0 auto; }

.dl-label {
  display: inline-block;
  font-size: 12px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--jb-blue);
  margin-bottom: 12px;
}

.dl-hero-title {
  font-size: 36px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 16px;
  letter-spacing: -0.02em;
}

.dl-hero-desc {
  font-size: 18px;
  line-height: 1.7;
  color: var(--jb-text-secondary);
  margin: 0;
}

.dl-section { padding: 64px 24px; }
.dl-section-alt { background: var(--jb-bg-alt); }
.dl-inner { max-width: 960px; margin: 0 auto; }

.dl-section-title {
  font-size: 24px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 24px;
  text-align: center;
}

.dl-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.dl-card {
  background: var(--jb-bg);
  border: 1px solid var(--jb-border);
  border-radius: 16px;
  padding: 28px;
  position: relative;
}

.dl-card-primary {
  border-color: var(--jb-blue-border);
  background: var(--jb-blue-light);
}

.dl-card-badge {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--jb-blue);
  background: var(--jb-bg);
  border: 1px solid var(--jb-blue-border);
  padding: 4px 10px;
  border-radius: 100px;
  margin-bottom: 16px;
}

.dl-card-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: var(--jb-blue-light);
  color: var(--jb-blue);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 16px;
}

.dl-card-primary .dl-card-repo,
.dl-card-primary .dl-card-stack { color: var(--jb-text-on-tint); }

.dl-card-primary .dl-card-icon {
  background: var(--jb-blue-solid);
  color: #fff;
}

.dl-card h2 {
  font-size: 20px;
  font-weight: 700;
  color: var(--jb-ink);
  margin: 0 0 4px;
}

.dl-card-repo {
  font-family: "SF Mono", "Fira Code", monospace;
  font-size: 13px;
  color: var(--jb-text-secondary);
  margin: 0 0 12px;
}

.dl-card-desc {
  font-size: 14px;
  color: var(--jb-text);
  line-height: 1.65;
  margin: 0 0 16px;
}

.dl-card-stack {
  font-size: 12px;
  color: var(--jb-text-secondary);
  margin-bottom: 12px;
}

.dl-card-requires {
  font-size: 13px;
  color: var(--jb-text-secondary);
  background: var(--jb-bg-alt);
  border-radius: 8px;
  padding: 10px 14px;
}

/* ─── 채널 바로가기 ─── */
.dl-card-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 14px;
  padding: 10px 18px;
  border-radius: 10px;
  background: var(--jb-blue-solid);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.15s ease, transform 0.15s ease,
    box-shadow 0.15s ease;
}

.dl-card-link:hover {
  background: var(--jb-blue-solid-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(36, 87, 230, 0.3);
}

.dl-ext { font-size: 12px; }

.dl-install {
  margin-top: 14px;
  color: var(--jb-text);
  font-size: 14px;
  line-height: 1.7;
  overflow-wrap: anywhere;
}

.dl-install summary { cursor: pointer; font-weight: 600; }
.dl-install ol { padding-left: 22px; margin: 12px 0; list-style: decimal; }
.dl-install li + li { margin-top: 8px; }
.dl-install p { margin: 12px 0 0; }
.dl-card-link:focus-visible,
.dl-install summary:focus-visible { outline: 2px solid var(--jb-blue); outline-offset: 4px; }

.dl-card-pending {
  margin: 10px 0 0;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--jb-text-secondary);
}

.dl-card-primary .dl-card-requires {
  background: var(--jb-bg);
}

.dl-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 15px;
}

.dl-table th, .dl-table td {
  padding: 12px 16px;
  text-align: center;
  border-bottom: 1px solid var(--jb-border);
}

/* 열 머리글만 대문자 라벨 스타일 — 행 머리글까지 적용되면 "IOS 앱"이 됨 */
.dl-table th[scope="col"] {
  font-weight: 600;
  color: var(--jb-text-secondary);
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.dl-table td { color: var(--jb-text); }
/* 행 머리글은 본문 셀과 같은 모양 (기존 <td><strong>…</strong></td>과 동일하게) */
.dl-table th[scope="row"] {
  text-align: left;
  font-weight: 700;
  color: var(--jb-ink);
}
.dl-yes { color: var(--jb-green); font-weight: 700; }
.dl-no { color: var(--jb-text-secondary); }

.dl-note {
  font-size: 14px;
  color: var(--jb-text-secondary);
  text-align: center;
  margin-top: 16px;
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
  background: var(--jb-blue-solid);
  color: #fff;
}

.btn-primary:hover {
  background: var(--jb-blue-solid-hover);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(36, 87, 230, 0.3);
}

@media (max-width: 768px) {
  .dl-hero { padding: 48px 20px 40px; }
  .dl-hero-title { font-size: 28px; }
  .dl-section { padding: 40px 20px; }
  .dl-grid { grid-template-columns: 1fr; }
}
</style>
