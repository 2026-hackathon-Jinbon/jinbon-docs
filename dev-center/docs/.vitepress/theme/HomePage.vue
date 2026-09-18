<script setup lang="ts">
import VerificationDemo from './VerificationDemo.vue'
import { useCases } from './useCases'

const proofs = [
  { number: '01', title: '영상과 음성을 비교합니다', text: '파일이 정확히 같은지 먼저 확인합니다. 파일이 다르면 유사한 등록 영상을 찾아 대표 장면과 음성을 비교합니다.' },
  { number: '02', title: '등록 기록을 대조합니다', text: '블록체인에 남긴 영상의 대표 지문과 등록자 식별 정보 등을 대조하고, 등록이 유효한 상태인지 확인합니다.' },
  { number: '03', title: '등록 보증서를 확인합니다', text: '보증서의 유효성과 발급자·등록자 정보를 확인하고, 해당 영상의 등록 기록에 연결되는지 대조합니다.' },
]
const faqs = [
  { question: '진본에서 확인하는 ‘출처’는 무엇인가요?', answer: '누가 언제 영상을 등록했는지, 지금 보는 영상이 그 등록 영상과 어떻게 일치하는지를 확인합니다. 인터넷에서 처음 게시된 곳이나 모든 공유 경로를 추적하는 것은 아닙니다.' },
  { question: '등록 기록이 없으면 가짜 영상인가요?', answer: '아닙니다. 진본은 사전에 등록된 영상을 기준으로 비교합니다. 기록을 찾지 못했다면 등록 영상과의 일치 여부를 확인할 수 없다는 뜻입니다. 원 게시자나 공식 채널에서 발표 내용과 등록 여부를 확인하세요.' },
  { question: '등록 영상이면 내용도 사실인가요?', answer: '진본이 확인하는 것은 등록 기록과 영상의 비교 결과입니다. 영상 속 사건의 사실성, 촬영 원본 여부, AI 생성 여부, 제작자·저작권자 여부까지 보증하지는 않습니다.' },
  { question: '등록자 이름이 기관명이면 공식 발표인가요?', answer: '등록자 표시명만으로 기관 소속이나 공식 발표 권한이 인증되는 것은 아닙니다. 기관 홈페이지나 공식 채널에서 안내하는 등록자 정보와 발표 내용을 함께 확인하세요. 모바일 신분증을 통한 본인확인과 기관의 공식 권한 확인은 별개입니다.' },
  { question: '영상 파일은 어떻게 처리하나요?', answer: '영상은 분석을 위해 서버로 전송됩니다. 원본을 장기 보관하지 않으며, 분석용 임시 파일은 처리 후 삭제합니다. 등록한 영상의 지문과 등록 정보 등은 검증에 사용됩니다. 원본 파일은 직접 보관하세요.' },
  { question: '영상을 등록하려면 무엇이 필요한가요?', answer: 'iOS 앱에서 모바일 신분증으로 본인확인을 마치고 디지털 지갑을 연결해야 합니다. 영상 등록 후 보증서 발급도 완료해야 합니다. 현재 앱은 배포 준비 중이며, 시작하기 페이지에서 공개 후 설치 방법을 안내합니다.' },
]
</script>

