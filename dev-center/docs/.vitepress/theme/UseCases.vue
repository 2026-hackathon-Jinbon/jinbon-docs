<script setup lang="ts">
import { useCases } from './useCases'
</script>

<template>
  <div class="use-cases-page">
    <header class="uc-hero">
      <div class="uc-inner"><span class="eyebrow">진본 활용 사례</span><h1>“같은 영상이 맞나요?”<br /><span>그 질문에 답할 근거를 남기세요.</span></h1><p>발표를 전하고, 콘텐츠를 공유하고, 업무 기록을 주고받을 때.<br />미리 등록한 영상이 나중에 확인할 기준이 됩니다.</p>
        <nav class="case-nav" aria-label="관심 있는 활용 사례"><a v-for="item in useCases" :key="item.id" :href="`#${item.id}`"><span aria-hidden="true">{{ item.number }}</span>{{ item.audience }} <span aria-hidden="true">↓</span></a></nav>
      </div>
    </header>
    <div class="uc-inner stories">
      <article v-for="item in useCases" :id="item.id" :key="item.id" class="story">
        <div class="story-heading"><span class="story-number" aria-hidden="true">{{ item.number }}</span><div><span class="eyebrow">{{ item.audience }}</span><h2>{{ item.title }}</h2></div></div>
        <div class="story-body">
          <blockquote>{{ item.question }}</blockquote>
          <div class="comparison"><div class="before"><span class="comparison-label">이런 고민이 있다면</span><p>{{ item.before }}</p></div><div class="after"><span class="comparison-label">이렇게 확인할 수 있어요</span><p>{{ item.after }}</p></div></div>
          <ol class="story-flow" aria-label="활용 순서"><li v-for="(step, index) in item.steps" :key="step"><span class="step-number" aria-hidden="true">{{ index + 1 }}</span>{{ step }}</li></ol>
          <div class="evidence"><span>확인할 수 있는 것</span><strong>{{ item.evidence }}</strong></div><p class="scope">{{ item.note }}</p>
          <a class="story-link" href="/#experience">결과 예시로 살펴보기 <span aria-hidden="true">→</span></a>
        </div>
      </article>
      <p class="caption">사전에 등록된 영상을 기준으로 한 활용 예입니다. 실제 고객 사례나 도입 실적을 나타내지 않습니다.</p>
    </div>
    <section class="uc-start">
      <div class="uc-inner start-grid">
        <div><span class="eyebrow">파일 없이 먼저 살펴보세요</span><h2>결과를 보면,<br />조금 더 분명해집니다.</h2><p>같은 파일, 짧게 자른 영상, 등록 기록이 없는 영상.<br />세 가지 상황에서 무엇을 확인할 수 있는지 알아보세요.</p><a class="primary" href="/#experience">결과 예시 살펴보기 <span aria-hidden="true">→</span></a></div>
        <div class="start-guide"><h3>직접 확인하거나, 더 알아보세요.</h3><a href="https://jinbon-web.vercel.app"><span>확인할 영상이 있다면<strong>웹에서 영상 확인하기</strong></span><span aria-hidden="true">↗</span></a><a href="/downloads"><span>등록 과정이 궁금하다면 · 앱 배포 준비 중<strong>등록·이용 방법 보기</strong></span><span aria-hidden="true">→</span></a><a href="/verification-status"><span>어디까지 확인할 수 있는지<strong>검증 결과와 한계 알아보기</strong></span><span aria-hidden="true">→</span></a></div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.use-cases-page { color: var(--jb-ink); }
