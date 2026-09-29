<script setup lang="ts">
import { computed, ref } from 'vue'

const states = [
  {
    id: 'complete', label: '진본 확인', short: '진본 확인', icon: '✓',
    title: '영상과 등록 근거를\n함께 확인했어요.',
    description: '파일이 정확히 같거나 영상·음성 비교 기준을 통과했고, 등록 기록과 디지털 보증서(VC)도 유효한 상태입니다.',
    checks: [
      { label: '영상 비교', value: '정확 일치 또는 비교 기준 통과', text: '어떤 방식으로 확인됐는지 결과에 표시된 확인 방식을 살펴보세요.' },
      { label: '등록 기록', value: '등록 상태와 블록체인 기록 확인', text: '활성 상태인 등록 기록을 대조했어요.' },
      { label: '디지털 보증서(VC)', value: '유효 · 해당 영상의 등록 정보 일치', text: '보증서가 유효하고 해당 등록 기록에 연결되는지 확인했어요.' },
    ],
    nextTitle: '확인된 범위까지 함께 살펴보세요.',
    next: '등록자와 등록 시각, 확인 방식을 읽어보세요. 일부 구간이 대응한다면 전체 영상의 맥락도 함께 확인해 주세요.',
    link: '#methods', linkText: '두 가지 확인 방식 알아보기',
  },
  {
    id: 'mismatch', label: '원본 불일치', short: '원본 불일치', icon: '!',
    title: '영상 또는 음성에서\n불일치가 확인됐어요.',
    description: '영상·음성 비교 정보가 모두 있고, 비교 기준을 통과하지 못한 영상에서 화면 또는 음성의 불일치 구간이 확인된 결과입니다.',
    checks: [
      { label: '영상 비교', value: '영상·음성 중 불일치 구간 확인', text: '상세 메시지에서 화면과 음성 중 어느 쪽이 일치하지 않았는지 확인해 주세요.' },
      { label: '등록 기록', value: '비교 대상으로 찾은 등록 영상의 정보', text: '표시된 등록자와 등록 시각은 비교 원본의 정보이며, 제출 영상이 진본이라는 뜻은 아니에요.' },
      { label: '디지털 보증서(VC)', value: '등록 근거와 영상 비교는 별개', text: '비교 원본의 보증서가 유효해도 제출 영상의 비교 기준 통과를 뜻하지는 않아요.' },
    ],
    nextTitle: '어떤 부분이 다른지 살펴보세요.',
    next: '상세 메시지와 불일치 구간을 확인하고, 원 게시자나 공식 채널에서도 영상을 살펴보세요. 이 결과만으로 조작이나 AI 생성 여부를 확정할 수는 없어요.',
    link: '#examples', linkText: '상황별 결과 해석 보기',
  },
  {
    id: 'missing', label: '등록 기록 없음', short: '등록 기록 없음', icon: '−',
    title: '비교할 등록 영상을\n찾지 못했어요.',
    description: '현재 비교에서 등록 영상이나 후보를 찾지 못한 결과입니다. 실제 미등록 외에 파일 변환이나 편집 등으로 후보 검색에 실패한 경우에도 표시될 수 있어요.',
    checks: [
      { label: '영상 비교', value: '일치 여부를 확인할 비교 대상 없음', text: '이 결과만으로 가짜나 조작 영상이라고 판단할 수 없어요.' },
      { label: '등록 기록', value: '현재 비교에서 등록 후보를 찾지 못함', text: '등록자와 등록 시각도 확인할 수 없어요. 등록 여부와 제출한 영상을 함께 살펴보세요.' },
      { label: '디지털 보증서(VC)', value: '대조할 등록 보증서를 확인하지 못함', text: '등록 후보를 찾지 못한 결과이며, 보증서가 무효라고 판정한 것은 아니에요.' },
    ],
    nextTitle: '등록 여부와 제출한 영상을 확인해 주세요.',
    next: '원 게시자나 공식 채널에서 영상의 출처와 등록 여부를 살펴보세요. 등록된 영상이라면 등록에 사용한 파일로 다시 확인할 수 있어요.',
    link: '/downloads', linkText: '영상 등록·이용 안내 보기',
  },
  {
    id: 'unavailable', label: '확인 불가', short: '확인 불가', icon: '…',
    title: '현재 결과로는\n진본 여부를 확인할 수 없어요.',
    description: '비교 정보 부족, 비교 기준 미충족, 등록 비활성화, 보증서 문제 또는 외부 서비스 오류 등으로 진본을 확인할 수 없는 결과입니다.',
    checks: [
      { label: '영상 비교', value: '비교 정보와 상세 사유 확인', text: '비교 정보가 부족하거나, 불일치 구간이 표시되지 않아도 영상·음성의 대응 시점이나 순서가 맞지 않을 수 있어요.' },
      { label: '등록 기록', value: '활성 상태·블록체인 확인 결과 살펴보기', text: '등록 비활성화, 일시적인 연결 오류, 블록체인 기록 불일치를 구분해 주세요.' },
      { label: '디지털 보증서(VC)', value: '발급·유효성·등록 정보 연결 확인', text: '미발급·무효와 보증서 확인 서비스 연결 실패를 상세 사유로 구분해 주세요.' },
    ],
    nextTitle: '표시된 사유에 따라 다음 행동이 달라요.',
    next: '비교 정보가 부족하면 원본 파일로 다시 확인하고, 등록·보증서 문제는 등록자에게 확인해 주세요. 연결 오류는 잠시 후 재시도하고, 블록체인 기록 불일치는 운영자에게 확인해 주세요.',
    link: 'https://jinbon-web.vercel.app', linkText: '검증 화면으로 이동',
  },
]
const selected = ref('complete')
const state = computed(() => states.find(item => item.id === selected.value)!)
const reasons = [
  { title: '영상·음성 비교 정보 부족', text: '음성 트랙이 없거나 필요한 비교 정보를 만들지 못한 경우예요. 이때는 불일치를 확인했다고 표시하지 않습니다. 원본 파일로 다시 확인해 주세요.' },
  { title: '대응 시점·순서 등 비교 기준 미충족', text: '불일치 구간이 표시되지 않아도 영상과 음성의 원본 대응 시점이나 순서가 맞지 않으면 진본으로 확인할 수 없어요. 상세 메시지를 확인해 주세요.' },
  { title: '등록 비활성화', text: '찾은 등록의 사용이 중지된 상태예요. 기록 자체가 남아 있어도 진본으로 확인하지 않습니다. 등록자에게 활성 상태를 확인해 주세요.' },
  { title: '보증서 미발급·무효', text: '보증서가 연결되지 않았거나 유효하지 않거나 해당 영상의 등록 정보와 맞지 않는 경우예요. 등록자에게 발급·연결 상태를 확인해 주세요.' },
  { title: '외부 검증 서비스 연결 오류', text: '블록체인이나 보증서 확인 서비스에 연결하지 못한 경우예요. 잠시 후 다시 시도해 주세요. 자동 재검증이 예약된 상태는 아닙니다.' },
  { title: '블록체인 기록 불일치', text: '등록 기록은 찾았지만 블록체인 무결성 검증을 통과하지 못한 경우예요. 운영자 확인이 필요합니다.' },
]
const examples = [
  { title: 'SNS에 올라가면서 해상도나 파일이 바뀌었어요.', text: '파일 지문이 달라지면 유사한 등록 후보를 찾고 장면·음성을 비교합니다. 비교 기준과 등록 기록·VC 검증을 모두 통과해야 진본 확인으로 표시됩니다.' },
  { title: '긴 영상에서 일부를 잘라 쇼츠로 만들었어요.', text: '후보 검색에 성공하고, 잘라낸 구간의 영상·음성이 등록 영상의 같은 시간대에 대응하며 비교 기준과 등록 근거 검증을 통과하면 확인될 수 있어요. 모든 짧은 영상을 찾는 것은 아니며, 생략된 앞뒤 맥락은 따로 살펴봐야 합니다.' },
  { title: '등록 파일을 그대로 확인했어요.', text: '파일 전체의 디지털 지문(SHA-256)이 같고 등록 기록과 보증서가 유효하면 파일 정확 일치로 확인돼요. 이 방식은 오디오가 없는 파일도 확인할 수 있습니다.' },
  { title: '음성을 바꾸거나 오디오를 제거했어요.', text: '파일이 다른 경우, 음성 비교 기준에 미달하거나 비교할 음성이 없으면 영상·음성 비교 경로로 승인하지 않습니다. 일부 음성 변경은 샘플 비교에서 놓칠 수 있으므로 모든 변경을 탐지한다는 뜻은 아니에요.' },
  { title: '얼굴·입모양, 자막·로고, 장면을 바꿨어요.', text: '변경 내용이 비교 샘플에 반영되어 기준에 미달하면 진본으로 인증하지 않습니다. 작은 변화나 짧은 편집은 놓칠 수 있으며, 불일치만으로 딥페이크나 편집 여부를 확정하지 않습니다.' },
  { title: '영상이 일치하는데도 진본 확인이 아니에요.', text: '등록이 비활성화됐거나 디지털 보증서(VC)가 미발급·무효이면 확인 불가로 표시됩니다. 블록체인 기록이 남아 있어도 등록 상태와 보증서를 함께 확인해야 해요.' },
  { title: 'SNS 링크의 영상을 가져오지 못했어요.', text: '로그인 요구나 접근 제한 등으로 영상을 가져오지 못하면 비교를 진행할 수 없어요. ‘등록 기록 없음’과는 다른 요청 오류입니다. 본인이 보유하고 검증에 사용할 권한이 있는 파일을 직접 올려 확인해 주세요.' },
]
</script>