<template>
  <div class="home-page">
    <section class="hero">
      <div class="hero-inner">
        <div class="hero-copy">
          <span class="eyebrow"><span class="brand-dot" aria-hidden="true" />영상 등록·검증 서비스, 진본</span>
          <h1>공유하기 전,<br /><span>영상의 출처를 확인하세요.</span></h1>
          <p class="hero-desc">누가 등록한 영상인지, 등록 영상과 일치하는지.<br class="desktop-break" /> 진본에서 확인하고 공유하세요.</p>
          <div class="actions">
            <a href="https://jinbon-web.vercel.app" class="btn primary">영상 확인하기 <span aria-hidden="true">↗</span></a>
            <a href="#experience" class="btn secondary">결과 예시 살펴보기 <span aria-hidden="true">↓</span></a>
          </div>
          <p class="hint">설치·로그인 없이, 사전에 등록된 영상과 비교합니다.<br />등록 기록이 없다는 이유만으로 가짜 영상은 아닙니다.</p>
        </div>
        <aside class="example" aria-label="가상의 파일 정확 일치 결과 예시">
          <div class="example-top"><span>공유하기 전에 확인할 정보</span><span class="example-mark">가상 예시</span></div>
          <div class="example-heading"><span class="check-icon" aria-hidden="true">✓</span><div><span class="success-label">파일 정확 일치</span><h2>등록 파일과 같아요.</h2></div></div>
          <dl class="identity">
            <div><dt>등록자 · 예시</dt><dd>김진본 <span class="identity-note">본인확인 완료</span></dd></div>
            <div><dt>등록 시각 · 예시</dt><dd>2026. 09. 01. 10:30</dd></div>
          </dl>
          <details class="example-detail"><summary>어떤 근거를 확인하나요?</summary><p>파일 전체의 디지털 지문이 같고, 블록체인 등록 기록과 등록 보증서가 유효한 경우입니다. 등록 시각은 촬영 시각과 다릅니다.</p></details>
          <p class="example-note">실제 검증 결과가 아닌 이해를 돕기 위한 예시입니다.</p>
        </aside>
      </div>
      <div class="hero-bottom"><span>누가 등록했는지</span><i aria-hidden="true" /><span>언제 등록했는지</span><i aria-hidden="true" /><span>등록 영상과 일치하는지</span></div>
    </section>

    <section id="use-cases" class="section cases-section">
      <div class="inner">
        <div class="section-heading"><div><span class="eyebrow">이런 순간에, 진본</span><h2>다시 공유하기 전에,<br />한 번 더 확인하세요.</h2></div><p class="heading-description">대화방에서 받은 발표부터 짧게 잘린 영상까지.<br />등록자와 비교 결과를 살펴보세요.</p></div>
        <div class="case-grid">
          <article v-for="item in useCases" :key="item.id" class="case-card">
            <div class="case-top"><span>{{ item.audience }}</span><span class="case-number" aria-hidden="true">{{ item.number }}</span></div>
            <h3>{{ item.title }}</h3>
            <p class="case-question">{{ item.question }}</p>
            <div class="case-outcome"><span>진본으로 확인할 수 있는 것</span><strong>{{ item.outcome }}</strong></div>
            <a :href="`/use-cases#${item.id}`" class="case-link">이 상황에서 사용하는 방법 <span aria-hidden="true">→</span></a>
          </article>
        </div>
        <p class="note">사전에 등록된 영상을 기준으로 한 활용 예입니다. 영상 내용의 사실성이나 제작자·저작권자 여부를 보증하지는 않습니다.</p>
      </div>
    </section>

    <section id="experience" class="section alternate">
      <div class="inner">
        <span class="eyebrow">파일 없이 먼저 살펴보세요</span>
        <h2>어떤 결과를 받게 될까요?</h2>
        <p class="intro">등록 영상과 일치할 때, 일부 구간이 대응할 때, 등록 기록을 찾지 못했을 때.<br class="desktop-break" /> 세 가지 가상 예시로 결과의 의미와 다음에 확인할 내용을 살펴보세요.</p>
        <VerificationDemo />
        <div class="demo-followup"><p>공유하려는 영상이 있다면</p><a href="https://jinbon-web.vercel.app">영상 확인하기 <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>

    <section id="using-jinbon" class="section">
      <div class="inner">
        <span class="eyebrow">등록부터 확인까지</span><h2>전하는 사람은 기록을 남기고,<br />공유하는 사람은 출처를 확인합니다.</h2>
        <div class="journeys">
          <article class="journey">
            <div class="journey-top"><span class="tag">영상을 전하는 사람</span><span class="availability">iOS 앱 · 배포 준비 중</span></div>
            <h3>공개 전에, 확인할 기준 남기기</h3>
            <ol><li><strong>본인확인</strong><p>모바일 신분증으로 본인확인을 마치고 디지털 지갑을 연결합니다.</p></li><li><strong>영상 등록</strong><p>공유할 영상의 디지털 지문을 계산해 블록체인에 등록합니다.</p></li><li><strong>보증서 발급</strong><p>지갑에서 발급 절차를 완료해 등록 보증서를 보관합니다.</p></li></ol>
            <div class="journey-bottom"><p>등록과 보증서 발급은 별도 단계입니다.<br />원본 파일은 직접 보관하세요.</p><a href="/downloads">앱 이용 준비 확인하기 <span aria-hidden="true">→</span></a></div>
          </article>
          <article class="journey viewer">
            <div class="journey-top"><span class="tag blue">영상을 보는 사람</span><span class="availability">웹 · 로그인 없이</span></div>
            <h3>다시 공유하기 전, 등록 정보 확인하기</h3>
            <ol><li><strong>공유받은 영상 선택</strong><p>웹에서 영상 파일을 올려 비교를 시작합니다.</p></li><li><strong>등록자와 비교 결과 확인</strong><p>누가 언제 등록했는지, 등록 영상과 어떻게 일치하는지 살펴보세요.</p></li><li><strong>확인이 더 필요하다면</strong><p>등록 기록이 없거나 출처가 불분명하면 원 게시자나 공식 채널에서 확인하세요.</p></li></ol>
            <div class="journey-bottom"><p>YouTube·Instagram에서는<br />Chrome 확장으로도 검증을 시작할 수 있습니다.</p><a href="https://jinbon-web.vercel.app">웹에서 영상 확인하기 <span aria-hidden="true">↗</span></a></div>
          </article>
        </div>
        <div class="other-channels"><span>평소 사용하는 곳에서도</span><a href="/downloads">Chrome 확장 설치 안내 <span aria-hidden="true">→</span></a><a href="https://pf.kakao.com/_xgtNBX">카카오톡 채널 안내 <span aria-hidden="true">↗</span></a></div>
      </div>
    </section>

    <section id="how-it-works" class="section proof-section">
      <div class="inner">
        <div class="section-heading"><div><span class="eyebrow">확인 결과를 뒷받침하는 근거</span><h2>영상의 일치 여부와<br />등록 기록을 함께 확인합니다.</h2></div><p class="heading-description">파일 정확 일치 또는 영상·음성 비교 기준을 통과하고,<br />등록 기록과 보증서가 유효해야 진본으로 표시합니다.</p></div>
        <div class="proof-grid"><article v-for="item in proofs" :key="item.number"><span class="proof-number">{{ item.number }}</span><h3>{{ item.title }}</h3><p>{{ item.text }}</p></article></div>
        <a class="text-link" href="/verification-status">확인 방식과 결과의 한계 자세히 보기 <span aria-hidden="true">→</span></a>
      </div>
    </section>

    <section class="section">
      <div class="inner faq-layout"><div><span class="eyebrow">궁금한 점을 먼저 확인하세요</span><h2>시작하기 전에.</h2><p class="heading-description">진본이 확인하는 범위와<br />이용에 필요한 내용을 모았습니다.</p></div><div class="faq"><details v-for="item in faqs" :key="item.question"><summary>{{ item.question }}</summary><p>{{ item.answer }}</p></details></div></div>
    </section>

    <section class="closing">
      <div class="inner closing-grid">
        <div><span class="eyebrow">공유 전 확인하는 습관, 진본</span><h2>공유하기 전,<br />영상의 출처를 확인하세요.</h2><p>누가 등록했는지, 등록 영상과 일치하는지 확인하세요.</p><a href="https://jinbon-web.vercel.app" class="btn primary">영상 확인하기 <span aria-hidden="true">↗</span></a></div>
        <div class="adoption"><span class="tag blue">더 알아보기</span><h3>등록 과정이 궁금하다면</h3><p>본인확인부터 영상 등록, 보증서 발급까지의 흐름을 살펴보세요. iOS 앱은 배포 준비 중입니다.</p><a href="/downloads">등록·이용 방법 보기 <span aria-hidden="true">→</span></a><a href="/developers/guide/introduction">기술 문서 살펴보기 <span aria-hidden="true">→</span></a></div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-page { color: var(--jb-ink); }
