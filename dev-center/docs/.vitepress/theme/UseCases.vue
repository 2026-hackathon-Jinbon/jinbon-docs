<script setup lang="ts">
import { useCases } from './useCases'
</script>

<template>
  <div class="use-cases-page">
    <header class="uc-hero">
      <div class="uc-inner">
        <p class="eyebrow">진본 사용 사례</p>
        <h1>지금 보고 있는 영상,<br /><span>출처와 진본 여부가 궁금할 때.</span></h1>
        <p class="hero-description">SNS 피드의 발표, 쇼츠와 릴스 속 짧은 발언.<br />영상의 등록 기록과 비교 결과를 확인하는 과정을 살펴보세요.</p>
        <nav class="case-nav" aria-label="관심 있는 사용 사례로 이동">
          <a v-for="item in useCases" :key="item.id" :href="'#' + item.id">
            <div class="nav-top"><span>{{ item.number }}</span><span>{{ item.audience }}</span></div>
            <strong>{{ item.navTitle }}</strong>
            <span class="nav-action">확인 과정 보기 <span aria-hidden="true">↓</span></span>
          </a>
        </nav>
        <p class="hero-note">사전에 진본에 등록된 영상을 기준으로 한 활용 예입니다. 실제 고객 사례나 도입 실적을 나타내지 않습니다.</p>
      </div>
    </header>

    <section v-for="item in useCases" :id="item.id" :key="item.id" class="story" :aria-labelledby="item.id + '-title'">
      <div class="uc-inner">
        <div class="story-heading">
          <p class="eyebrow"><span class="story-number">{{ item.number }}</span>{{ item.audience }}</p>
          <h2 :id="item.id + '-title'">{{ item.title }}</h2>
          <p class="story-description">{{ item.situation }}</p>
        </div>

        <div class="example-workspace">
          <div class="scenario" :class="item.id">
            <div class="panel-heading"><span>{{ item.id === 'work' ? '이런 영상을 받았다면' : 'SNS에서 이런 영상을 봤다면' }}</span><span class="example-tag">가상 예시</span></div>
            <div v-if="item.id === 'announcement'" class="feed-scene" aria-label="SNS 피드에서 발표 영상을 접한 상황의 가상 예시">
              <div class="feed-account"><span class="avatar" aria-hidden="true">소</span><span>오늘의 소식 · 예시 계정</span></div>
              <p class="feed-caption">오늘 올라온 발표 영상이에요.</p>
              <div class="shared-video">
                <div class="video-slate" aria-hidden="true"><span>JINBON STORIES</span><strong>오늘의 소식을<br />전합니다.</strong><div class="video-controls"><i /><span>발표 영상 · 예시</span></div></div>
                <div class="video-caption"><span>{{ item.file }}</span><span>MP4</span></div>
              </div>
              <p class="visual-caption">SNS에서 영상 링크를 복사하고,<br />진본의 ‘URL 검증’에 붙여넣으세요.</p>
            </div>

            <figure v-else-if="item.id === 'creator'" class="timeline-scene">
              <div class="clip-preview" aria-hidden="true"><span class="clip-format">6초 클립</span><strong>짧은 장면 뒤에,<br />더 긴 이야기가 있어요.</strong><span>{{ item.file }}</span></div>
              <div class="timeline-label"><span>등록 영상</span><span>12초</span></div>
              <div class="timeline-track" aria-hidden="true"><i v-for="n in 12" :key="n" :class="{ matched: n > 3 && n <= 9 }" /></div>
              <div class="time-labels" aria-hidden="true"><span>0초</span><span>3초</span><span>9초</span><span>12초</span></div>
              <div class="matched-range"><span>제출한 6초 영상</span></div>
              <figcaption>등록 영상의 3–9초 구간에 대응하는 개념 예시입니다.</figcaption>
            </figure>

            <div v-else class="file-scene" aria-label="등록한 현장 기록과 전달받은 파일을 비교하는 가상 예시">
              <div class="file-comparison">
                <div class="file-example"><span class="file-label">등록한 파일</span><div class="file-sheet" aria-hidden="true"><span>MP4</span><i /><i /><i /></div><strong>현장기록.mp4</strong></div>
                <span class="equal-sign" aria-hidden="true">=</span>
                <div class="file-example"><span class="file-label">받은 파일</span><div class="file-sheet received" aria-hidden="true"><span>MP4</span><i /><i /><i /></div><strong>현장기록_전달본.mp4</strong></div>
              </div>
              <div class="file-match"><span aria-hidden="true">✓</span> 파일 전체의 디지털 지문 일치</div>
              <p class="visual-caption">파일 이름 대신, 파일 전체가 같은지 비교합니다.</p>
            </div>
          </div>

          <div class="result-panel">
            <div class="panel-heading"><span>진본에서 확인한 근거</span><span class="example-tag">가상 결과 예시</span></div>
            <span class="result-status"><span aria-hidden="true">✓</span>{{ item.resultLabel }}</span>
            <h3>{{ item.resultTitle }}</h3>
            <p class="result-description">{{ item.resultDescription }}</p>
            <dl class="result-evidence">
              <div><dt>등록자</dt><dd>김진본 <span class="identity-badge">본인확인 완료</span></dd></div>
              <div><dt>등록 시각</dt><dd>2026. 09. 01. 10:30</dd></div>
              <div><dt>영상 비교</dt><dd>{{ item.comparison }}</dd></div>
              <div class="vc-row"><dt>디지털 보증서(VC)</dt><dd><span class="evidence-check" aria-hidden="true">✓</span> 유효 · 등록 정보 일치</dd></div>
            </dl>
            <div class="next-action"><span>결과를 확인했다면</span><p>{{ item.next }}</p></div>
          </div>
        </div>

        <ol class="story-flow" aria-label="등록하는 사람과 확인하는 사람의 이용 순서">
          <li v-for="(step, index) in item.steps" :key="step.title"><span class="step-number" aria-hidden="true">{{ index + 1 }}</span><div><span class="step-who">{{ step.who }}</span><h3>{{ step.title }}</h3><p>{{ step.text }}</p></div></li>
        </ol>
        <div class="story-foot"><p>{{ item.note }}</p><a href="/#experience">다른 결과도 살펴보기 <span aria-hidden="true">→</span></a></div>
      </div>
    </section>

    <section class="shared-evidence" aria-labelledby="shared-evidence-title">
      <div class="uc-inner evidence-grid">
        <div><p class="eyebrow">모든 사례에서 함께 확인해요</p><h2 id="shared-evidence-title">영상 비교에,<br />등록 근거까지.</h2><p class="evidence-intro">영상의 일치 여부와 함께 블록체인 등록 기록,<br class="desktop-break" /> 디지털 보증서(VC)를 확인합니다.</p><a href="/verification-details" class="text-link">검증 원리 자세히 보기 <span aria-hidden="true">→</span></a></div>
        <div class="evidence-notes">
          <div><span class="evidence-icon" aria-hidden="true">VC</span><div><h3>보증서가 이 영상의 기록과 맞는지</h3><p>보증서의 유효성과 발급자·등록자 정보를 확인하고, 해당 영상의 등록 기록에 연결되는지 대조해요.</p></div></div>
          <div><span class="evidence-icon neutral" aria-hidden="true">i</span><div><h3>누가 등록했는지 확인해요.</h3><p>모바일 신분증으로 본인확인을 마친 등록자의 정보예요. SNS 게시 계정과의 소유 관계나 기관 소속·발표 권한은 해당 공식 채널에서 별도로 확인해 주세요.</p></div></div>
          <div><span class="evidence-icon neutral" aria-hidden="true">i</span><div><h3>등록 사실과 영상 속 사실은 달라요.</h3><p>보증서는 영상의 등록 사실을 담아요. 영상 내용의 사실성, AI 생성 여부나 저작권까지 보증하지는 않아요.</p></div></div>
          <div><span class="evidence-icon neutral" aria-hidden="true">−</span><div><h3>기록이 없다고 가짜는 아니에요.</h3><p>현재 비교할 기록을 찾지 못했다는 뜻이에요. 원 게시자나 공식 채널에서 내용과 등록 여부를 확인해 주세요.</p></div></div>
        </div>
      </div>
    </section>

    <section class="uc-start" aria-labelledby="start-title">
      <div class="uc-inner">
        <p class="eyebrow">이제, 내 영상으로</p><h2 id="start-title">확인할 영상이 있나요?</h2>
        <p>등록자부터 디지털 보증서까지,<br class="mobile-break" /> 확인할 근거를 함께 살펴보세요.</p>
        <div class="start-actions"><a href="https://jinbon-web.vercel.app" class="button primary">영상 확인하기 <span aria-hidden="true">↗</span></a><a href="/#experience" class="button secondary">결과 예시 먼저 보기 <span aria-hidden="true">→</span></a></div>
        <div class="registration-link"><a href="/downloads">내 영상 등록 방법 보기 <span aria-hidden="true">→</span></a><span>iOS 앱 · 배포 준비 중</span></div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.use-cases-page { color: var(--jb-ink); background: var(--jb-bg); }
