<script setup lang="ts">
const cases = [
  {
    id: 'announcement', number: '01', audience: '보도 · 발표',
    title: '전달받은 발표 영상,\n누가 등록했을까요?',
    description: '공개 전에 영상을 등록해 두면, 전달받은 사람도 등록 기록을 확인할 수 있습니다.',
    evidence: '등록자 · 등록 시각',
    method: '등록 기록과 보증서에서 이 영상을 등록한 사람과 등록 시각을 확인합니다.',
    first: '발표 영상', second: '등록 기록',
    note: '기관 소속과 공식 발표 권한은 별도 확인이 필요합니다.',
  },
  {
    id: 'creator', number: '02', audience: '크리에이터 · 시청자',
    title: '다시 공유된 영상,\n등록 영상과 같을까요?',
    description: '다른 플랫폼에서 접한 영상의 장면과 음성을 등록 영상과 비교합니다.',
    evidence: '영상·음성 비교 결과',
    method: '파일이 다르면 대표 장면과 음성 지문을 대조합니다. 파일 전체의 동일성을 뜻하지는 않습니다.',
    first: '등록 영상', second: '공유된 영상',
    note: '재인코딩·짧게 자른 영상은 후보 검색과 비교 기준을 충족해야 합니다.',
  },
  {
    id: 'work', number: '03', audience: '업무 · 현장 기록',
    title: '전달한 기록 파일,\n같은 파일일까요?',
    description: '현장 영상을 미리 등록하고, 주고받은 파일의 디지털 지문이 같은지 확인합니다.',
    evidence: '파일 전체의 정확 일치 여부',
    method: '파일 전체의 디지털 지문이 같은지 확인하고, 등록 기록과 보증서도 함께 검증합니다.',
    first: '등록 파일', second: '전달 파일',
    note: '등록한 원본 파일은 직접 보관하세요. 등록 시각은 촬영 시각과 다릅니다.',
  },
]
</script>

<template>
  <div class="use-cases-page">
    <header class="uc-hero">
      <div class="uc-hero-inner">
      <span class="uc-eyebrow">진본 활용 사례</span>
      <h1>영상이 전해지는 순간마다,<br /><span>확인할 근거를 함께.</span></h1>
      <p>미리 등록한 영상으로, 나중에 확인할 기준을 만듭니다.</p>
      </div>
    </header>

    <section class="uc-section" aria-label="세 가지 활용 예">
      <div class="uc-content">
      <div class="uc-cases">
        <article v-for="item in cases" :key="item.id" class="uc-case" :class="item.id">
          <div class="uc-case-top"><span>{{ item.audience }}</span><span class="uc-number">{{ item.number }}</span></div>
          <h2>{{ item.title }}</h2>

          <div class="uc-visual" aria-hidden="true">
            <div class="uc-object">
              <svg v-if="item.id !== 'work'" viewBox="0 0 72 54" fill="none"><rect x="1" y="1" width="70" height="52" rx="9"/><path d="m30 17 16 10-16 10V17Z"/></svg>
              <svg v-else viewBox="0 0 54 64" fill="none"><path d="M10 1h24l19 19v35a8 8 0 0 1-8 8H10a9 9 0 0 1-9-9V10a9 9 0 0 1 9-9Z"/><path d="M34 1v19h19M13 35h28M13 43h28M13 51h18"/></svg>
              <span>{{ item.first }}</span>
            </div>
            <span class="uc-connector"><svg viewBox="0 0 44 16" fill="none"><path d="M1 8h40m-6-6 6 6-6 6"/></svg></span>
            <div class="uc-object uc-object-target">
              <svg v-if="item.id === 'announcement'" viewBox="0 0 54 64" fill="none"><rect x="1" y="1" width="52" height="62" rx="8"/><circle cx="27" cy="21" r="7"/><path d="M16 39c0-12 22-12 22 0M13 49h28M19 55h16"/></svg>
              <svg v-else-if="item.id === 'creator'" viewBox="0 0 72 54" fill="none"><rect x="1" y="1" width="70" height="52" rx="9"/><path d="m30 17 16 10-16 10V17Z"/></svg>
              <svg v-else viewBox="0 0 54 64" fill="none"><path d="M10 1h24l19 19v35a8 8 0 0 1-8 8H10a9 9 0 0 1-9-9V10a9 9 0 0 1 9-9Z"/><path d="M34 1v19h19M13 35h28M13 43h28M13 51h18"/></svg>
              <span>{{ item.second }}</span>
            </div>
          </div>

          <p class="uc-description">{{ item.description }}</p>
          <div class="uc-evidence"><span>확인할 수 있는 것</span><strong>{{ item.evidence }}</strong><p>{{ item.method }}</p></div>
          <details class="uc-detail"><summary>이 사례의 확인 범위</summary><p>{{ item.note }}</p></details>
        </article>
      </div>
      <p class="uc-caption">사전에 등록된 영상을 기준으로 한 활용 예입니다. 실제 도입 실적이나 검증 결과를 나타내지 않습니다.</p>

      <section class="uc-steps" aria-labelledby="uc-steps-title">
        <span class="uc-eyebrow">공통 이용 방법</span>
        <h2 id="uc-steps-title">미리 등록하고, 필요할 때 확인하세요.</h2>
        <ol>
          <li><span class="uc-step-number" aria-hidden="true">1</span><div><h3>영상과 보증서 준비</h3><p>본인확인 후 앱에서 영상을 등록하고 등록 보증서를 발급받습니다.</p><a href="/downloads">iOS 앱 · 배포 준비 중 →</a></div></li>
          <li><span class="uc-step-number" aria-hidden="true">2</span><div><h3>파일이나 링크로 비교</h3><p>웹에서 파일·URL을 입력하거나, YouTube·Instagram에서 Chrome 확장으로 검증을 시작합니다.</p><a href="/downloads">이용 방법 보기 →</a></div></li>
          <li><span class="uc-step-number" aria-hidden="true">3</span><div><h3>확인 방식까지 읽기</h3><p>파일 정확 일치와 영상·음성 비교를 구분하고, 등록 증거와 상세 사유를 함께 확인합니다.</p><a href="/verification-status">결과 읽는 방법 →</a></div></li>
        </ol>
      </section>

      <div class="uc-scope">
        <div><strong>등록 기록과 비교 결과를 확인합니다.</strong><p>영상 내용의 사실성·AI 생성 여부·제작자·저작권자 여부는 보증하지 않습니다. 등록 기록을 찾지 못해도 가짜라는 뜻은 아닙니다.</p></div>
        <a href="/verification-status">검증 범위 알아보기 <span aria-hidden="true">→</span></a>
      </div>
      </div>
    </section>

    <section class="uc-start" aria-labelledby="uc-start-title">
      <div><h2 id="uc-start-title">확인하고 싶은 영상이 있나요?</h2><p>파일이나 링크로 시작하세요. 로그인은 필요 없습니다.</p></div>
      <a class="uc-primary" href="https://jinbon-web.vercel.app">영상 확인하기 <span aria-hidden="true">↗</span></a>
    </section>
    <nav class="uc-more" aria-label="다른 시작 방법">
      <a href="/downloads">영상을 등록하고 싶다면 <span>앱 이용 안내 →</span></a>
      <a href="/developers/guide/introduction">서비스에 연결하고 싶다면 <span>개발자 센터 →</span></a>
    </nav>
  </div>