.hero { padding: 76px 24px 0; background: radial-gradient(ellipse at 85% 20%, var(--jb-blue-light), transparent 65%), var(--jb-bg); border-bottom: 1px solid var(--jb-border); }
.hero-inner { max-width: 1120px; margin: auto; display: grid; grid-template-columns: 1.5fr 1fr; gap: 56px; align-items: center; }
.hero-copy, .example { min-width: 0; }
.eyebrow { display: flex; align-items: center; gap: 8px; color: var(--jb-blue); font-size: 12px; font-weight: 650; margin-bottom: 20px; }
.brand-dot { height: 7px; width: 7px; background: var(--jb-blue); border-radius: 50%; }
h1 { font-size: clamp(30px, 3.1vw, 43px); line-height: 1.4; letter-spacing: -.045em; font-weight: 750; margin: 0 0 24px; text-wrap: balance; }
h1 span { color: var(--jb-blue); }
.hero-desc { font-size: 17px; line-height: 1.9; color: var(--jb-text); margin: 0 0 30px; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 16px; padding: 14px 20px; border-radius: 10px; font-size: 14px; font-weight: 650; border: 1px solid transparent; transition: background-color .15s, border-color .15s; }
.primary { background: var(--jb-blue-solid); color: white; }
.primary:hover { background: var(--jb-blue-solid-hover); }
.secondary { background: var(--jb-bg); border-color: var(--jb-border); }
.secondary:hover { border-color: var(--jb-blue); }
.hint { color: var(--jb-text-secondary); font-size: 12px; line-height: 1.8; margin: 18px 0 0; }
.example { background: var(--jb-bg); border: 1px solid var(--jb-blue-border); border-radius: 20px; padding: 26px; box-shadow: 0 16px 50px #2457e60a; }
.example-top { display: flex; align-items: center; justify-content: space-between; gap: 12px; font-size: 11px; color: var(--jb-text-secondary); }
.example-mark { border: 1px solid var(--jb-border); border-radius: 5px; padding: 2px 6px; }
.example-heading { display: flex; gap: 14px; align-items: center; margin: 28px 0 24px; }
.check-icon { flex-shrink: 0; display: grid; place-items: center; width: 42px; height: 42px; border-radius: 50%; background: var(--jb-green-bg); color: var(--jb-green); font-size: 23px; }
.success-label { font-size: 11px; color: var(--jb-green); font-weight: 650; }
.example h2 { font-size: 23px; margin: 4px 0 0; }
.identity { border: solid var(--jb-border); border-width: 1px 0; padding: 12px 0; margin: 0; }
.identity > div { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; font-size: 12px; padding: 8px 0; line-height: 1.7; }
.identity dt { color: var(--jb-text-secondary); }
.identity dd { margin: 0; font-weight: 600; }
.identity-note { font-size: 10px; color: var(--jb-blue); background: var(--jb-blue-light); border-radius: 4px; padding: 3px 5px; margin-left: 4px; white-space: nowrap; }
.example-detail summary { cursor: pointer; font-size: 12px; color: var(--jb-text); padding: 16px 0 8px; }
.example-detail p, .example-note { font-size: 11px; line-height: 1.8; color: var(--jb-text-secondary); margin: 8px 0 0; }
.hero-bottom { max-width: 1120px; margin: 56px auto 0; border-top: 1px solid var(--jb-border); display: flex; justify-content: center; align-items: center; gap: 28px; padding: 22px 0; font-size: 12px; color: var(--jb-text-secondary); }
.hero-bottom i { width: 3px; height: 3px; border-radius: 50%; background: var(--jb-blue); }
.section { padding: 88px 24px; scroll-margin-top: 80px; }
.inner { max-width: 1120px; margin: auto; }
h2 { font-size: 34px; line-height: 1.45; letter-spacing: -.035em; font-weight: 700; margin: 0 0 20px; }
h3 { font-size: 20px; line-height: 1.55; font-weight: 650; letter-spacing: -.025em; margin: 0 0 12px; }
.section-heading { display: flex; justify-content: space-between; align-items: flex-end; gap: 36px; margin-bottom: 36px; }
.section-heading h2 { margin: 0; }
.heading-description, .intro { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; margin: 0; }
.intro { margin-bottom: 32px; }
.alternate { background: var(--jb-bg-alt); }
.case-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
.case-card { display: flex; flex-direction: column; padding: 28px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); }
.case-top { display: flex; justify-content: space-between; gap: 12px; font-size: 11px; color: var(--jb-blue); font-weight: 600; margin-bottom: 24px; }
.case-number { font-variant-numeric: tabular-nums; color: var(--jb-text-secondary); font-weight: 400; }
.case-card h3 { white-space: pre-line; font-size: 22px; margin-bottom: 18px; }
.case-question { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.9; margin: 0 0 26px; }
.case-outcome { margin-top: auto; border-top: 1px solid var(--jb-border); padding-top: 20px; }
.case-outcome span { display: block; color: var(--jb-text-secondary); font-size: 11px; margin-bottom: 6px; }
.case-outcome strong { font-size: 14px; font-weight: 600; }
.case-link { display: flex; justify-content: space-between; align-items: center; gap: 8px; color: var(--jb-blue); font-size: 12px; min-height: 44px; margin-top: 12px; }
.case-link:hover, .text-link:hover, .adoption a:hover { text-decoration: underline; text-underline-offset: 4px; }
.note { font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); margin: 18px 0 0; }
.demo-followup { display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 8px 20px; margin-top: 24px; font-size: 13px; }
.demo-followup p { margin: 0; color: var(--jb-text-secondary); }
.demo-followup a { color: var(--jb-blue); font-weight: 600; padding: 10px 0; }
.journeys { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px; margin-top: 32px; }
.journey { border: 1px solid var(--jb-border); border-radius: 18px; padding: 32px; }
.viewer { border-color: var(--jb-blue-border); background: var(--jb-blue-light); }
.journey-top { display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; }
.tag { display: inline-block; padding: 4px 9px; border-radius: 5px; font-size: 11px; font-weight: 600; color: var(--jb-neutral-fg); background: var(--jb-gray-bg); }
.tag.blue { color: var(--jb-blue); background: var(--jb-blue-light); }
.viewer .tag { background: var(--jb-bg); }
.availability { font-size: 11px; color: var(--jb-text-secondary); }
.journey ol { list-style: none; counter-reset: steps; padding: 0; margin: 28px 0; }
.journey li { position: relative; padding: 0 0 24px 40px; counter-increment: steps; }
.journey li:last-child { padding-bottom: 0; }
.journey li::before { content: counter(steps); position: absolute; left: 0; top: 1px; display: grid; place-items: center; width: 24px; height: 24px; border: 1px solid var(--jb-border); background: var(--jb-bg); border-radius: 50%; font-size: 11px; color: var(--jb-blue); }
.journey strong { font-size: 14px; }
.journey li p { font-size: 13px; color: var(--jb-text-secondary); line-height: 1.85; margin: 6px 0 0; }
.journey-bottom { border-top: 1px solid var(--jb-border); padding-top: 20px; }
.journey-bottom p { font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); margin: 0 0 12px; }
.journey-bottom a { color: var(--jb-blue); font-size: 13px; font-weight: 600; display: inline-block; padding: 10px 0; }
.other-channels { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 8px 24px; margin-top: 24px; font-size: 12px; }
.other-channels > span { color: var(--jb-text-secondary); }
.other-channels a { padding: 12px 0; color: var(--jb-blue); }
.proof-section { background: var(--jb-bg-alt); }
.proof-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 36px; }
.proof-grid article { border-top: 1px solid var(--jb-blue-border); padding-top: 24px; }
.proof-number { font-size: 12px; color: var(--jb-blue); display: block; margin-bottom: 24px; }
.proof-grid h3 { font-size: 18px; }
.proof-grid p { font-size: 14px; line-height: 1.9; color: var(--jb-text-secondary); margin: 0; }
.text-link { display: inline-block; color: var(--jb-blue); font-size: 13px; font-weight: 600; margin-top: 28px; padding: 10px 0; }
.faq-layout { display: grid; grid-template-columns: 1fr 1.65fr; gap: 64px; }
.faq details { border-bottom: 1px solid var(--jb-border); }
.faq details:first-child { border-top: 1px solid var(--jb-border); }
.faq summary { font-size: 15px; font-weight: 600; padding: 22px 0; cursor: pointer; }
.faq p { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.9; margin: 0 0 24px; }
.closing { padding: 72px 24px; background: var(--jb-blue-light); }
.closing-grid { display: grid; grid-template-columns: 1.3fr 1fr; gap: 80px; align-items: center; }
.closing p { font-size: 15px; color: var(--jb-text-secondary); line-height: 1.9; margin: 0 0 24px; }
.adoption { padding: 30px; border: 1px solid var(--jb-blue-border); border-radius: 16px; background: var(--jb-bg); }
.adoption h3 { margin: 18px 0 12px; }
.adoption p { font-size: 13px; margin-bottom: 16px; }
.adoption a { display: flex; justify-content: space-between; gap: 12px; color: var(--jb-blue); font-size: 13px; padding: 12px 0; border-top: 1px solid var(--jb-border); }
@media (max-width: 1000px) {
  .hero-inner { gap: 28px; grid-template-columns: 1.2fr 1fr; }
  .desktop-break { display: none; }
  .case-card { padding: 22px; }
  .case-card h3 { font-size: 19px; }
  .faq-layout, .closing-grid { gap: 36px; }
}
@media (max-width: 768px) {
  .hero { padding: 44px 20px 0; }
  .hero-inner { grid-template-columns: 1fr; gap: 28px; }
  h1 { font-size: clamp(28px, 6.4vw, 38px); text-wrap: initial; }
  .hero-desc { font-size: 15px; margin-bottom: 24px; }
  .eyebrow { font-size: 11px; margin-bottom: 16px; }
  .actions { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
  .btn { padding: 13px 10px; gap: 8px; font-size: 12px; }
  .hint { margin-top: 14px; font-size: 11px; }
  .example { padding: 20px; border-radius: 16px; }
  .example-heading { margin: 18px 0; }
  .example h2 { font-size: 21px; }
  .example-note { font-size: 10px; }
  .hero-bottom { margin-top: 28px; gap: 10px; padding: 18px 0; font-size: 10px; flex-wrap: wrap; }
  .section { padding: 56px 20px; }
  h2 { font-size: 28px; }
  .section-heading { flex-direction: column; align-items: flex-start; gap: 18px; margin-bottom: 28px; }
  .heading-description, .intro { font-size: 14px; }
  .case-grid, .journeys, .proof-grid, .faq-layout, .closing-grid { grid-template-columns: 1fr; }
  .case-grid { gap: 14px; }
  .case-card { padding: 24px; }
  .case-top { margin-bottom: 18px; }
  .case-card h3 { font-size: 22px; }
  .case-question { margin-bottom: 20px; }
  .journeys { gap: 16px; }
  .journey { padding: 24px; }
  .other-channels { column-gap: 18px; }
  .other-channels > span { width: 100%; text-align: center; }
  .proof-grid { gap: 28px; }
  .proof-number { margin-bottom: 14px; }
  .faq-layout { gap: 28px; }
  .faq summary { font-size: 14px; }
  .closing { padding: 52px 20px; }
  .closing .btn { padding: 14px 20px; font-size: 14px; }
  .adoption { padding: 24px; }
}
</style>
