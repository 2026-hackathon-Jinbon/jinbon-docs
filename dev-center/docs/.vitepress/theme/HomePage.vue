<script setup lang="ts">
import VerificationDemo from './VerificationDemo.vue'

function openStorageInfo() {
  const detail = document.getElementById('original-storage') as HTMLDetailsElement | null
  if (detail) detail.open = true
}

const facts = [
  { number: '01', label: '등록자', title: '누가 등록했는지', text: '모바일 신분증으로 본인확인을 마친 등록자의 정보를 살펴보세요.', sample: '김진본', detail: '등록자 · 가상 예시', kind: 'person' },
  { number: '02', label: '등록 시각', title: '언제 등록했는지', text: '진본에 영상의 기록을 남긴 시점을 확인하세요.', sample: '2026. 09. 01.', detail: '등록 시각 · 가상 예시', kind: 'date' },
  { number: '03', label: '비교 결과', title: '등록 영상과 일치하는지', text: '같은 파일인지, 장면과 음성이 대응하는지 확인하세요.', sample: '등록 파일과 일치', detail: '파일 정확 일치 · 가상 예시', kind: 'match' },
  { number: '04', label: '디지털 보증서(VC)', title: '보증서가 유효한지', text: '보증서의 유효성과, 보증서에 담긴 등록 정보가 해당 영상과 맞는지 확인합니다.', sample: '등록 보증서 유효', detail: '등록 정보 일치 · 가상 예시', kind: 'certificate' },
]
const cases = [
  { id: 'announcement', label: 'SNS에서 본 발표', title: '피드에서 본 이 발표,\n그 영상이 맞을까요?', text: '영상의 등록자와 등록 기록, 장면·음성의 비교 결과를 살펴보세요.', visual: 'message', sub: '피드 속 영상, 등록 기록부터.' },
  { id: 'creator', label: '짧게 잘린 영상', title: '짧은 장면의\n앞뒤가 궁금할 때.', text: '등록 영상과 대응하는 구간을 확인하고, 전체 맥락도 살펴보세요.', visual: 'clip', sub: '등록 영상과 비교해 보세요.' },
  { id: 'work', label: '업무와 현장 기록', title: '주고받은 파일이\n같은지 분명하게.', text: '전달 전에 영상을 등록해 두고, 받은 파일과 정확히 같은지 확인하세요.', visual: 'file', sub: '등록한 파일과 같아요.' },
]
const faqs = [
  { question: '진본에서 확인하는 ‘출처’는 무엇인가요?', answer: '누가 언제 영상을 등록했는지, 지금 보는 영상이 그 등록 영상과 어떻게 일치하는지를 확인합니다. 인터넷에서 처음 게시된 곳이나 모든 공유 경로를 추적하는 것은 아닙니다.' },
  { question: '등록 기록이 없으면 가짜 영상인가요?', answer: '아니에요. 진본은 사전에 등록된 영상을 기준으로 비교합니다. 기록을 찾지 못했다면 현재 등록 영상과의 일치 여부를 확인할 수 없다는 뜻입니다. 원 게시자나 공식 채널에서 내용과 등록 여부를 확인해 주세요.' },
  { question: '등록된 영상이면 내용도 사실인가요?', answer: '진본이 확인하는 것은 등록 기록과 영상의 비교 결과입니다. 영상 속 내용의 사실성, AI 생성 여부, 촬영 원본 여부, 제작자·저작권자 여부까지 보증하지는 않습니다. 등록자 표시명만으로 기관 소속이나 공식 발표 권한이 인증되는 것도 아닙니다.' },
  { id: 'original-storage', question: '원본 미보관은 어떤 뜻인가요?', answer: '영상 원본을 장기 보관하지 않는다는 뜻이에요. 업로드하거나 링크에서 가져온 영상은 서버에서 분석하며, 분석용 임시 파일은 처리 후 삭제합니다. 영상의 지문과 등록 정보 등은 검증에 사용됩니다. 원본 파일은 직접 보관해 주세요.' },
  { question: '링크로 확인할 수 없는 영상도 있나요?', answer: '네. 지원하는 플랫폼의 공개 영상이어도 로그인 요구나 접근 제한에 따라 가져오지 못할 수 있습니다. 이때는 본인이 보유하고 검증에 사용할 권한이 있는 영상 파일을 직접 올려 주세요.' },
  { question: '제 영상을 등록하려면 어떻게 하나요?', answer: 'iOS 앱에서 모바일 신분증으로 본인확인을 마치고, 영상을 등록한 뒤 등록 보증서 발급까지 완료하는 과정입니다. 현재 앱은 배포 준비 중이에요. 시작하기 페이지에서 이용 준비와 등록 과정을 확인할 수 있습니다.' },
]
</script>