.uc-inner { width: min(1120px, calc(100% - 64px)); margin-inline: auto; }
h1, h2, h3, p, figure { margin: 0; }
h1, h2, h3 { letter-spacing: -.045em; text-wrap: balance; }
h2 { font-size: clamp(30px, 3.4vw, 42px); line-height: 1.4; font-weight: 750; }
h3 { font-weight: 650; line-height: 1.5; }
a:focus-visible { outline: 3px solid var(--jb-blue); outline-offset: 5px; }
.eyebrow { color: var(--jb-blue); font-size: 13px; font-weight: 650; line-height: 1.6; margin-bottom: 18px; }
.uc-hero { padding-block: 74px 36px; }
h1 { font-size: clamp(36px, 4.5vw, 56px); line-height: 1.3; font-weight: 750; }
h1 > span { color: var(--jb-blue); }
.hero-description { font-size: 17px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 24px; }
.case-nav { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 44px; }
.case-nav a { display: flex; flex-direction: column; padding: 24px 26px 20px; border: 1px solid var(--jb-border); border-radius: 14px; background: var(--jb-bg-alt); transition: border-color .2s, background-color .2s; }
.case-nav a:hover { border-color: var(--jb-blue-border); background: var(--jb-blue-light); }
.nav-top { display: flex; gap: 10px; align-items: center; font-size: 11px; color: var(--jb-text-secondary); }
.nav-top > span:first-child { color: var(--jb-blue); font-variant-numeric: tabular-nums; }
.case-nav strong { white-space: pre-line; font-size: 22px; line-height: 1.5; letter-spacing: -.035em; margin-top: 15px; font-weight: 650; }
.nav-action { display: flex; align-items: center; justify-content: space-between; margin-top: 22px; padding-top: 14px; border-top: 1px solid var(--jb-border); font-size: 11px; color: var(--jb-text-secondary); }
.nav-action > span { color: var(--jb-blue); }
.hero-note { margin-top: 20px; color: var(--jb-text-secondary); font-size: 11px; line-height: 1.85; }
.story { padding-block: 80px; scroll-margin-top: 64px; }
.story + .story { border-top: 1px solid var(--jb-border); }
.story-heading { margin-bottom: 32px; }
.story-heading .eyebrow { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }
.story-number { display: grid; place-items: center; height: 26px; width: 30px; border-radius: 6px; background: var(--jb-blue-light); font-size: 11px; font-variant-numeric: tabular-nums; }
.story-heading h2 { white-space: pre-line; font-size: clamp(29px, 3.1vw, 38px); }
.story-description { max-width: 660px; font-size: 15px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 19px; }
.example-workspace { display: grid; grid-template-columns: 1fr 1.12fr; border: 1px solid var(--jb-border); border-radius: 20px; overflow: hidden; }
.scenario { min-width: 0; background: var(--jb-bg-alt); border-right: 1px solid var(--jb-border); padding: 28px; }
.panel-heading { display: flex; align-items: center; justify-content: space-between; gap: 12px; font-size: 11px; color: var(--jb-text-secondary); line-height: 1.7; }
.panel-heading > span:first-child { font-weight: 600; }
.example-tag { font-size: 10px; flex-shrink: 0; color: var(--jb-text-secondary); }
.feed-scene { max-width: 340px; margin: 26px auto 0; }
.feed-account { display: flex; align-items: center; gap: 9px; font-size: 11px; color: var(--jb-text-secondary); }
.avatar { display: grid; place-items: center; width: 29px; height: 29px; border-radius: 50%; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 11px; }
.feed-caption { margin: 14px 0; font-size: 13px; line-height: 1.85; color: var(--jb-text); }
.shared-video { border: 1px solid var(--jb-border); border-radius: 12px; background: var(--jb-bg); overflow: hidden; }
.video-slate { background: #172942; color: #fff; padding: 20px; }
.video-slate > span { color: #b5c5e1; font-size: 8px; letter-spacing: .15em; }
.video-slate strong { display: block; font-size: 25px; font-weight: 550; letter-spacing: -.04em; line-height: 1.4; margin-top: 20px; }
.video-controls { display: flex; align-items: center; gap: 10px; margin-top: 25px; color: #b5c5e1; font-size: 9px; }
.video-controls i { width: 0; height: 0; border-top: 4px solid transparent; border-bottom: 4px solid transparent; border-left: 6px solid currentColor; }
.video-caption { display: flex; justify-content: space-between; gap: 10px; padding: 10px 14px; font-size: 11px; }
.video-caption > span:last-child { font-size: 9px; color: var(--jb-text-secondary); }
.visual-caption { font-size: 11px; line-height: 1.85; color: var(--jb-text-secondary); text-align: center; margin-top: 23px; }
.timeline-scene { margin-top: 26px; }
.clip-preview { display: flex; flex-direction: column; align-items: flex-start; padding: 24px; border: 1px solid var(--jb-blue-border); border-radius: 12px; background: var(--jb-blue-light); color: var(--jb-blue); }
.clip-format { padding: 3px 8px; border: 1px solid var(--jb-blue-border); border-radius: 5px; font-size: 10px; }
.clip-preview strong { font-size: 23px; font-weight: 600; line-height: 1.5; letter-spacing: -.035em; margin-top: 18px; }
.clip-preview > span:last-child { margin-top: 21px; font-size: 10px; color: var(--jb-text-secondary); }
.timeline-label { display: flex; justify-content: space-between; margin: 25px 0 10px; font-size: 11px; color: var(--jb-text-secondary); }
.timeline-track { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 4px; }
.timeline-track i { height: 31px; background: var(--jb-blue-light); border: 1px solid var(--jb-blue-border); border-radius: 3px; }
.timeline-track i.matched { background: var(--jb-blue-solid); border-color: var(--jb-blue-solid); }
.time-labels { display: grid; grid-template-columns: 1fr 2fr 1fr; position: relative; font-size: 9px; color: var(--jb-text-secondary); margin-top: 5px; height: 18px; }
.time-labels > span { position: absolute; }
.time-labels > span:nth-child(2) { left: 25%; transform: translateX(-50%); }
.time-labels > span:nth-child(3) { left: 75%; transform: translateX(-50%); }
.time-labels > span:last-child { right: 0; }
.matched-range { width: 50%; margin: 2px auto 0; border: solid var(--jb-blue); border-width: 0 1px 1px; padding-bottom: 6px; color: var(--jb-blue); font-size: 10px; text-align: center; }
.timeline-scene figcaption { margin-top: 16px; font-size: 11px; line-height: 1.85; text-align: center; color: var(--jb-text-secondary); }
.file-scene { display: flex; flex-direction: column; justify-content: center; min-height: 391px; }
.file-comparison { display: grid; grid-template-columns: minmax(0, 1fr) 24px minmax(0, 1fr); gap: 12px; align-items: center; }
.file-example { display: flex; align-items: center; flex-direction: column; min-width: 0; }
.file-label { color: var(--jb-text-secondary); font-size: 11px; }
.file-sheet { width: 86px; height: 112px; background: var(--jb-bg); border: 1px solid var(--jb-blue-border); border-radius: 10px; margin-top: 17px; padding: 18px; box-shadow: 0 6px 16px #15295705; }
.file-sheet span { color: var(--jb-blue); font-size: 14px; font-weight: 650; }
.file-sheet i { display: block; height: 3px; border-radius: 2px; background: var(--jb-blue-border); margin-top: 8px; }
.file-sheet i:last-child { width: 65%; }
.file-sheet.received { background: var(--jb-blue-light); }
.file-example strong { font-size: 10px; font-weight: 550; line-height: 1.85; margin-top: 16px; text-align: center; overflow-wrap: anywhere; }
.equal-sign { font-size: 25px; color: var(--jb-blue); text-align: center; }
.file-match { display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 32px; font-size: 12px; color: var(--jb-blue); }
.file-match > span { display: grid; place-items: center; height: 23px; width: 23px; border-radius: 50%; background: var(--jb-blue-light); }
.result-panel { min-width: 0; padding: 28px 32px; }
.result-status { display: inline-flex; align-items: center; gap: 7px; padding: 4px 9px; border-radius: 5px; margin-top: 26px; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 11px; font-weight: 600; }
.result-panel h3 { font-size: 26px; margin-top: 13px; }
.result-description { font-size: 13px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 10px; }
.result-evidence { margin: 22px 0; padding-top: 10px; border-top: 1px solid var(--jb-border); }
.result-evidence > div { display: flex; align-items: baseline; justify-content: space-between; gap: 14px; padding-block: 8px; font-size: 13px; line-height: 1.85; }
.result-evidence dt { color: var(--jb-text-secondary); flex-shrink: 0; }
.result-evidence dd { margin: 0; text-align: right; font-weight: 550; }
.identity-badge { display: inline-block; font-size: 12px; color: var(--jb-blue); margin-left: 5px; }
.result-evidence .vc-row { flex-wrap: wrap; gap: 4px 12px; margin-top: 10px; padding: 12px 14px; background: var(--jb-blue-light); border: 1px solid var(--jb-blue-border); border-radius: 9px; }
.vc-row dd { color: var(--jb-blue); }
.evidence-check { margin-right: 3px; }
.next-action { background: var(--jb-bg-alt); padding: 15px 18px; border-radius: 9px; }
.next-action > span { font-size: 11px; color: var(--jb-text); font-weight: 650; }
.next-action p { margin-top: 6px; font-size: 12px; line-height: 1.85; color: var(--jb-text-secondary); }
.story-flow { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 32px; list-style: none; margin: 30px 0 0; padding: 0; }
.story-flow li { display: flex; align-items: flex-start; gap: 12px; }
.step-number { display: grid; place-items: center; width: 27px; height: 27px; flex-shrink: 0; border-radius: 50%; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 11px; }
.step-who { font-size: 10px; color: var(--jb-text-secondary); }
.story-flow h3 { font-size: 15px; margin-top: 4px; }
.story-flow p { font-size: 12px; line-height: 1.85; color: var(--jb-text-secondary); margin-top: 7px; }
.story-foot { display: flex; align-items: flex-start; justify-content: space-between; gap: 32px; margin-top: 26px; border-top: 1px solid var(--jb-border); padding-top: 19px; }
.story-foot p { max-width: 740px; font-size: 11px; line-height: 1.9; color: var(--jb-text-secondary); }
.story-foot a { display: inline-flex; gap: 13px; color: var(--jb-blue); font-size: 12px; flex-shrink: 0; min-height: 32px; align-items: center; }
.story-foot a:hover, .text-link:hover, .registration-link a:hover { text-decoration: underline; text-underline-offset: 5px; }
.shared-evidence { padding-block: 88px; background: var(--jb-bg-alt); }
.evidence-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; }
.evidence-intro { font-size: 15px; color: var(--jb-text-secondary); line-height: 1.9; margin-top: 22px; }
.text-link { display: inline-flex; align-items: center; gap: 16px; min-height: 44px; margin-top: 16px; font-size: 13px; font-weight: 600; color: var(--jb-blue); }
.evidence-notes { display: grid; gap: 24px; }
.evidence-notes > div { display: flex; align-items: flex-start; gap: 15px; }
.evidence-notes > div + div { padding-top: 24px; border-top: 1px solid var(--jb-border); }
.evidence-icon { display: grid; place-items: center; flex-shrink: 0; width: 32px; height: 32px; border-radius: 8px; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 11px; font-weight: 650; }
.evidence-icon.neutral { background: var(--jb-gray-bg); color: var(--jb-text-secondary); border-radius: 50%; font-size: 14px; }
.evidence-notes h3 { font-size: 16px; line-height: 32px; }
.evidence-notes p { font-size: 13px; color: var(--jb-text-secondary); line-height: 1.85; margin-top: 7px; }
.uc-start { padding-block: 82px; text-align: center; }
.uc-start > .uc-inner > p:not(.eyebrow) { margin-top: 18px; font-size: 15px; line-height: 1.9; color: var(--jb-text-secondary); }
.start-actions { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-top: 29px; }
.button { display: inline-flex; align-items: center; justify-content: center; gap: 20px; min-height: 52px; padding: 13px 22px; border-radius: 10px; font-size: 14px; font-weight: 650; transition: background-color .2s; }
.primary { color: #fff; background: var(--jb-blue-solid); }
.primary:hover { background: var(--jb-blue-solid-hover); }
.secondary { border: 1px solid var(--jb-border); background: var(--jb-bg-alt); }
.secondary:hover { background: var(--jb-blue-light); }
.registration-link { display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 14px; margin-top: 22px; font-size: 11px; }
.registration-link a { display: inline-flex; align-items: center; min-height: 32px; gap: 8px; color: var(--jb-text); }
.registration-link > span { color: var(--jb-text-secondary); }
.mobile-break { display: none; }

@media (max-width: 1024px) {
  .case-nav a { padding-inline: 20px; }
  .case-nav strong { font-size: 20px; }
  .example-workspace { grid-template-columns: 1fr 1.1fr; }
  .scenario { padding: 22px; }
  .result-panel { padding: 22px; }
  .result-panel h3 { font-size: 23px; }
  .result-evidence > div { gap: 9px; }
  .identity-badge { display: block; margin-left: 0; }
  .story-flow { gap: 22px; }
  .story-foot { gap: 24px; }
  .evidence-grid { gap: 40px; }
}
@media (max-width: 760px) {
  .uc-inner { width: calc(100% - 40px); }
  .uc-hero { padding-block: 44px 24px; }
  h1 { font-size: clamp(32px, 7.3vw, 44px); }
  h2 { font-size: 31px; }
  .hero-description { font-size: 15px; margin-top: 19px; }
  .case-nav { grid-template-columns: 1fr; gap: 10px; margin-top: 30px; }
  .case-nav a { display: grid; grid-template-columns: 1fr auto; column-gap: 12px; padding: 17px 20px; }
  .nav-top { grid-column: 1; font-size: 10px; }
  .case-nav strong { grid-column: 1; font-size: 18px; margin-top: 7px; white-space: normal; }
  .nav-action { grid-column: 2; grid-row: 1 / 3; align-self: center; margin: 0; border: 0; padding: 0; gap: 9px; font-size: 10px; }
  .hero-note { font-size: 10px; margin-top: 16px; }
  .story { padding-block: 50px; }
  .story-heading h2 { font-size: 29px; }
  .story-description { font-size: 14px; margin-top: 16px; }
  .example-workspace { grid-template-columns: 1fr; border-radius: 15px; }
  .scenario { padding: 22px; border-right: 0; border-bottom: 1px solid var(--jb-border); }
  .feed-scene { max-width: 340px; margin-top: 20px; }
  .feed-caption { font-size: 12px; }
  .video-slate { padding: 18px; }
  .video-slate strong { font-size: 22px; margin-top: 15px; }
  .video-controls { margin-top: 20px; }
  .visual-caption { font-size: 13px; margin-top: 18px; }
  .clip-preview { padding: 20px; }
  .clip-preview strong { font-size: 22px; }
  .timeline-scene { margin-top: 20px; }
  .file-scene { min-height: 290px; }
  .file-comparison { gap: 8px; }
  .file-sheet { width: 76px; height: 100px; padding: 14px; }
  .file-example strong { font-size: 9px; }
  .file-match { font-size: 11px; }
  .result-panel { padding: 24px 22px; }
  .result-status { margin-top: 22px; font-size: 12px; }
  .result-panel h3 { font-size: 23px; }
  .identity-badge { display: block; margin-left: 0; }
  .story-flow { grid-template-columns: 1fr; gap: 22px; margin-top: 26px; }
  .story-flow h3 { font-size: 15px; }
  .story-flow p { font-size: 13px; margin-top: 5px; }
  .story-foot { flex-direction: column; gap: 10px; margin-top: 23px; }
  .story-foot a { min-height: 44px; }
  .shared-evidence { padding-block: 60px; }
  .evidence-grid { grid-template-columns: 1fr; gap: 30px; }
  .evidence-intro { font-size: 14px; margin-top: 18px; }
  .evidence-notes h3 { font-size: 15px; }
  .uc-start { padding-block: 60px; }
  .uc-start > .uc-inner > p:not(.eyebrow) { font-size: 14px; }
  .button { padding-inline: 17px; gap: 13px; font-size: 13px; }
  .registration-link { flex-direction: column; gap: 0; }
  .mobile-break { display: initial; }
  .desktop-break { display: none; }
}
@media (max-width: 380px) {
  .uc-inner { width: calc(100% - 32px); }
  .case-nav a { padding-inline: 16px; }
  .case-nav strong { font-size: 17px; }
  .nav-action { font-size: 0; }
  .nav-action > span { font-size: 16px; }
  .scenario, .result-panel { padding-inline: 18px; }
  .result-panel h3 { font-size: 21px; }
  .result-evidence > div { flex-wrap: wrap; gap: 2px 12px; }
}
@media (prefers-reduced-motion: reduce) {
  .case-nav a, .button { transition: none; }
}
</style>