</template>

<style scoped>
.use-cases-page { color: var(--jb-ink); }
.uc-hero { padding: 88px 24px; background: linear-gradient(150deg, var(--jb-blue-light), var(--jb-bg) 75%); border-bottom: 1px solid var(--jb-border); }
.uc-hero-inner { max-width: 1120px; margin: auto; }
.uc-eyebrow { display: block; font-size: 13px; font-weight: 700; color: var(--jb-blue); margin-bottom: 18px; }
.uc-hero h1 { font-size: clamp(30px, 3.3vw, 44px); font-weight: 750; line-height: 1.35; letter-spacing: -.04em; margin: 0 0 24px; }
.uc-hero h1 span { color: var(--jb-blue); }
.uc-hero-inner > p { font-size: 19px; line-height: 1.8; margin: 0; color: var(--jb-text-secondary); }
.uc-section { padding: 80px 24px; background: var(--jb-bg-alt); }
.uc-content, .uc-more { max-width: 1040px; margin-left: auto; margin-right: auto; }
.uc-cases { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; align-items: start; }
.uc-case { border: 1px solid var(--jb-border); border-radius: 16px; padding: 28px; background: var(--jb-bg); }
.uc-case-top { display: flex; justify-content: space-between; align-items: center; color: var(--jb-blue); font-size: 12px; font-weight: 650; }
.uc-case-top > span:first-child { padding: 4px 9px; border-radius: 6px; background: var(--jb-blue-light); font-size: 11px; font-weight: 600; }
.uc-number { color: var(--jb-text-secondary); font-variant-numeric: tabular-nums; }
.uc-case h2 { white-space: pre-line; font-size: 19px; font-weight: 650; letter-spacing: -.02em; line-height: 1.5; margin: 18px 0 22px; }
.uc-visual { display: flex; align-items: center; justify-content: center; gap: 12px; height: 130px; border: 1px solid var(--jb-blue-border); border-radius: 12px; background: var(--jb-blue-light); color: var(--jb-blue); }
.uc-object { display: flex; flex-direction: column; align-items: center; gap: 14px; min-width: 72px; }
.uc-object > svg { height: 54px; width: 64px; stroke: currentColor; stroke-width: 1.6; }
.uc-object > span { font-size: 11px; font-weight: 600; }
.uc-object-target > svg { stroke-width: 2.2; }
.uc-connector { width: 28px; margin-bottom: 25px; }
.uc-connector svg { width: 100%; stroke: currentColor; stroke-width: 1.4; }
.uc-description { font-size: 15px; color: var(--jb-text-secondary); line-height: 1.8; margin: 22px 0; min-height: 108px; }
.uc-evidence { border-top: 1px solid var(--jb-border); padding-top: 18px; }
.uc-evidence span { display: block; font-size: 11px; color: var(--jb-text-secondary); margin-bottom: 6px; }
.uc-evidence strong { display: block; font-size: 16px; font-weight: 650; }
.uc-evidence p { font-size: 13px; line-height: 1.8; color: var(--jb-text-secondary); margin: 10px 0 0; }
.uc-detail { margin-top: 18px; }
.uc-detail summary { cursor: pointer; padding: 8px 0; font-size: 12px; color: var(--jb-text-secondary); }
.uc-detail p { font-size: 13px; line-height: 1.8; color: var(--jb-text-secondary); margin: 8px 0 0; }
.uc-caption { font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); margin: 16px 0 28px; }
.uc-steps { margin: 52px 0 32px; }
.uc-steps h2 { font-size: 30px; line-height: 1.45; font-weight: 700; letter-spacing: -.025em; margin: 0 0 28px; }
.uc-steps ol { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; list-style: none; margin: 0; padding: 0; }
.uc-steps li { display: flex; gap: 12px; align-items: flex-start; }
.uc-step-number { display: grid; place-items: center; flex-shrink: 0; width: 28px; height: 28px; border-radius: 50%; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 12px; font-weight: 700; }
.uc-steps h3 { font-size: 16px; font-weight: 650; margin: 0 0 8px; }
.uc-steps p { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.8; margin: 0 0 12px; }
.uc-steps a { color: var(--jb-blue); font-size: 12px; text-decoration: underline; text-underline-offset: 4px; }
.uc-scope { display: flex; justify-content: space-between; align-items: center; gap: 24px; padding: 24px 28px; background: var(--jb-blue-light); border-radius: 14px; }
.uc-scope strong { font-size: 14px; font-weight: 600; }
.uc-scope p { font-size: 13px; line-height: 1.8; color: var(--jb-text-secondary); margin: 5px 0 0; }
.uc-scope a { color: var(--jb-blue); font-size: 13px; font-weight: 600; flex-shrink: 0; }
.uc-scope a:hover, .uc-more a:hover span { text-decoration: underline; text-underline-offset: 4px; }
.uc-start { padding: 72px 24px 80px; text-align: center; background: var(--jb-blue-light); }
.uc-start h2 { font-size: 30px; line-height: 1.45; font-weight: 700; letter-spacing: -.025em; margin: 0 0 8px; }
.uc-start p { margin: 0 0 28px; font-size: 16px; color: var(--jb-text-secondary); line-height: 1.8; }
.uc-primary { flex-shrink: 0; display: inline-flex; align-items: center; justify-content: center; gap: 14px; border-radius: 10px; padding: 13px 22px; border: 1px solid transparent; background: var(--jb-blue-solid); color: white; font-size: 15px; font-weight: 650; }
.uc-primary:hover { background: var(--jb-blue-solid-hover); }
.uc-more { display: flex; flex-wrap: wrap; gap: 12px 32px; padding: 24px; justify-content: center; }
.uc-more a { font-size: 12px; color: var(--jb-text-secondary); line-height: 1.8; }
.uc-more span { color: var(--jb-blue); font-weight: 600; margin-left: 6px; }
@media (min-width: 769px) and (max-width: 1000px) {
  .uc-hero { padding: 64px 24px; }
  .uc-cases { gap: 14px; }
  .uc-case { padding: 24px; }
  .uc-case h2 { min-height: 86px; }
  .uc-visual { gap: 6px; }
  .uc-object { min-width: 52px; }
  .uc-object > svg { width: 52px; }
}
@media (max-width: 768px) {
  .uc-hero { padding: 48px 20px; }
  .uc-hero h1 { font-size: 32px; }
  .uc-hero-inner > p { font-size: 17px; }
  .uc-section { padding: 52px 20px; }
  .uc-cases { grid-template-columns: 1fr; gap: 16px; }
  .uc-case { padding: 24px; }
  .uc-visual { gap: 22px; }
  .uc-description { min-height: 0; margin: 18px 0; }
  .uc-scope { flex-direction: column; align-items: flex-start; gap: 14px; padding: 24px; }
  .uc-steps { margin-top: 36px; }
  .uc-steps h2 { font-size: 26px; }
  .uc-steps ol { grid-template-columns: 1fr; }
  .uc-start { padding: 52px 20px; }
  .uc-start h2 { font-size: 26px; }
  .uc-more { flex-direction: column; align-items: center; padding: 24px 20px; }
}
</style>