<template>
  <div class="home-page">
    <section class="hero" aria-labelledby="hero-title">
      <div class="container hero-grid">
        <div class="hero-copy">
          <p class="eyebrow"><span class="brand-dot" aria-hidden="true" />영상 출처·진본 확인 서비스</p>
          <h1 id="hero-title">SNS에서 만난 영상,<br />출처와 진본 여부를<br /><span>확인하세요.</span></h1>
          <p class="hero-description">SNS 링크를 넣고, 등록자와 영상 일치 여부,<br class="desktop-break" /> 디지털 보증서(VC)를 함께 확인하세요.</p>
          <div class="actions">
            <a href="https://jinbon-web.vercel.app" class="button primary">영상 확인하기 <span aria-hidden="true">↗</span></a>
            <a href="#experience" class="button secondary">결과 예시 보기 <span aria-hidden="true">↓</span></a>
          </div>
          <p class="hero-note">설치·로그인 없이 · <a href="#original-storage" @click="openStorageInfo">원본 미보관</a><br />사전에 진본에 등록된 영상을 기준으로 비교합니다.</p>
        </div>
        <figure class="hero-product" aria-label="SNS 링크 입력과 영상·음성 비교 기준을 통과한 결과의 가상 예시">
          <div class="product-canvas">
            <div class="video-window">
              <div class="window-bar"><span>SNS에서 복사한 영상 링크</span><span class="example-label">입력 예시</span></div>
              <div class="link-preview"><span aria-hidden="true">↗</span><span>sns.example/video/announcement</span></div>
              <div class="video-scene" aria-hidden="true">
                <div class="scene-top"><span>JINBON STORIES</span><span>01 / 03</span></div>
                <div class="scene-title">오늘의 소식을<br /><strong>전합니다.</strong></div>
                <div class="scene-bottom"><span class="play-symbol" /><div class="playback-track"><i /></div><span>00:12 / 00:30</span></div>
                <span class="scene-orbit orbit-one" /><span class="scene-orbit orbit-two" />
              </div>
            </div>
            <div class="result-card">
              <div class="result-top"><span class="result-icon" aria-hidden="true">✓</span><span>진본 확인</span><span class="result-brand">진본</span></div>
              <h2>등록 영상과 대응해요.</h2>
              <p class="comparison-label">영상·음성 비교 기준 통과</p>
              <div class="certificate-result"><span>디지털 보증서(VC)</span><strong><span aria-hidden="true">✓</span> 유효 · 등록 정보 일치</strong></div>
              <dl><div><dt>등록자</dt><dd>김진본 <span class="verified">본인확인 완료</span></dd></div><div><dt>등록 시각</dt><dd>2026. 09. 01. 10:30</dd></div></dl>
            </div>
          </div>
          <figcaption>링크 입력과 검증 결과를 보여주는 가상 예시입니다.</figcaption>
        </figure>
      </div>
      <div class="container hero-foot"><span>SNS 속 영상, 확인할 수 있는 근거부터.</span><a href="#what-to-check">진본 알아보기 <span aria-hidden="true">↓</span></a></div>
    </section>

    <section id="what-to-check" class="section" aria-labelledby="facts-title">
      <div class="container">
        <div class="section-heading"><p class="eyebrow">진본으로 확인하는 것</p><h2 id="facts-title">확인할 근거는<br />이 네 가지예요.</h2><p class="section-description">영상 비교 결과에 디지털 보증서(VC) 검증을 더해,<br class="desktop-break" /> 해당 영상의 등록 근거까지 확인합니다.</p></div>
        <div class="facts-grid">
          <article v-for="fact in facts" :key="fact.number" class="fact">
            <div class="fact-top"><span>{{ fact.number }}</span><span>{{ fact.label }}</span></div>
            <h3>{{ fact.title }}</h3><p>{{ fact.text }}</p>
            <div class="fact-sample"><span class="sample-icon" :class="fact.kind" aria-hidden="true">{{ fact.kind === 'person' ? '김' : fact.kind === 'date' ? '01' : fact.kind === 'certificate' ? 'VC' : '✓' }}</span><div><strong>{{ fact.sample }}</strong><span>{{ fact.detail }}</span></div></div>
          </article>
        </div>
        <p class="section-note">디지털 보증서(VC)는 해당 영상의 등록 사실을 담은 증명서입니다.<br />등록 시각은 촬영 시각과 다르며, 등록자 표시명이 기관의 공식 권한을 뜻하지는 않습니다.</p>
      </div>
    </section>

    <section id="using-jinbon" class="section experience-section" aria-labelledby="experience-title">
      <div class="container">
        <div class="section-heading centered"><p class="eyebrow">이렇게 사용하세요</p><h2 id="experience-title">SNS에서 본 영상,<br />링크로 확인해 보세요.</h2><p class="section-description">지원하는 공개 영상의 링크를 넣으면, 등록 영상과 비교해 드려요.</p></div>
        <ol class="steps">
          <li><span>1</span><div><strong>SNS에서 링크 복사</strong><p>보고 있는 영상의 공유 메뉴에서<br />영상 링크를 복사하세요.</p></div></li>
          <li><span>2</span><div><strong>진본에 링크 붙여넣기</strong><p>‘영상 확인하기’로 이동해<br />‘URL 검증’에 링크를 넣으세요.</p></div></li>
          <li><span>3</span><div><strong>등록자·비교 결과·VC 확인</strong><p>누가 등록했는지, 영상이 대응하는지,<br />보증서가 유효한지 살펴보세요.</p></div></li>
        </ol>
        <p class="input-alternative">파일로도 확인할 수 있어요. 검증 화면에서 ‘파일 업로드’를 선택하세요.</p>
        <div id="experience" class="demo-container">
          <div class="demo-heading"><h3>어떤 결과를 받게 될까요?</h3><span>상황을 선택해 살펴보세요 <span aria-hidden="true">↓</span></span></div>
          <VerificationDemo />
        </div>
        <div class="experience-footer"><p>확인할 영상이 준비됐나요?</p><a href="https://jinbon-web.vercel.app" class="text-link">내 영상 확인하기 <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>

    <section id="use-cases" class="section" aria-labelledby="cases-title">
      <div class="container">
        <div class="section-heading heading-row"><div><p class="eyebrow">이런 순간에, 진본</p><h2 id="cases-title">확인이 필요한 순간은<br />생각보다 가까이 있어요.</h2></div><a href="/use-cases" class="text-link">사용 사례 더 보기 <span aria-hidden="true">→</span></a></div>
        <div class="cases-grid">
          <a v-for="item in cases" :key="item.id" :href="'/use-cases#' + item.id" class="case">
            <div class="case-visual" :class="item.visual" aria-hidden="true">
              <template v-if="item.visual === 'message'"><span class="message-bubble">피드에서 본 이 발표, 어디서 왔을까?</span><span class="message-reply"><i class="mini-play" />SNS 영상 링크<span>↗</span></span><span class="visual-caption">{{ item.sub }}</span></template>
              <template v-else-if="item.visual === 'clip'"><span class="clip-label">등록 영상</span><div class="clip-track"><i v-for="n in 9" :key="n" :class="{ selected: n > 3 && n < 7 }" /></div><span class="clip-bracket">비교하는 구간</span><span class="visual-caption">{{ item.sub }}</span></template>
              <template v-else><div class="file-pair"><span class="mini-file">MP4</span><span class="pair-equal">=</span><span class="mini-file second">MP4</span></div><span class="visual-caption"><span class="small-check">✓</span>{{ item.sub }}</span></template>
            </div>
            <div class="case-copy"><span class="case-label">{{ item.label }}</span><h3>{{ item.title }}</h3><p>{{ item.text }}</p><span class="case-link">사용 방법 보기 <span aria-hidden="true">↗</span></span></div>
          </a>
        </div>
        <p class="section-note">사전에 등록된 영상을 기준으로 한 활용 예입니다. 일부 구간 비교는 후보 검색과 영상·음성 비교 기준을 충족해야 합니다.</p>
      </div>
    </section>

    <section id="how-it-works" class="section understanding-section" aria-labelledby="understanding-title">
      <div class="container understanding-grid">
        <div class="understanding-copy"><p class="eyebrow">결과를 이해하는 방법</p><h2 id="understanding-title">‘일치’라는 결과에,<br />확인한 근거를 함께.</h2><p>파일 또는 장면·음성을 비교하고,<br class="desktop-break" /> 등록 기록과 보증서가 유효한지 확인합니다.</p><a href="/verification-status" class="text-link">검증 결과 자세히 보기 <span aria-hidden="true">→</span></a></div>
        <div class="meaning-list">
          <div><span class="meaning-icon" aria-hidden="true">✓</span><div><h3>같은 파일인지, 일부 구간이 대응하는지</h3><p>확인 방식에 따라 결과의 의미가 달라요.<br />결과에 표시된 비교 방식도 함께 살펴보세요.</p></div></div>
          <div><span class="meaning-icon neutral" aria-hidden="true">−</span><div><h3>등록 기록이 없다고 가짜는 아니에요.</h3><p>비교할 기록을 찾지 못했다는 뜻이에요.<br />원 게시자나 공식 채널에서도 확인해 주세요.</p></div></div>
          <div><span class="meaning-icon neutral" aria-hidden="true">i</span><div><h3>영상의 내용과 맥락도 살펴보세요.</h3><p>등록 영상과의 일치가 영상 속 내용의 사실성이나<br class="desktop-break" /> 공식 발표 권한을 보증하지는 않아요.</p></div></div>
        </div>
      </div>
    </section>

    <section class="section faq-section" aria-labelledby="faq-title">
      <div class="container faq-grid">
        <div class="section-heading"><p class="eyebrow">자주 묻는 질문</p><h2 id="faq-title">궁금한 점을<br />먼저 확인하세요.</h2><div class="detail-links"><a id="audio-verification" href="/verification-details#audio-verification">영상·음성 비교 원리 <span aria-hidden="true">↗</span></a><a id="platform-plan" href="/verification-details#platform-plan">현재 데모와 앞으로의 계획 <span aria-hidden="true">↗</span></a></div></div>
        <div class="faq"><details v-for="item in faqs" :id="item.id" :key="item.question"><summary>{{ item.question }}<span aria-hidden="true">+</span></summary><p>{{ item.answer }}</p></details></div>
      </div>
    </section>

    <section class="closing" aria-labelledby="closing-title">
      <div class="container closing-inner"><p class="eyebrow">영상의 출처와 진본 여부, 진본에서</p><h2 id="closing-title">지금 보고 있는 영상,<br />진본에서 확인해 보세요.</h2><a href="https://jinbon-web.vercel.app" class="button primary">영상 확인하기 <span aria-hidden="true">↗</span></a><div class="closing-links"><a href="/downloads">영상을 등록하고 싶다면 <span aria-hidden="true">→</span></a><span>iOS 앱 · 배포 준비 중</span></div></div>
    </section>
  </div>
