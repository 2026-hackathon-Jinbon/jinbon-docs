<script setup lang="ts">
const questions = [
  { number: '01', title: '누가 등록했나요?', text: '본인확인을 마친 등록자의 식별 정보와 등록 시각을 확인합니다.' },
  { number: '02', title: '등록 영상과 같나요?', text: '파일이 정확히 같은지 확인하고, 파일이 다르면 영상과 음성 지문을 비교합니다.' },
  { number: '03', title: '확인 근거가 있나요?', text: '블록체인 등록 기록과 그 기록에 연결된 보증서의 유효성을 확인합니다.' },
]
const proofs = [
  { label: '영상 비교', title: '등록 영상과의 관계', text: '먼저 파일 전체의 디지털 지문을 비교합니다. 파일이 다르면 유사한 등록 영상을 찾아 대표 장면과 음성 지문이 대응하는지 확인합니다.', tech: '파일 해시 · 영상·음성 지문' },
  { label: '블록체인 기록', title: '대조할 수 있는 등록 기록', text: '블록체인에 남긴 영상의 대표 지문과 등록자 식별자 등을 대조하고, 등록이 유효한 상태인지 확인합니다.', tech: 'OmniOne Chain' },
  { label: '등록 보증서', title: '영상과 등록 정보의 연결', text: '등록 보증서(VC)의 상태와 발급자·등록자 정보를 확인하고, 보증서가 해당 영상의 등록 기록에 연결되는지 대조합니다.', tech: 'Open DID' },
]
const cases = [
  { title: '보도·발표 영상을 전달할 때', text: '공개할 영상을 미리 등록해 두면, 전달받은 사람이 등록 기록과 영상 비교 결과를 확인할 수 있습니다.', note: '기관 소속과 공식 발표 권한은 별도 확인이 필요합니다.' },
  { title: '여러 플랫폼에 영상을 공유할 때', text: '게시 전에 등록 기록을 남겨두고, 유통된 영상이 등록 영상과 어떻게 대응하는지 확인할 수 있습니다.', note: '재인코딩된 영상은 후보 검색과 비교 기준을 충족해야 합니다.' },
  { title: '업무 현장의 기록을 주고받을 때', text: '같은 파일을 전달했는지 확인할 비교 기준을 남기고, 등록자와 등록 시각을 함께 확인할 수 있습니다.', note: '등록한 원본 파일은 직접 보관하세요.' },
]
const faqs = [
  { question: '등록 영상이면 내용도 사실인가요?', answer: '진본이 확인하는 것은 등록 기록과 영상의 비교 결과입니다. 영상 속 사건의 사실성, 촬영 원본 여부, AI 생성 여부, 제작자·저작권자 여부까지 보증하지는 않습니다.' },
  { question: '등록한 사람은 공식 기관의 담당자인가요?', answer: '모바일 신분증을 통한 본인확인과 기관의 공식 권한 확인은 별개입니다. 등록자 표시명만으로 소속이나 직함이 인증되는 것은 아닙니다.' },
  { question: '영상 파일은 어떻게 처리하나요?', answer: '영상은 분석을 위해 서버로 전송됩니다. 원본을 장기 보관하지 않으며, 분석용 임시 파일은 처리 후 삭제합니다. 등록한 영상의 지문과 등록 정보 등은 검증에 사용됩니다.' },
  { question: '등록 시각은 촬영 시각인가요?', answer: '진본에 등록된 시각입니다. 촬영하거나 제작한 시각을 의미하지 않습니다.' },
  { question: '등록 기록이 없으면 가짜인가요?', answer: '현재 진본에서 비교할 등록 기록을 찾지 못했다는 뜻입니다. 그 결과만으로 조작 여부를 판단할 수 없습니다.' },
]
</script>