.uc-inner { max-width: 1120px; margin: auto; }
.uc-hero { padding: 72px 24px 44px; background: radial-gradient(ellipse at 85% 20%, var(--jb-blue-light), transparent 65%), var(--jb-bg); border-bottom: 1px solid var(--jb-border); }
.eyebrow { display: block; color: var(--jb-blue); font-size: 12px; font-weight: 650; margin-bottom: 18px; }
h1 { font-size: clamp(30px, 3.1vw, 43px); line-height: 1.4; letter-spacing: -.045em; font-weight: 750; margin: 0 0 24px; }
h1 span { color: var(--jb-blue); }
.uc-hero p { font-size: 16px; line-height: 1.9; color: var(--jb-text-secondary); margin: 0; }
.case-nav { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }
.case-nav a { display: inline-flex; align-items: center; gap: 14px; padding: 13px 18px; border: 1px solid var(--jb-border); border-radius: 10px; background: var(--jb-bg); font-size: 13px; font-weight: 600; }
.case-nav a:hover { border-color: var(--jb-blue); color: var(--jb-blue); }
.case-nav a > span:first-child { font-size: 10px; color: var(--jb-blue); font-variant-numeric: tabular-nums; }
.stories { padding: 0 24px 56px; max-width: 1168px; }
.story { display: grid; grid-template-columns: 1fr 1.8fr; gap: 64px; padding: 64px 0; border-bottom: 1px solid var(--jb-border); scroll-margin-top: 72px; }
.story-heading { display: flex; flex-direction: column; align-items: flex-start; }
.story-number { font-size: 48px; letter-spacing: -.05em; line-height: 1; color: var(--jb-blue); font-weight: 400; margin-bottom: 36px; }
h2 { white-space: pre-line; font-size: 30px; line-height: 1.5; letter-spacing: -.035em; font-weight: 700; margin: 0; }
blockquote { margin: 0 0 24px; font-size: 20px; font-weight: 600; line-height: 1.7; letter-spacing: -.025em; }
.comparison { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.comparison > div { padding: 22px; border-radius: 12px; }
.before { background: var(--jb-bg-alt); border: 1px solid var(--jb-border); }
.after { background: var(--jb-blue-light); border: 1px solid var(--jb-blue-border); }
.comparison-label { font-size: 12px; font-weight: 650; color: var(--jb-text-secondary); }
.after .comparison-label { color: var(--jb-blue); }
.comparison p { font-size: 14px; line-height: 1.9; color: var(--jb-text); margin: 12px 0 0; }
.story-flow { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; padding: 20px 0; margin: 12px 0 0; list-style: none; }
.story-flow li { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--jb-text-secondary); }
.step-number { flex-shrink: 0; display: grid; place-items: center; width: 22px; height: 22px; border: 1px solid var(--jb-blue-border); border-radius: 50%; color: var(--jb-blue); font-size: 10px; }
.evidence { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px 20px; padding-top: 20px; border-top: 1px solid var(--jb-border); font-size: 13px; }
.evidence > span { color: var(--jb-text-secondary); }
.evidence strong { font-weight: 600; }
.scope, .caption { font-size: 12px; line-height: 1.85; color: var(--jb-text-secondary); margin: 14px 0 0; }
.story-link { display: inline-flex; gap: 14px; color: var(--jb-blue); font-size: 13px; font-weight: 600; padding: 12px 0; margin-top: 8px; }
.story-link:hover { text-decoration: underline; text-underline-offset: 4px; }
.caption { margin-top: 24px; }
.uc-start { padding: 72px 24px; background: var(--jb-blue-light); }
.start-grid { display: grid; grid-template-columns: 1.3fr 1fr; gap: 80px; align-items: center; }
.uc-start h2 { font-size: 32px; }
.uc-start p { font-size: 14px; line-height: 1.9; color: var(--jb-text-secondary); margin: 18px 0 24px; }
.primary { display: inline-flex; align-items: center; justify-content: center; gap: 20px; padding: 14px 22px; border-radius: 10px; font-size: 14px; font-weight: 650; background: var(--jb-blue-solid); color: white; }
.primary:hover { background: var(--jb-blue-solid-hover); }
.start-guide { background: var(--jb-bg); border: 1px solid var(--jb-blue-border); border-radius: 16px; padding: 28px; }
.start-guide h3 { font-size: 18px; font-weight: 650; margin: 0 0 18px; }
.start-guide a { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 16px 0; border-top: 1px solid var(--jb-border); color: var(--jb-blue); }
.start-guide a > span:first-child { font-size: 11px; color: var(--jb-text-secondary); }
.start-guide strong { display: block; font-size: 13px; font-weight: 600; margin-top: 6px; color: var(--jb-blue); }
.start-guide a:hover strong { text-decoration: underline; text-underline-offset: 4px; }
@media (max-width: 1000px) {
  .story { gap: 32px; grid-template-columns: 1fr 1.6fr; }
  h2 { font-size: 26px; }
  .start-grid { gap: 36px; }
}
@media (max-width: 768px) {
  .uc-hero { padding: 44px 20px 32px; }
  h1 { font-size: 30px; }
  .uc-hero p { font-size: 14px; }
  .case-nav { gap: 8px; margin-top: 24px; }
  .case-nav a { padding: 12px; font-size: 12px; gap: 8px; }
  .stories { padding: 0 20px 36px; }
  .story { grid-template-columns: 1fr; gap: 24px; padding: 40px 0; }
  .story-heading { flex-direction: row; gap: 20px; }
  .story-number { font-size: 32px; margin: 0; }
  .story-heading .eyebrow { margin-bottom: 10px; font-size: 11px; }
  h2 { font-size: 25px; }
  blockquote { font-size: 18px; }
  .comparison { grid-template-columns: 1fr; }
  .comparison > div { padding: 20px; }
  .story-flow { grid-template-columns: 1fr; gap: 12px; padding: 16px 0 22px; }
  .uc-start { padding: 48px 20px; }
  .start-grid { grid-template-columns: 1fr; gap: 32px; }
  .uc-start h2 { font-size: 28px; }
  .start-guide { padding: 24px; }
}
</style>