<template>
  <div class="vs-page">
    <header class="vs-hero">
      <div class="inner">
        <p class="eyebrow">검증 결과 안내</p>
        <h1>진본 확인 결과,<br /><span>어디까지 확인된 걸까요?</span></h1>
        <p class="hero-description">SNS에서 본 영상의 비교 결과와 등록 기록,<br />디지털 보증서(VC) 상태를 함께 살펴보세요.</p>
        <nav class="vs-jump" aria-label="검증 안내 바로가기"><a href="#states">결과별 의미 <span aria-hidden="true">↓</span></a><a href="#methods">두 가지 확인 방식 <span aria-hidden="true">↓</span></a><a href="#criteria">등록 기록과 VC <span aria-hidden="true">↓</span></a><a href="#examples">상황별 해석 <span aria-hidden="true">↓</span></a></nav>
      </div>
    </header>

    <section id="states" class="section states-section" aria-labelledby="states-title">
      <div class="inner">
        <div class="section-heading"><p class="eyebrow">결과 읽기</p><h2 id="states-title">받은 결과를 선택해 보세요.</h2><p class="intro">웹·카카오톡의 결과 제목을 기준으로, 확인된 범위와 다음에 할 일을 안내합니다.</p></div>
        <div class="state-selector" role="group" aria-label="의미를 살펴볼 검증 상태">
          <button v-for="item in states" :key="item.id" type="button" :class="item.id" :aria-pressed="selected === item.id" aria-controls="status-detail" @click="selected = item.id"><span class="selector-icon" aria-hidden="true">{{ item.icon }}</span><span>{{ item.short }}</span></button>
        </div>
        <div id="status-detail" class="status-detail" :class="selected" role="region" aria-labelledby="state-title">
          <div class="state-summary">
            <div aria-live="polite" aria-atomic="true"><span class="status-label"><span aria-hidden="true">{{ state.icon }}</span>{{ state.label }}</span><h3 id="state-title">{{ state.title }}</h3><p class="state-description">{{ state.description }}</p></div>
            <div class="next-action"><span>다음으로 할 일</span><h4>{{ state.nextTitle }}</h4><p>{{ state.next }}</p><a :href="state.link">{{ state.linkText }} <span aria-hidden="true">→</span></a></div>
          </div>
          <div class="state-checks"><p class="panel-label">결과에서 함께 읽을 근거</p><dl><div v-for="(check, index) in state.checks" :key="check.label"><dt><span aria-hidden="true">0{{ index + 1 }}</span>{{ check.label }}</dt><dd><strong>{{ check.value }}</strong><p>{{ check.text }}</p></dd></div></dl></div>
        </div>
        <div v-if="selected === 'unavailable'" class="reason-panel">
          <h3>같은 ‘확인 불가’도 이유는 달라요.</h3>
          <div class="reason-grid"><details v-for="reason in reasons" :key="reason.title"><summary>{{ reason.title }}<span aria-hidden="true">+</span></summary><p>{{ reason.text }}</p></details></div>
        </div>
        <p class="section-note">같은 결과명이라도 상세 사유는 다를 수 있어요. 결과와 함께 표시된 영상·음성 비교 정보와 등록 근거를 확인해 주세요.</p>
      </div>
    </section>

    <section id="methods" class="section alternate" aria-labelledby="methods-title">
      <div class="inner">
        <div class="section-heading"><p class="eyebrow">두 가지 확인 방식</p><h2 id="methods-title">확인 완료라고 해도,<br />비교한 범위는 달라요.</h2><p class="intro">두 방식 모두 등록 기록과 디지털 보증서(VC)가 유효해야 합니다.</p></div>
        <div class="methods-grid">
          <article class="method">
            <div class="method-top"><span>01</span><span>파일 전체 비교</span></div><h3>등록 파일과 정확 일치</h3><p>파일 전체에서 계산한 디지털 지문이 같아요.</p>
            <div class="file-diagram" aria-hidden="true"><div><span class="file-icon">MP4</span><span>등록 파일</span></div><span class="equals">=</span><div><span class="file-icon submitted">MP4</span><span>제출 파일</span></div></div>
            <div class="method-scope"><span>확인한 범위</span><strong>파일 전체의 동일성</strong></div><p class="method-note">등록 파일을 그대로 제출한 경우예요.<br />오디오가 없는 파일도 확인할 수 있습니다.</p>
          </article>
          <article class="method">
            <div class="method-top"><span>02</span><span>대표 장면 · 음성 비교</span></div><h3>영상·음성 비교 기준 통과</h3><p>비교한 장면과 음성이 등록 영상의 같은 시간대에 대응해요.</p>
            <div class="sample-diagram" aria-hidden="true"><div><span>장면</span><div class="sample-frames"><i v-for="n in 6" :key="n" /></div></div><div><span>음성</span><div class="sample-audio"><i v-for="n in 24" :key="n" /></div></div><span class="sample-caption">대표 장면과 음성 지문을 비교</span></div>
            <div class="method-scope"><span>확인한 범위</span><strong>비교한 장면과 음성의 대응 관계</strong></div><p class="method-note">파일 전체가 같다는 뜻은 아니에요.<br />샘플 사이의 편집이나 작은 변화는 놓칠 수 있습니다.</p>
          </article>
        </div>
        <div class="segment-card">
          <div class="segment-copy"><span class="small-label">짧은 영상이라면</span><h3>어느 구간에<br />대응하는지도 살펴보세요.</h3><p>6초짜리 제출 영상이 등록 영상의 3–9초 구간에 대응하는 개념 예시예요.</p></div>
          <figure class="timeline">
            <div class="time-axis" aria-hidden="true"><span>0초</span><span>3초</span><span>9초</span><span>12초</span></div>
            <div class="track-row"><span>등록 영상</span><div class="track" aria-hidden="true"><i v-for="n in 12" :key="n" /></div></div>
            <div class="track-row"><span>제출 영상</span><div class="track" aria-hidden="true"><i v-for="n in 12" :key="n" :class="n > 3 && n <= 9 ? 'matched' : 'empty'" /></div></div>
            <div class="match-axis" aria-hidden="true"><span>3–9초 대응</span></div>
            <figcaption>일부 구간이 대응해도 생략된 앞뒤 맥락은 따로 확인해야 해요. 실제 확인은 후보 검색·영상·음성 비교와 등록 근거 검증을 모두 통과해야 합니다.</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section id="criteria" class="section" aria-labelledby="criteria-title">
      <div class="inner">
        <div class="section-heading"><p class="eyebrow">결과를 뒷받침하는 근거</p><h2 id="criteria-title">영상이 일치해도,<br />등록 근거까지 확인합니다.</h2><p class="intro">등록한 사람의 정보가 표시되는 것만으로 진본 확인이 완료되지는 않아요.</p></div>
        <div class="evidence-grid">
          <article><span class="evidence-number">01</span><h3>등록이 활성 상태인지</h3><p>영상의 등록 상태를 확인해요. 사용이 중지된 등록은 기록이 남아 있어도 확인 완료로 표시하지 않습니다.</p><span class="evidence-tag">등록 상태</span></article>
          <article><span class="evidence-number">02</span><h3>블록체인 기록이 맞는지</h3><p>블록체인에 남긴 영상의 대표 지문과 등록자 식별 정보 등을 대조해 등록 기록을 확인해요.</p><span class="evidence-tag">블록체인 등록 기록</span></article>
          <article class="certificate"><span class="evidence-number">VC</span><h3>디지털 보증서가 유효한지</h3><p>보증서의 유효성과 발급자·등록자 정보를 확인하고, 해당 영상의 등록 기록에 연결되는지 대조해요.</p><span class="evidence-tag">보증서 유효성 · 등록 정보 연결</span></article>
        </div>
        <div class="registration-note"><strong>디지털 보증서(VC)는 해당 영상의 등록 사실을 담아요.</strong><p>영상 내용의 사실성이나 AI 생성 여부, 저작권까지 보증하는 것은 아닙니다. 등록 시각은 촬영 시각과 다르며, 등록자 표시명이 기관 소속이나 공식 발표 권한을 뜻하지는 않아요.</p></div>
        <details class="criteria-detail"><summary>영상·음성 비교의 상세 기준 보기<span aria-hidden="true">+</span></summary><div class="detail-body">
          <p>파일 전체의 지문(SHA-256)이 같으면 등록 근거 확인으로 넘어갑니다. 파일이 다르면 후보 검색 후 <strong>1초 간격 대표 프레임과 음성 지문</strong>을 비교해요. 모든 프레임을 검사하는 방식은 아닙니다.</p>
          <div class="thresholds"><div><span>영상 구간 일치율</span><strong>95% 이상</strong></div><div><span>음성 구간 일치율</span><strong>100%</strong></div></div>
          <p><strong>이 수치는 판정 기준이며 정확도나 조작 탐지율이 아닙니다.</strong> 순서가 보존되고 영상·음성의 원본 대응 시점이 같아야 해요. 반복 장면 등으로 대응 시점이 다르면 진본으로 인증하지 않습니다.</p>
          <p>음성 100%는 모든 비교 구간의 지문이 허용 오차(해밍 거리 10 이하) 안에서 일치한다는 뜻이에요. 재압축된 영상도 통과할 수 있지만, 음질 저하 등으로 한 구간이라도 기준을 벗어나면 정상 영상도 진본으로 확인되지 않을 수 있습니다.</p>
          <p>음성 비교 정보가 없으면 영상·음성 비교 경로로 승인하지 않습니다. 구간별 허용 오차와 샘플링의 한계로 작은 화면 변화·짧은 편집·일부 음성 교체를 놓칠 수 있어요.</p>
          <p>일부 결과는 캐시를 사용하므로 모든 요청에서 등록 근거를 새로 조회하는 것은 아닙니다.</p>
          <div class="detail-links"><a href="/verification-details#audio-verification">음성 비교의 네 단계 보기 <span aria-hidden="true">→</span></a><a href="/developers/api/verify">검증 API 상세 보기 <span aria-hidden="true">→</span></a></div>
        </div></details>
      </div>
    </section>

    <section id="examples" class="section alternate" aria-labelledby="examples-title">
      <div class="inner faq-grid"><div><p class="eyebrow">상황별 해석</p><h2 id="examples-title">이런 영상은<br />어떻게 확인되나요?</h2><p class="faq-intro">실제 결과는 영상 비교 기준과<br />등록 근거 확인에 따라 달라집니다.</p><a href="/use-cases" class="text-link">사용 사례로 살펴보기 <span aria-hidden="true">→</span></a></div>
        <div class="examples"><details v-for="example in examples" :key="example.title"><summary>{{ example.title }}<span aria-hidden="true">+</span></summary><p>{{ example.text }}</p></details></div>
      </div>
    </section>

    <section class="closing" aria-labelledby="closing-title"><div class="inner"><p class="eyebrow">영상의 출처와 진본 여부, 진본에서</p><h2 id="closing-title">지금 보는 영상의<br />확인 근거를 살펴보세요.</h2><p>등록자와 등록 시각, 영상 비교 결과,<br class="mobile-break" /> 디지털 보증서까지 함께 확인하세요.</p><div class="closing-actions"><a class="button primary" href="https://jinbon-web.vercel.app">영상 확인하기 <span aria-hidden="true">↗</span></a><a class="button secondary" href="/#experience">결과 예시 먼저 보기 <span aria-hidden="true">→</span></a></div></div></section>
  </div>