<template>
  <div class="home-page">
    <section class="hero">
      <div class="hero-inner">
        <div class="hero-copy">
          <span class="eyebrow">영상 등록·검증 서비스, 진본</span>
          <h1><span>영상을 믿고 공유하기 전,</span><span class="accent">등록 기록부터 확인하세요.</span></h1>
          <p class="hero-desc">누가 언제 등록한 영상인지,<br class="desktop-break" /> 지금 보는 영상이 등록 영상과 어떻게 일치하는지 확인하세요.</p>
          <p class="hero-detail">진본은 영상 비교 결과와 블록체인 등록 기록,<br class="desktop-break" /> 등록 보증서를 함께 확인합니다.</p>
          <div class="actions">
            <a href="https://jinbon-web.vercel.app" class="btn primary">영상 확인하기 <span aria-hidden="true">↗</span></a>
            <a href="#how-it-works" class="btn secondary">검증 원리 알아보기</a>
          </div>
          <p class="hint">사전에 진본에 등록된 영상을 기준으로 비교합니다.<br />웹 검증은 로그인 없이 이용할 수 있습니다.</p>
        </div>
        <aside class="example" aria-label="파일 정확 일치 검증 결과 예시">
          <div class="example-top"><span>검증 결과 예시</span><span class="example-mark" aria-hidden="true">JINBON</span></div>
          <div class="check-icon" aria-hidden="true">✓</div>
          <span class="success-label">진본 확인 완료</span>
          <h2>등록 파일과<br />정확히 일치합니다.</h2>
          <p>파일 전체의 디지털 지문이 같고,<br />등록 기록과 보증서가 유효합니다.</p>
          <dl>
            <div><dt>확인 방식</dt><dd>파일 정확 일치</dd></div>
            <div><dt>블록체인 등록 기록</dt><dd>확인됨 <span aria-hidden="true">✓</span></dd></div>
            <div><dt>등록 보증서</dt><dd>유효함 <span aria-hidden="true">✓</span></dd></div>
          </dl>
          <p class="example-note">이해를 돕기 위한 예시입니다. 실제 검증 결과가 아닙니다.</p>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="inner">
        <span class="eyebrow">왜 진본인가요</span>
        <h2>공유된 영상,<br />무엇을 기준으로 확인하시나요?</h2>
        <p class="intro">다른 계정이 다시 올린 영상, 짧게 잘린 발표 영상.<br />진본은 등록할 때 남긴 기록을 바탕으로, 나중에 접한 영상과의 관계를 확인할 수 있게 합니다.</p>
        <div class="grid three">
          <article v-for="item in questions" :key="item.number" class="question-card">
            <span class="number">{{ item.number }}</span><h3>{{ item.title }}</h3><p>{{ item.text }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section alternate" id="using-jinbon">
      <div class="inner">
        <span class="eyebrow">등록부터 확인까지</span>
        <h2>등록할 때 남긴 근거를,<br />확인할 때 꺼내봅니다.</h2>
        <div class="grid two journeys">
          <article class="card journey">
            <div class="card-heading"><h3>영상을 등록하는 사람</h3><span class="tag">iOS 앱 · 배포 준비 중</span></div>
            <ol>
              <li><strong>본인확인</strong><p>모바일 신분증으로 본인확인을 마치고 디지털 지갑을 연결합니다.</p></li>
              <li><strong>영상 등록</strong><p>영상을 선택하면 디지털 지문을 계산해 블록체인에 등록합니다.</p></li>
              <li><strong>보증서 수령</strong><p>지갑에서 발급 절차를 완료하고 등록 보증서를 보관합니다.</p></li>
            </ol>
            <p class="footnote">등록과 보증서 발급은 별도 단계입니다. 원본 파일은 직접 보관하세요.</p>
          </article>
          <article class="card journey">
            <div class="card-heading"><h3>영상을 확인하는 사람</h3><span class="tag blue">웹 · 로그인 없이</span></div>
            <ol>
              <li><strong>파일 또는 링크 선택</strong><p>영상 파일을 올리거나 지원하는 영상 링크를 입력합니다.</p></li>
              <li><strong>영상과 기록 대조</strong><p>등록 영상을 찾아 비교하고 등록 기록과 보증서를 확인합니다.</p></li>
              <li><strong>근거와 함께 결과 확인</strong><p>비교 방식, 등록자 표시명, 등록 시각과 상세 사유를 살펴봅니다.</p></li>
            </ol>
            <p class="footnote">YouTube·Instagram에서는 Chrome 확장으로 검증을 시작할 수도 있습니다.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section" id="how-it-works">
      <div class="inner">
        <span class="eyebrow">검증 원리</span>
        <h2>세 가지 근거를 함께 확인합니다.</h2>
        <p class="intro">영상이 얼마나 일치하는지와 등록 증거가 유효한지를 함께 살펴봅니다.</p>
        <div class="grid three">
          <article v-for="item in proofs" :key="item.label" class="card proof">
            <span class="tag blue">{{ item.label }}</span><h3>{{ item.title }}</h3><p>{{ item.text }}</p><span class="tech">{{ item.tech }}</span>
          </article>
        </div>
        <p class="note">영상 비교와 등록 증거 확인을 <strong>모두 통과해야</strong> 검증 완료로 표시합니다. <a href="/verification-status">상세 기준 보기 →</a></p>
      </div>
    </section>

    <section class="section alternate" id="verification-results">
      <div class="inner">
        <span class="eyebrow">결과 읽기</span>
        <h2>배지와 확인 방식을 함께 보세요.</h2>
        <p class="intro">같은 ‘진본 확인 완료’라도 확인한 근거는 다릅니다.</p>
        <div class="grid two">
          <article class="card result exact">
            <span class="success-label">진본 확인 완료</span><h3>등록 파일과 정확 일치</h3>
            <p>파일 전체의 디지털 지문이 같습니다. 등록 기록과 보증서도 유효합니다.</p>
            <div class="result-basis"><span>확인한 범위</span><strong>파일 전체의 동일성</strong></div>
          </article>
          <article class="card result similar">
            <span class="success-label">진본 확인 완료</span><h3>영상·음성 비교 기준 통과</h3>
            <p>대표 장면과 음성 지문이 기준을 충족합니다. 등록 기록과 보증서도 유효합니다.</p>
            <div class="result-basis"><span>확인한 범위</span><strong>비교한 샘플의 대응 관계</strong></div>
            <p class="footnote">파일 전체가 같다는 뜻은 아닙니다. 일부 구간만 대응한다면 생략된 앞뒤 맥락도 살펴보세요.</p>
          </article>
        </div>
        <div class="status-list">
          <div><strong>유사한 등록 영상 발견</strong><p>후보는 찾았지만 비교 기준을 충족하지 못했거나 정보가 부족해 확인을 보류합니다.</p></div>
          <div><strong>등록 기록을 찾지 못함</strong><p>현재 비교할 기록을 찾지 못했습니다. 가짜라는 뜻은 아닙니다.</p></div>
          <div><strong>등록·보증서 상태 확인 필요</strong><p>등록이 비활성화되었거나 보증서가 없거나 유효하지 않습니다. 상세 사유를 확인하세요.</p></div>
          <div><strong>현재 확인할 수 없음</strong><p>외부 연결 또는 등록 기록의 검증 문제입니다. 안내에 따라 재시도하거나 운영자 확인이 필요합니다.</p></div>
        </div>
        <p class="note">등록 영상은 비교 기준으로 등록된 파일을 뜻합니다. 영상 속 사건의 사실성이나 AI 생성 여부까지 보증하지는 않습니다. <a href="/verification-status">결과의 의미와 한계 보기 →</a></p>
      </div>
    </section>

    <section class="section">
      <div class="inner">
        <span class="eyebrow">활용 예</span>
        <h2>영상과 함께, 확인할 근거를 전하세요.</h2>
        <p class="intro">사전에 등록한 영상이 있다면 다음과 같이 활용할 수 있습니다.</p>
        <div class="grid three">
          <article v-for="item in cases" :key="item.title" class="card"><h3>{{ item.title }}</h3><p>{{ item.text }}</p><p class="footnote">{{ item.note }}</p></article>
        </div>
        <p class="text-link"><a href="/use-cases">사용 사례 자세히 보기 →</a></p>
      </div>
    </section>

    <section class="section alternate">
      <div class="inner">
        <span class="eyebrow">진본의 구성</span>
        <h2>목적에 맞게 시작하세요.</h2>
        <p class="intro">앱에서 등록하고, 웹과 영상 페이지에서 확인합니다.<br />각 이용 경로는 진본의 공통 검증 서비스를 사용합니다.</p>
        <div class="grid two channels">
          <article class="card"><span class="tag blue">파일 · 영상 링크</span><h3>설치 없이, 웹에서 확인</h3><p>파일을 올리거나 지원하는 영상 URL을 입력하세요. 로그인 없이 비교 결과를 확인할 수 있습니다.</p><a href="https://jinbon-web.vercel.app">웹에서 영상 확인하기 ↗</a></article>
          <article class="card"><span class="tag">Chrome 확장 · 수동 설치</span><h3>보고 있는 영상 페이지에서</h3><p>YouTube·Instagram 영상 페이지에서 버튼을 눌러 검증을 시작하세요.</p><a href="/downloads">확장 프로그램 설치 방법 →</a></article>
          <article class="card"><span class="tag">iOS 앱 · 배포 준비 중</span><h3>영상 등록과 보증서 관리</h3><p>본인확인부터 영상 등록, 디지털 지갑의 보증서 보관까지 이어집니다. 공개 후 설치 방법을 안내합니다.</p><a href="/downloads">앱 이용 안내 보기 →</a></article>
          <article class="card"><span class="tag">카카오톡 채널</span><h3>대화창에서 영상 링크로</h3><p>영상 URL을 보내 검증을 요청하는 채널입니다. 채널에서 이용 안내를 확인하세요.</p><a href="https://pf.kakao.com/_xgtNBX">카카오톡 채널 열기 ↗</a></article>
        </div>
        <div class="developer-link"><div><strong>서비스에 진본을 연결하고 싶다면</strong><p>시스템 구성과 등록·검증 API를 개발자 센터에서 확인하세요.</p></div><a href="/developers/guide/introduction">개발자 센터 →</a></div>
      </div>
    </section>

    <section class="section">
      <div class="inner faq">
        <span class="eyebrow">자주 묻는 질문</span>
        <h2>결과를 더 정확하게 이해하려면</h2>
        <details v-for="item in faqs" :key="item.question"><summary>{{ item.question }}</summary><p>{{ item.answer }}</p></details>
      </div>
    </section>

    <section class="closing">
      <div class="inner"><span class="eyebrow">확인의 시작, 진본</span><h2>확인할 영상이 있나요?</h2><p>파일이나 링크로 등록 기록과 비교 결과를 살펴보세요.</p><a href="https://jinbon-web.vercel.app" class="btn primary">영상 확인하기 <span aria-hidden="true">↗</span></a></div>
    </section>
  </div>
</template>

<style scoped>
.home-page { color: var(--jb-ink); }
.hero { padding: 88px 24px; background: linear-gradient(150deg, var(--jb-blue-light), var(--jb-bg) 75%); border-bottom: 1px solid var(--jb-border); }
.hero-inner { max-width: 1120px; margin: auto; display: grid; grid-template-columns: 1.45fr 1fr; gap: 64px; align-items: center; }
.eyebrow { display: block; color: var(--jb-blue); font-size: 13px; font-weight: 700; margin-bottom: 18px; }
h1 { font-size: clamp(30px, 3.3vw, 44px); line-height: 1.35; letter-spacing: -.04em; font-weight: 750; margin: 0 0 24px; }
h1 span { display: block; }
.accent { color: var(--jb-blue); }
.hero-desc { font-size: 19px; line-height: 1.8; margin: 0 0 12px; }
.hero-detail, .hint { color: var(--jb-text-secondary); line-height: 1.8; }
.hero-detail { font-size: 15px; margin: 0 0 28px; }
.hint { font-size: 13px; margin: 18px 0 0; }
.actions { display: flex; flex-wrap: wrap; gap: 10px; }
.btn { display: inline-flex; align-items: center; justify-content: center; gap: 14px; padding: 13px 22px; border-radius: 10px; font-size: 15px; font-weight: 650; border: 1px solid transparent; transition: background-color .15s; }
.primary { background: var(--jb-blue-solid); color: white; }
.primary:hover { background: var(--jb-blue-solid-hover); }
.secondary { background: var(--jb-bg); border-color: var(--jb-border); }
.secondary:hover { border-color: var(--jb-blue); }
.example { background: var(--jb-bg); border: 1px solid var(--jb-blue-border); border-radius: 22px; padding: 28px; box-shadow: 0 18px 60px rgba(36,87,230,.08); }
.example-top { display: flex; justify-content: space-between; font-size: 12px; color: var(--jb-text-secondary); }
.example-mark { letter-spacing: .12em; font-weight: 750; color: var(--jb-blue); }
.check-icon { display: grid; place-items: center; width: 48px; height: 48px; border-radius: 50%; background: var(--jb-green-bg); color: var(--jb-green); font-size: 25px; margin: 28px 0 16px; }
.success-label { display: inline-block; font-size: 12px; font-weight: 650; color: var(--jb-green); background: var(--jb-green-bg); padding: 4px 9px; border-radius: 6px; }
.example h2 { font-size: 26px; line-height: 1.4; margin: 16px 0 12px; }
.example p { font-size: 14px; color: var(--jb-text-secondary); line-height: 1.7; }
.example dl { margin: 24px 0 0; padding-top: 12px; border-top: 1px solid var(--jb-border); }
.example dl div { display: flex; justify-content: space-between; gap: 14px; padding: 8px 0; font-size: 13px; }
.example dt { color: var(--jb-text-secondary); }
.example dd { margin: 0; font-weight: 600; }
.example dd span { color: var(--jb-green); }
.example .example-note { font-size: 11px; margin: 18px 0 0; }
.section { padding: 80px 24px; scroll-margin-top: 80px; }
.alternate { background: var(--jb-bg-alt); }
.inner { max-width: 1040px; margin: auto; }
h2 { font-size: 30px; line-height: 1.45; letter-spacing: -.025em; font-weight: 700; margin: 0 0 20px; }
h3 { font-size: 19px; line-height: 1.5; font-weight: 650; margin: 0 0 12px; letter-spacing: -.02em; }
.intro { max-width: 780px; color: var(--jb-text-secondary); font-size: 16px; line-height: 1.85; margin: 0 0 32px; }
.grid { display: grid; gap: 20px; }
.three { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.card { padding: 28px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); }
.card p, .question-card p { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.8; margin: 0; }
.question-card { border-top: 2px solid var(--jb-blue-border); padding: 26px 8px 0 0; }
.number { display: block; color: var(--jb-blue); font-size: 14px; font-variant-numeric: tabular-nums; margin-bottom: 22px; }
.card-heading { display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: center; }
.card-heading h3 { margin: 0; }
.tag { display: inline-block; padding: 4px 9px; border-radius: 6px; font-size: 11px; font-weight: 600; background: var(--jb-gray-bg); color: var(--jb-neutral-fg); }
.tag.blue { background: var(--jb-blue-light); color: var(--jb-blue); }
.journeys { margin-top: 32px; }
.journey ol { list-style: none; counter-reset: steps; padding: 0; margin: 28px 0; }
.journey li { position: relative; padding: 0 0 25px 42px; counter-increment: steps; }
.journey li:last-child { padding-bottom: 0; }
.journey li::before { content: counter(steps); position: absolute; left: 0; top: 0; display: grid; place-items: center; width: 28px; height: 28px; border-radius: 50%; font-size: 12px; font-weight: 700; color: var(--jb-blue); background: var(--jb-blue-light); }
.journey strong { display: block; margin-bottom: 5px; font-size: 16px; }
.card .footnote { font-size: 13px; margin-top: 20px; padding-top: 16px; border-top: 1px solid var(--jb-border); }
.proof { display: flex; flex-direction: column; align-items: flex-start; }
.proof h3, .channels h3 { margin-top: 18px; }
.tech { display: block; margin-top: auto; padding-top: 24px; font-size: 12px; color: var(--jb-blue); }
.note { margin: 24px 0 0; color: var(--jb-text-secondary); font-size: 14px; line-height: 1.9; }
.note strong { color: var(--jb-ink); }
.note a, .text-link a, .channels a, .developer-link a { color: var(--jb-blue); text-decoration: underline; text-underline-offset: 4px; font-weight: 600; }
.result h3 { margin-top: 18px; font-size: 23px; }
.exact { border-top: 3px solid var(--jb-green); }
.similar { border-top: 3px solid var(--jb-blue); }
.result-basis { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 8px; background: var(--jb-bg-alt); border-radius: 8px; padding: 14px; margin-top: 24px; font-size: 13px; }
.result-basis span { color: var(--jb-text-secondary); }
.status-list { margin-top: 28px; border-top: 1px solid var(--jb-border); }
.status-list > div { display: grid; grid-template-columns: 230px 1fr; gap: 20px; padding: 18px 0; border-bottom: 1px solid var(--jb-border); }
.status-list strong { font-size: 14px; }
.status-list p { font-size: 14px; line-height: 1.8; margin: 0; color: var(--jb-text-secondary); }
.text-link { margin: 24px 0 0; font-size: 14px; }
.channels a { display: inline-block; margin-top: 22px; font-size: 14px; }
.developer-link { margin-top: 24px; border-radius: 14px; padding: 24px 28px; background: var(--jb-blue-light); display: flex; justify-content: space-between; align-items: center; gap: 20px; }
.developer-link p { color: var(--jb-text-secondary); font-size: 14px; margin: 6px 0 0; }
.developer-link a { flex-shrink: 0; font-size: 14px; }
.faq { max-width: 800px; }
.faq details { border-bottom: 1px solid var(--jb-border); }
.faq summary { cursor: pointer; font-size: 16px; font-weight: 600; padding: 24px 4px; }
.faq details p { margin: 0 0 24px; color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; }
.closing { padding: 72px 24px 88px; text-align: center; background: var(--jb-blue-light); }
.closing p { color: var(--jb-text-secondary); line-height: 1.8; margin: 0 0 28px; }
@media (max-width: 1000px) {
  .hero-inner { gap: 32px; }
  .hero { padding: 64px 24px; }
  .desktop-break { display: none; }
  .card { padding: 24px; }
  .three { gap: 14px; }
}
@media (max-width: 768px) {
  .hero-inner, .three, .two { grid-template-columns: 1fr; }
  .hero { padding: 48px 20px; }
  .hero-inner { gap: 36px; }
  h1 { font-size: 32px; }
  .hero-desc { font-size: 17px; }
  .example { max-width: 480px; width: 100%; }
  .section { padding: 52px 20px; }
  h2 { font-size: 26px; }
  .grid { gap: 16px; }
  .question-card { padding: 22px 0; }
  .number { margin-bottom: 12px; }
  .status-list > div { grid-template-columns: 1fr; gap: 6px; }
  .developer-link { flex-direction: column; align-items: flex-start; }
  .closing { padding: 52px 20px; }
}
</style>