</template>

<style scoped>
.home-page { color: var(--jb-ink); background: var(--jb-bg); }
.container { width: min(1120px, calc(100% - 64px)); margin-inline: auto; }
.home-page h1, .home-page h2, .home-page h3, .home-page p, .home-page figure { margin: 0; }
.home-page h1, .home-page h2, .home-page h3 { letter-spacing: -.045em; text-wrap: balance; }
.home-page h2 { font-size: clamp(30px, 3.4vw, 42px); font-weight: 750; line-height: 1.4; }
.home-page h3 { font-weight: 700; line-height: 1.5; }
.home-page a, .home-page summary { -webkit-tap-highlight-color: transparent; }
.home-page a:focus-visible, .home-page summary:focus-visible { outline: 3px solid var(--jb-blue); outline-offset: 5px; }
.eyebrow { color: var(--jb-blue); font-size: 13px; font-weight: 650; letter-spacing: -.01em; line-height: 1.6; }
.hero { padding-top: 84px; }
.hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; align-items: center; }
.hero-copy { padding: 10px 0 26px; }
.hero-copy .eyebrow { display: flex; align-items: center; gap: 9px; margin-bottom: 26px; }
.brand-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--jb-blue); }
.hero h1 { font-size: clamp(42px, 4.7vw, 60px); line-height: 1.24; font-weight: 750; }
.hero h1 > span { color: var(--jb-blue); }
.hero .hero-description { margin-top: 25px; font-size: 18px; line-height: 1.85; color: var(--jb-text-secondary); }
.actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 32px; }
.button { min-height: 52px; display: inline-flex; align-items: center; justify-content: center; gap: 22px; border-radius: 10px; padding: 14px 22px; font-size: 15px; font-weight: 650; transition: background-color .2s; }
.primary { background: var(--jb-blue-solid); color: #fff; }
.primary:hover { background: var(--jb-blue-solid-hover); }
.secondary { color: var(--jb-text); background: var(--jb-bg-alt); border: 1px solid var(--jb-border); }
.secondary:hover { background: var(--jb-blue-light); }
.hero .hero-note { margin-top: 20px; font-size: 12px; line-height: 1.9; color: var(--jb-text-secondary); }
.hero-note a { text-decoration: underline; text-underline-offset: 3px; }
.hero-product { min-width: 0; }
.product-canvas { padding: 24px; position: relative; isolation: isolate; border-radius: 24px; background: radial-gradient(ellipse at 60% 58%, var(--jb-blue-light) 15%, var(--jb-bg-alt) 75%); }
.video-window { margin-right: 24px; background: var(--jb-bg); border: 1px solid var(--jb-border); border-radius: 14px; box-shadow: 0 12px 34px #1529570a; overflow: hidden; }
.window-bar { display: flex; align-items: center; gap: 8px; padding: 13px 15px 5px; font-size: 12px; color: var(--jb-text-secondary); }
.example-label { margin-left: auto; white-space: nowrap; }
.link-preview { display: flex; align-items: center; gap: 9px; padding: 0 15px 13px; font-size: 13px; color: var(--jb-text); }
.link-preview > span:first-child { color: var(--jb-blue); }
.link-preview > span:last-child { min-width: 0; overflow-wrap: anywhere; }
.video-scene { height: 170px; position: relative; isolation: isolate; overflow: hidden; background: #172942; color: #fff; padding: 18px 24px; }
.scene-top { display: flex; justify-content: space-between; color: #b5c5e1; font-size: 8px; letter-spacing: .14em; }
.scene-title { position: relative; z-index: 1; font-size: 25px; font-weight: 400; letter-spacing: -.04em; line-height: 1.45; padding-top: 12px; }
.scene-title strong { font-weight: 650; }
.scene-bottom { display: flex; align-items: center; gap: 12px; position: absolute; bottom: 20px; right: 24px; left: 24px; font-size: 8px; color: #d8e1ee; }
.play-symbol, .mini-play { width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 6px solid currentColor; }
.playback-track { flex: 1; height: 2px; background: #ffffff33; }
.playback-track i { display: block; width: 40%; height: 100%; background: #9db6ff; }
.scene-orbit { position: absolute; z-index: -1; width: 195px; height: 195px; border: 1px solid #7c9dd947; border-radius: 50%; right: -32px; top: 53px; }
.orbit-two { width: 275px; height: 275px; right: -72px; top: 13px; }
.result-card { position: relative; z-index: 2; margin: -12px 0 0 28px; padding: 22px 24px; border: 1px solid var(--jb-blue-border); border-radius: 14px; background: var(--jb-bg); box-shadow: 0 14px 38px #10285c12; }
.result-top { display: flex; align-items: center; gap: 7px; font-size: 13px; color: var(--jb-blue); font-weight: 650; }
.result-icon { display: grid; place-items: center; width: 20px; height: 20px; border-radius: 50%; background: var(--jb-blue-solid); color: #fff; font-size: 12px; }
.result-brand { margin-left: auto; color: var(--jb-text-secondary); font-size: 12px; font-weight: 750; }
.result-card h2 { font-size: 24px; margin-top: 12px; letter-spacing: -.045em; }
.result-card .comparison-label { margin-top: 5px; font-size: 13px; color: var(--jb-text-secondary); }
.certificate-result { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px 12px; margin-top: 16px; padding: 13px 14px; border: 1px solid var(--jb-blue-border); border-radius: 9px; background: var(--jb-blue-light); font-size: 13px; line-height: 1.8; }
.certificate-result strong { color: var(--jb-blue); font-weight: 650; }
.result-card dl { display: grid; gap: 9px; margin: 16px 0 0; }
.result-card dl > div { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; font-size: 13px; line-height: 1.7; }
.result-card dt { color: var(--jb-text-secondary); flex-shrink: 0; }
.result-card dd { margin: 0; font-weight: 550; text-align: right; }
.verified { display: inline-block; color: var(--jb-blue); margin-left: 4px; font-size: 12px; }
.hero-product figcaption { margin-top: 12px; font-size: 12px; line-height: 1.8; text-align: center; color: var(--jb-text-secondary); }
.hero-foot { display: flex; align-items: center; justify-content: space-between; gap: 20px; margin-top: 62px; padding-block: 25px; border-top: 1px solid var(--jb-border); font-size: 12px; color: var(--jb-text-secondary); }
.hero-foot a { display: inline-flex; align-items: center; gap: 16px; min-height: 32px; color: var(--jb-text); }
.section { padding-block: 104px; scroll-margin-top: 84px; }
.section-heading { margin-bottom: 44px; }
.section-heading .eyebrow, .understanding-copy .eyebrow { margin-bottom: 15px; }
.facts-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); }
.fact { display: flex; flex-direction: column; padding-right: 20px; }
.fact + .fact { padding-left: 20px; border-left: 1px solid var(--jb-border); }
.fact:last-child { padding-right: 0; }
.fact-top { display: flex; align-items: center; gap: 10px; color: var(--jb-text-secondary); font-size: 11px; }
.fact-top > span:first-child { color: var(--jb-blue); font-variant-numeric: tabular-nums; }
.fact h3 { margin-top: 17px; font-size: 19px; }
.fact > p { margin-top: 10px; margin-bottom: 26px; font-size: 14px; line-height: 1.85; color: var(--jb-text-secondary); }
.fact-sample { display: flex; align-items: center; gap: 10px; padding: 16px 12px; margin-top: auto; border-radius: 10px; background: var(--jb-bg-alt); }
.sample-icon { display: grid; place-items: center; width: 38px; height: 38px; flex-shrink: 0; color: var(--jb-blue); background: var(--jb-blue-light); font-size: 15px; border-radius: 10px; }
.sample-icon.person { border-radius: 50%; font-size: 13px; }
.sample-icon.date { border-top: 4px solid var(--jb-blue); font-size: 13px; }
.sample-icon.certificate { font-size: 12px; font-weight: 700; border: 1px solid var(--jb-blue-border); }
.fact-sample strong { display: block; font-size: 13px; font-weight: 650; }
.fact-sample div > span { display: block; margin-top: 2px; font-size: 10px; color: var(--jb-text-secondary); }
.section .section-note { margin-top: 26px; font-size: 11px; line-height: 1.85; color: var(--jb-text-secondary); }
.experience-section, .understanding-section { background: var(--jb-bg-alt); }
.centered { text-align: center; }
.section-heading .section-description { margin-top: 20px; color: var(--jb-text-secondary); font-size: 16px; line-height: 1.85; }
.steps { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 30px; max-width: 920px; padding: 0; margin: 0 auto 24px; list-style: none; }
.steps li { display: flex; align-items: flex-start; gap: 13px; }
.steps li > span { display: grid; place-items: center; width: 30px; height: 30px; border-radius: 50%; color: var(--jb-blue); background: var(--jb-blue-light); font-size: 12px; font-weight: 700; flex-shrink: 0; }
.steps strong { font-size: 14px; line-height: 30px; font-weight: 650; }
.steps p { font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); margin-top: 3px; }
.home-page .input-alternative { margin: 0 0 40px; font-size: 13px; line-height: 1.8; color: var(--jb-text-secondary); text-align: center; }
.demo-container { scroll-margin-top: 92px; }
.demo-heading { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 18px; }
.demo-heading h3 { font-size: 19px; }
.demo-heading > span { color: var(--jb-text-secondary); font-size: 12px; }
.demo-heading > span > span { margin-left: 8px; }
.experience-footer { display: flex; align-items: center; justify-content: center; gap: 18px; margin-top: 28px; font-size: 13px; }
.experience-footer p { color: var(--jb-text-secondary); }
.text-link { display: inline-flex; align-items: center; gap: 18px; min-height: 36px; color: var(--jb-blue); font-weight: 600; font-size: 13px; }
.text-link:hover, .detail-links a:hover, .closing-links a:hover { text-decoration: underline; text-underline-offset: 5px; }
.heading-row { display: flex; align-items: flex-end; justify-content: space-between; gap: 28px; }
.cases-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 26px; }
.case { display: flex; flex-direction: column; min-width: 0; border-radius: 14px; }
.case-visual { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 190px; border-radius: 14px; background: var(--jb-bg-alt); padding: 24px; overflow: hidden; transition: background-color .2s; }
.case:hover .case-visual { background: var(--jb-blue-light); }
.case-copy { display: flex; flex-direction: column; align-items: flex-start; flex: 1; padding-top: 25px; }
.case-label { color: var(--jb-blue); font-size: 11px; font-weight: 600; }
.case h3 { font-size: 24px; white-space: pre-line; margin-top: 12px; }
.case p { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.85; margin-top: 13px; margin-bottom: 21px; }
.case-link { display: flex; gap: 18px; align-items: center; color: var(--jb-text); font-size: 12px; min-height: 32px; margin-top: auto; }
.message-bubble { align-self: flex-start; margin-left: 8px; padding: 12px 15px; border: 1px solid var(--jb-border); border-radius: 12px 12px 12px 3px; background: var(--jb-bg); color: var(--jb-text); font-size: 11px; box-shadow: 0 3px 12px #15295705; }
.message-reply { display: flex; align-items: center; gap: 10px; align-self: flex-end; padding: 13px 16px; margin: 10px 5px 0 0; border-radius: 12px 12px 3px 12px; background: var(--jb-blue-light); font-size: 10px; color: var(--jb-blue); border: 1px solid var(--jb-blue-border); }
.message-reply > span { margin-left: 12px; }
.visual-caption { font-size: 10px; color: var(--jb-text-secondary); margin-top: 20px; }
.clip-label { font-size: 10px; color: var(--jb-text-secondary); align-self: flex-start; margin-bottom: 12px; }
.clip-track { display: grid; grid-template-columns: repeat(9, minmax(0, 1fr)); gap: 4px; width: 100%; }
.clip-track i { height: 39px; border: 1px solid var(--jb-blue-border); background: var(--jb-blue-light); border-radius: 3px; }
.clip-track i.selected { background: var(--jb-blue-solid); border-color: var(--jb-blue-solid); }
.clip-bracket { width: 33%; min-width: 82px; font-size: 9px; color: var(--jb-blue); text-align: center; border: solid var(--jb-blue); border-width: 0 1px 1px; padding-top: 10px; margin-top: 6px; }
.clip .visual-caption { margin-top: 12px; }
.file-pair { display: flex; align-items: center; gap: 22px; }
.mini-file { display: grid; place-items: center; width: 49px; height: 64px; border: 1px solid var(--jb-blue-border); border-radius: 7px; background: var(--jb-bg); font-size: 10px; font-weight: 650; color: var(--jb-blue); transform: rotate(-8deg); box-shadow: 0 3px 12px #15295705; }
.mini-file.second { transform: rotate(8deg); background: var(--jb-blue-light); }
.pair-equal { font-size: 21px; color: var(--jb-blue); }
.small-check { margin-right: 5px; color: var(--jb-blue); }
.understanding-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 90px; align-items: center; }
.understanding-copy > p:not(.eyebrow) { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; margin-top: 22px; }
.understanding-copy .text-link { margin-top: 20px; }
.meaning-list { display: grid; gap: 28px; }
.meaning-list > div { display: flex; gap: 16px; align-items: flex-start; }
.meaning-list > div + div { border-top: 1px solid var(--jb-border); padding-top: 26px; }
.meaning-icon { display: grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 14px; flex-shrink: 0; }
.meaning-icon.neutral { background: var(--jb-gray-bg); color: var(--jb-text-secondary); }
.meaning-list h3 { font-size: 16px; line-height: 28px; }
.meaning-list p { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.85; margin-top: 9px; }
.faq-grid { display: grid; grid-template-columns: .8fr 1.2fr; gap: 70px; }
.faq-grid .section-heading { margin: 0; }
.detail-links { display: grid; justify-items: start; margin-top: 27px; gap: 5px; }
.detail-links a { display: flex; align-items: center; gap: 14px; min-height: 36px; color: var(--jb-text-secondary); font-size: 12px; scroll-margin-top: 110px; }
.faq details { border-bottom: 1px solid var(--jb-border); }
.faq details[id] { scroll-margin-top: 110px; }
.faq details:target { background: var(--jb-blue-light); }
.faq details:first-child { border-top: 1px solid var(--jb-border); }
.faq summary { display: flex; justify-content: space-between; align-items: center; gap: 18px; cursor: pointer; font-size: 15px; line-height: 1.75; font-weight: 600; padding: 23px 0; list-style: none; }
.faq summary::-webkit-details-marker { display: none; }
.faq summary > span { color: var(--jb-text-secondary); font-size: 20px; font-weight: 400; flex-shrink: 0; }
.faq details[open] summary > span { transform: rotate(45deg); }
.faq details > p { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.95; padding-bottom: 24px; }
.closing { padding-block: 88px 92px; background: var(--jb-blue-light); }
.closing-inner { text-align: center; }
.closing h2 { margin-top: 18px; }
.closing .button { margin-top: 30px; }
.closing-links { display: flex; justify-content: center; align-items: center; gap: 13px; margin-top: 22px; font-size: 11px; flex-wrap: wrap; }
.closing-links a { display: inline-flex; align-items: center; gap: 8px; min-height: 32px; color: var(--jb-text); }
.closing-links > span { color: var(--jb-text-secondary); }

@media (max-width: 1024px) {
  .hero { padding-top: 60px; }
  .hero h1 { font-size: clamp(34px, 4.3vw, 44px); }
  .hero-grid { gap: 24px; }
  .hero .hero-description { font-size: 16px; }
  .button { gap: 15px; padding-inline: 18px; font-size: 14px; }
  .product-canvas { padding: 16px; }
  .video-window { margin-right: 10px; }
  .result-card { margin-left: 10px; padding: 18px; }
  .result-card h2 { font-size: 22px; }
  .facts-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); row-gap: 36px; }
  .fact { padding-right: 24px; }
  .fact + .fact { padding-left: 24px; }
  .fact:nth-child(2n) { padding-right: 0; }
  .fact:nth-child(2n + 1) { padding-left: 0; border-left: 0; }
  .fact h3 { font-size: 18px; }
  .fact-sample { padding: 14px 12px; gap: 9px; }
  .fact-sample strong { font-size: 12px; }
  .cases-grid { gap: 20px; }
  .case-visual { padding: 18px; }
  .case h3 { font-size: 22px; }
  .understanding-grid, .faq-grid { gap: 40px; }
}
@media (max-width: 760px) {
  .container { width: calc(100% - 40px); }
  .hero { padding-top: 28px; }
  .hero-grid { grid-template-columns: 1fr; gap: 24px; }
  .hero-copy { padding: 0; }
  .hero-copy .eyebrow { margin-bottom: 14px; }
  .hero h1 { font-size: clamp(34px, 8vw, 60px); }
  .hero .hero-description { font-size: 16px; margin-top: 16px; }
  .actions { margin-top: 22px; }
  .hero .hero-note { margin-top: 12px; }
  .hero-product { width: 100%; max-width: 510px; justify-self: center; }
  .product-canvas { padding: 0; background: none; }
  .video-window { margin: 0 8px; border-radius: 12px 12px 0 0; background: var(--jb-bg-alt); }
  .video-scene { display: none; }
  .result-card { margin: -1px 0 0; padding: 20px; }
  .hero-foot { margin-top: 38px; padding-block: 20px; font-size: 10px; }
  .hero-foot > span { max-width: 195px; line-height: 1.75; }
  .hero-foot a { flex-shrink: 0; gap: 7px; }
  .section { padding-block: 68px; }
  .section-heading { margin-bottom: 32px; }
  .home-page h2 { font-size: 31px; }
  .result-card h2 { font-size: 23px; }
  .facts-grid { grid-template-columns: 1fr; gap: 26px; }
  .fact, .fact + .fact { padding: 0; border: 0; }
  .fact + .fact { border-top: 1px solid var(--jb-border); padding-top: 26px; }
  .fact h3 { margin-top: 12px; font-size: 21px; }
  .fact > p { margin-bottom: 18px; }
  .fact-sample { padding: 16px; }
  .fact-sample strong { font-size: 14px; }
  .section .section-note { font-size: 11px; }
  .section-heading .section-description { font-size: 14px; }
  .steps { grid-template-columns: 1fr; gap: 22px; max-width: 320px; }
  .steps li { gap: 16px; }
  .steps strong { font-size: 15px; }
  .steps p { font-size: 13px; }
  .demo-heading { flex-direction: column; align-items: flex-start; gap: 6px; }
  .demo-heading h3 { font-size: 18px; }
  .experience-footer { gap: 8px; flex-wrap: wrap; }
  .heading-row { align-items: flex-start; flex-direction: column; gap: 16px; }
  .cases-grid { grid-template-columns: 1fr; gap: 34px; }
  .case-visual { height: 200px; padding: 24px 36px; }
  .case-copy { padding-top: 20px; }
  .case h3 { font-size: 24px; }
  .case p { font-size: 14px; margin-bottom: 13px; }
  .case-link { min-height: 44px; }
  .message-bubble { margin-left: 10%; }
  .message-reply { margin-right: 10%; }
  .understanding-grid, .faq-grid { grid-template-columns: 1fr; gap: 34px; }
  .understanding-copy > p:not(.eyebrow) { font-size: 14px; }
  .meaning-list h3 { font-size: 15px; }
  .faq summary { font-size: 14px; padding-block: 21px; }
  .closing { padding-block: 64px; }
  .closing-links { flex-direction: column; gap: 0; }
  .desktop-break { display: none; }
}
@media (max-width: 360px) {
  .container { width: calc(100% - 32px); }
  .hero h1 { font-size: 32px; }
  .actions { gap: 8px; }
  .button { font-size: 13px; padding-inline: 14px; gap: 11px; }
  .result-card { padding: 18px 16px; }
  .result-card h2 { font-size: 22px; }
}
@media (prefers-reduced-motion: reduce) {
  .button, .case-visual { transition: none; }
}
</style>