</template>

<style scoped>
.vs-page { color: var(--jb-ink); background: var(--jb-bg); }
.inner { width: min(1120px, calc(100% - 64px)); margin-inline: auto; }
h1, h2, h3, h4, p, figure { margin: 0; }
h1, h2, h3, h4 { letter-spacing: -.04em; text-wrap: balance; }
h2 { font-size: clamp(30px, 3.4vw, 42px); font-weight: 750; line-height: 1.4; }
h3, h4 { font-weight: 650; line-height: 1.5; }
a:focus-visible, button:focus-visible, summary:focus-visible { outline: 3px solid var(--jb-blue); outline-offset: 5px; }
.eyebrow { color: var(--jb-blue); font-size: 13px; font-weight: 650; line-height: 1.6; margin-bottom: 18px; }
.vs-hero { padding-block: 74px 36px; }
h1 { font-size: clamp(36px, 4.5vw, 56px); line-height: 1.3; font-weight: 750; }
h1 > span { color: var(--jb-blue); }
.hero-description { margin-top: 24px; color: var(--jb-text-secondary); font-size: 17px; line-height: 1.9; }
.vs-jump { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 32px; }
.vs-jump a { display: flex; align-items: center; gap: 17px; min-height: 44px; padding: 10px 16px; border: 1px solid var(--jb-border); border-radius: 9px; background: var(--jb-bg-alt); font-size: 12px; }
.vs-jump a > span { color: var(--jb-blue); }
.vs-jump a:hover { background: var(--jb-blue-light); border-color: var(--jb-blue-border); }
.section { padding-block: 84px; scroll-margin-top: 72px; }
.states-section { padding-top: 44px; }
.alternate { background: var(--jb-bg-alt); }
.section-heading { margin-bottom: 34px; }
.section-heading .eyebrow { margin-bottom: 15px; }
.intro { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; margin-top: 18px; }
.state-selector { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-bottom: 16px; }
.state-selector button { display: flex; justify-content: center; align-items: center; gap: 10px; min-height: 58px; padding: 12px; border: 1px solid var(--jb-border); border-radius: 10px; color: var(--jb-text-secondary); background: var(--jb-bg); font-size: 13px; font-weight: 600; cursor: pointer; transition: border-color .2s, background-color .2s; }
.state-selector button:hover { background: var(--jb-bg-alt); }
.state-selector button[aria-pressed="true"] { border-color: var(--jb-blue); color: var(--jb-ink); background: var(--jb-blue-light); box-shadow: inset 0 0 0 1px var(--jb-blue); }
.complete { --status-ink: var(--jb-green); --status-bg: var(--jb-green-bg); }
.mismatch { --status-ink: var(--jb-yellow); --status-bg: var(--jb-yellow-bg); }
.missing { --status-ink: var(--jb-neutral-fg); --status-bg: var(--jb-gray-bg); }
.unavailable { --status-ink: var(--jb-blue); --status-bg: var(--jb-blue-light); }
.selector-icon { display: grid; place-items: center; width: 24px; height: 24px; border-radius: 50%; background: var(--status-bg); color: var(--status-ink); font-size: 13px; font-weight: 650; }
.status-detail { display: grid; grid-template-columns: 1fr 1fr; border: 1px solid var(--jb-border); border-radius: 18px; overflow: hidden; }
.state-summary { padding: 34px; display: flex; flex-direction: column; }
.status-label { display: inline-flex; align-items: center; gap: 7px; color: var(--status-ink); background: var(--status-bg); padding: 5px 10px; border-radius: 6px; font-size: 11px; font-weight: 600; }
.state-summary h3 { white-space: pre-line; font-size: 28px; margin-top: 18px; }
.state-description { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.9; margin-top: 16px; margin-bottom: 26px; }
.next-action { padding-top: 22px; border-top: 1px solid var(--jb-border); margin-top: auto; }
.next-action > span { font-size: 10px; color: var(--jb-blue); font-weight: 650; }
.next-action h4 { font-size: 15px; margin-top: 7px; }
.next-action p { font-size: 13px; line-height: 1.85; color: var(--jb-text-secondary); margin-top: 8px; }
.next-action a { display: inline-flex; align-items: center; gap: 14px; min-height: 40px; margin-top: 10px; color: var(--jb-blue); font-size: 12px; font-weight: 600; }
.next-action a:hover, .detail-links a:hover, .text-link:hover { text-decoration: underline; text-underline-offset: 5px; }
.state-checks { padding: 34px; border-left: 1px solid var(--jb-border); background: var(--jb-bg-alt); }
.panel-label { color: var(--jb-text-secondary); font-size: 11px; font-weight: 600; }
.state-checks dl { margin: 8px 0 0; }
.state-checks dl > div { padding-block: 22px; }
.state-checks dl > div + div { border-top: 1px solid var(--jb-border); }
.state-checks dl > div:last-child { padding-bottom: 0; }
.state-checks dt { display: flex; align-items: center; gap: 9px; color: var(--jb-text-secondary); font-size: 11px; }
.state-checks dt > span { color: var(--jb-blue); font-size: 10px; }
.state-checks dd { margin: 10px 0 0; }
.state-checks strong { font-size: 15px; font-weight: 650; line-height: 1.7; }
.state-checks dd p { font-size: 13px; line-height: 1.85; color: var(--jb-text-secondary); margin-top: 7px; }
.section-note { font-size: 11px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 20px; }
.reason-panel { border: 1px solid var(--jb-border); border-radius: 14px; padding: 25px 28px; margin-top: 16px; }
.reason-panel h3 { font-size: 18px; margin-bottom: 12px; }
.reason-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 30px; align-items: start; }
.reason-grid details { border-top: 1px solid var(--jb-border); }
.reason-grid summary { font-size: 13px; padding-block: 17px; }
.reason-grid details p { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.85; padding-bottom: 20px; }
.methods-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px; }
.method { display: flex; flex-direction: column; padding: 30px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); }
.method-top { display: flex; gap: 10px; color: var(--jb-text-secondary); font-size: 11px; }
.method-top > span:first-child { color: var(--jb-blue); }
.method h3 { font-size: 25px; margin-top: 14px; }
.method > p { font-size: 14px; color: var(--jb-text-secondary); line-height: 1.85; margin-top: 12px; min-height: 52px; }
.file-diagram { display: flex; align-items: center; justify-content: center; gap: 32px; min-height: 172px; margin-block: auto 12px; padding-top: 20px; }
.file-diagram > div { display: flex; flex-direction: column; align-items: center; gap: 10px; font-size: 10px; color: var(--jb-text-secondary); }
.file-icon { display: grid; place-items: center; width: 61px; height: 78px; border: 1px solid var(--jb-blue-border); border-radius: 8px; font-size: 12px; font-weight: 650; background: var(--jb-bg-alt); color: var(--jb-blue); }
.file-icon.submitted { background: var(--jb-blue-light); }
.equals { color: var(--jb-blue); font-size: 24px; padding-bottom: 28px; }
.sample-diagram { display: flex; flex-direction: column; justify-content: center; gap: 15px; min-height: 172px; padding: 22px 16px 12px; margin-block: auto 12px; }
.sample-diagram > div { display: flex; align-items: center; gap: 14px; }
.sample-diagram > div > span { font-size: 10px; color: var(--jb-text-secondary); flex-shrink: 0; }
.sample-frames { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 6px; flex: 1; }
.sample-frames i { height: 29px; border: 1px solid var(--jb-blue-border); background: var(--jb-blue-light); border-radius: 4px; }
.sample-audio { display: flex; align-items: center; justify-content: space-between; gap: 3px; flex: 1; height: 28px; }
.sample-audio i { flex: 1; height: 10px; max-width: 5px; border-radius: 3px; background: var(--jb-blue); }
.sample-audio i:nth-child(3n) { height: 24px; }
.sample-audio i:nth-child(4n) { height: 16px; }
.sample-audio i:nth-child(5n) { height: 6px; }
.sample-caption { text-align: center; font-size: 10px; color: var(--jb-text-secondary); }
.method-scope { display: flex; justify-content: space-between; flex-wrap: wrap; gap: 6px 14px; border-top: 1px solid var(--jb-border); padding-top: 18px; font-size: 12px; }
.method-scope > span { color: var(--jb-text-secondary); }
.method-scope strong { color: var(--jb-blue); font-weight: 650; }
.method > .method-note { font-size: 12px; min-height: 0; margin-top: 12px; }
.segment-card { display: grid; grid-template-columns: .8fr 1.2fr; gap: 40px; align-items: center; padding: 30px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); margin-top: 22px; }
.small-label { font-size: 11px; color: var(--jb-blue); }
.segment-copy h3 { font-size: 22px; margin-top: 10px; }
.segment-copy p { font-size: 13px; line-height: 1.85; color: var(--jb-text-secondary); margin-top: 14px; }
.time-axis { position: relative; height: 22px; margin-left: 72px; color: var(--jb-text-secondary); font-size: 10px; }
.time-axis span { position: absolute; }
.time-axis span:first-child { left: 0; }
.time-axis span:nth-child(2) { left: 25%; transform: translateX(-50%); }
.time-axis span:nth-child(3) { left: 75%; transform: translateX(-50%); }
.time-axis span:last-child { right: 0; }
.track-row { display: flex; align-items: center; gap: 12px; margin: 10px 0; }
.track-row > span { font-size: 11px; flex: 0 0 60px; color: var(--jb-text-secondary); }
.track { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 3px; flex: 1; }
.track i { height: 23px; border: 1px solid var(--jb-blue-border); border-radius: 3px; background: var(--jb-blue-light); }
.track .matched { background: var(--jb-blue-solid); border-color: var(--jb-blue-solid); }
.track .empty { background: transparent; border: 1px dashed var(--jb-border); }
.match-axis { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 3px; margin-left: 72px; }
.match-axis span { grid-column: 4 / 10; border: solid var(--jb-blue); border-width: 0 1px 1px; padding-bottom: 6px; color: var(--jb-blue); font-size: 10px; text-align: center; }
figcaption { font-size: 11px; line-height: 1.85; color: var(--jb-text-secondary); margin-top: 18px; }
.evidence-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; }
.evidence-grid article { display: flex; flex-direction: column; padding: 25px; background: var(--jb-bg-alt); border: 1px solid var(--jb-border); border-radius: 14px; }
.evidence-number { display: grid; place-items: center; width: 32px; height: 32px; border-radius: 8px; background: var(--jb-blue-light); color: var(--jb-blue); font-size: 11px; font-weight: 650; }
.evidence-grid h3 { font-size: 19px; margin-top: 19px; }
.evidence-grid p { font-size: 13px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 12px; margin-bottom: 23px; }
.evidence-tag { font-size: 10px; color: var(--jb-text-secondary); padding-top: 14px; border-top: 1px solid var(--jb-border); margin-top: auto; }
.evidence-grid .certificate { background: var(--jb-blue-light); border-color: var(--jb-blue-border); }
.certificate .evidence-number { background: var(--jb-blue-solid); color: #fff; }
.certificate .evidence-tag { color: var(--jb-blue); border-color: var(--jb-blue-border); }
.registration-note { padding: 22px 0 0; }
.registration-note strong { font-size: 13px; font-weight: 650; }
.registration-note p { max-width: 920px; font-size: 12px; line-height: 1.9; color: var(--jb-text-secondary); margin-top: 8px; }
.criteria-detail { border: 1px solid var(--jb-border); border-radius: 12px; margin-top: 28px; padding-inline: 24px; }
summary { display: flex; align-items: center; justify-content: space-between; gap: 18px; cursor: pointer; font-size: 15px; font-weight: 600; line-height: 1.75; padding-block: 23px; list-style: none; }
summary::-webkit-details-marker { display: none; }
summary > span { font-size: 19px; font-weight: 400; color: var(--jb-text-secondary); flex-shrink: 0; }
details[open] > summary > span { transform: rotate(45deg); }
.detail-body { padding-bottom: 20px; }
.detail-body p { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.9; margin-bottom: 18px; }
.detail-body strong { color: var(--jb-ink); }
.thresholds { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; margin-bottom: 18px; max-width: 580px; }
.thresholds > div { padding: 18px; border-radius: 10px; background: var(--jb-bg-alt); }
.thresholds span { display: block; color: var(--jb-text-secondary); font-size: 12px; }
.thresholds strong { display: block; color: var(--jb-blue); font-size: 23px; margin-top: 6px; }
.detail-links { display: flex; flex-wrap: wrap; gap: 8px 28px; }
.detail-links a { display: inline-flex; align-items: center; gap: 12px; min-height: 36px; color: var(--jb-blue); font-size: 12px; }
.faq-grid { display: grid; grid-template-columns: .8fr 1.2fr; gap: 72px; }
.faq-intro { margin-top: 22px; color: var(--jb-text-secondary); font-size: 14px; line-height: 1.9; }
.text-link { display: inline-flex; align-items: center; gap: 16px; min-height: 44px; font-size: 13px; font-weight: 600; color: var(--jb-blue); margin-top: 17px; }
.examples details { border-bottom: 1px solid var(--jb-border); }
.examples details:first-child { border-top: 1px solid var(--jb-border); }
.examples p { font-size: 14px; line-height: 1.9; color: var(--jb-text-secondary); padding-bottom: 24px; }
.closing { padding-block: 82px; text-align: center; }
.closing h2 { margin-bottom: 20px; }
.closing .inner > p:not(.eyebrow) { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; }
.closing-actions { display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 29px; }
.button { display: inline-flex; align-items: center; justify-content: center; gap: 20px; min-height: 52px; padding: 13px 22px; border-radius: 10px; font-size: 14px; font-weight: 650; transition: background-color .2s; }
.primary { color: #fff; background: var(--jb-blue-solid); }
.primary:hover { background: var(--jb-blue-solid-hover); }
.secondary { border: 1px solid var(--jb-border); background: var(--jb-bg-alt); }
.secondary:hover { background: var(--jb-blue-light); }
.mobile-break { display: none; }

@media (max-width: 1024px) {
  .state-summary, .state-checks { padding: 27px; }
  .state-summary h3 { font-size: 25px; }
  .method { padding: 25px; }
  .method h3 { font-size: 23px; }
  .segment-card { gap: 28px; padding: 25px; }
  .evidence-grid { gap: 16px; }
  .evidence-grid article { padding: 22px; }
  .evidence-grid h3 { font-size: 17px; }
  .faq-grid { gap: 40px; }
}
@media (max-width: 760px) {
  .inner { width: calc(100% - 40px); }
  .vs-hero { padding-block: 44px 24px; }
  h1 { font-size: clamp(32px, 7.3vw, 44px); }
  h2 { font-size: 30px; }
  .hero-description { font-size: 15px; margin-top: 19px; }
  .vs-jump { gap: 8px; margin-top: 25px; }
  .vs-jump a { font-size: 11px; padding: 9px 12px; gap: 10px; }
  .section { padding-block: 58px; }
  .states-section { padding-top: 28px; }
  .section-heading { margin-bottom: 26px; }
  .intro { font-size: 14px; margin-top: 16px; }
  .state-selector { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; }
  .state-selector button { font-size: 12px; min-height: 52px; gap: 8px; }
  .selector-icon { width: 22px; height: 22px; font-size: 12px; }
  .status-detail { grid-template-columns: 1fr; border-radius: 14px; }
  .state-summary, .state-checks { padding: 24px; }
  .state-summary h3 { font-size: 26px; }
  .state-description { font-size: 13px; }
  .state-checks { border-left: 0; border-top: 1px solid var(--jb-border); }
  .state-checks dl > div { padding-block: 18px; }
  .state-checks strong { font-size: 14px; }
  .reason-panel { padding: 22px; }
  .reason-grid { grid-template-columns: 1fr; }
  .methods-grid { grid-template-columns: 1fr; gap: 16px; }
  .method { padding: 24px; }
  .method h3 { font-size: 23px; }
  .method > p { min-height: 0; font-size: 13px; }
  .segment-card { grid-template-columns: 1fr; gap: 24px; padding: 24px; margin-top: 16px; }
  .segment-copy h3 { font-size: 22px; }
  .time-axis, .match-axis { margin-left: 62px; }
  .track-row { gap: 10px; }
  .track-row > span { flex-basis: 52px; font-size: 10px; }
  .track, .match-axis { gap: 2px; }
  .track i { height: 19px; }
  .evidence-grid { grid-template-columns: 1fr; }
  .evidence-grid article { padding: 24px; }
  .evidence-grid h3 { font-size: 20px; }
  .criteria-detail { padding-inline: 20px; }
  summary { font-size: 14px; padding-block: 21px; }
  .thresholds { gap: 10px; }
  .thresholds > div { padding: 14px; }
  .thresholds span { font-size: 11px; }
  .faq-grid { grid-template-columns: 1fr; gap: 30px; }
  .examples p { font-size: 13px; }
  .closing { padding-block: 60px; }
  .closing .inner > p:not(.eyebrow) { font-size: 14px; }
  .button { padding-inline: 17px; gap: 13px; font-size: 13px; }
  .mobile-break { display: initial; }
}
@media (max-width: 380px) {
  .inner { width: calc(100% - 32px); }
  .state-summary, .state-checks { padding: 21px; }
  .state-summary h3 { font-size: 24px; }
  .state-selector button { font-size: 11px; }
  .segment-card { padding: 20px; }
}
@media (prefers-reduced-motion: reduce) {
  .state-selector button, .button { transition: none; }
}
</style>
