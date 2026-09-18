<script setup lang="ts">
const states = [
  { id: 'complete', label: '진본 확인 완료', icon: '✓', title: '비교와 등록 증거를 모두 확인했어요.', text: '파일 정확 일치 또는 영상·음성 비교 기준을 통과했고, 등록 기록과 보증서도 유효합니다.', action: '확인 방식과 등록자·등록 시각을 함께 살펴보세요.' },
  { id: 'similar', label: '콘텐츠 유사 · 확인 보류', icon: '!', title: '유사한 등록 영상은 찾았어요.', text: '비교 기준을 충족하지 못했거나 영상·음성 정보가 부족합니다. 일부 구간만 유사할 수도 있습니다.', action: '상세 사유와 대응 구간을 살펴보세요. 이 결과만으로 조작을 단정할 수 없으니 원 게시자나 공식 채널에서도 확인하세요.' },
  { id: 'unverified', label: '미인증', icon: '−', title: '등록 증거를 확인하지 못했어요.', text: '등록 기록을 찾지 못했거나, 등록이 비활성화되었거나, 보증서가 없거나 유효하지 않습니다.', action: '상세 사유를 살펴보세요. 미등록은 가짜라는 뜻이 아닙니다. 원 게시자나 공식 채널에서 내용과 등록 여부를 확인하세요.' },
  { id: 'unavailable', label: '현재 확인할 수 없음', icon: '…', title: '지금은 검증을 완료할 수 없어요.', text: '외부 서비스 연결 문제 또는 블록체인 등록 기록의 검증 문제로 판정할 수 없습니다.', action: '연결 문제는 재시도하고, 기록 불일치는 안내에 따라 운영자 확인이 필요합니다.' },
]
const examples = [
  { title: '등록 파일을 그대로 제출했어요.', text: '파일 전체의 SHA-256이 같고 등록 기록과 보증서가 유효하면, 파일 정확 일치로 확인됩니다. 오디오가 없는 파일도 가능합니다.' },
  { title: '재인코딩하거나 해상도를 바꿨어요.', text: '파일 지문이 달라지면 유사한 등록 후보를 찾고 영상·음성 지문을 비교합니다. 비교 기준과 등록 증거 검증을 모두 통과해야 완료로 표시됩니다.' },
  { title: '긴 영상에서 일부를 잘라 쇼츠로 만들었어요.', text: '후보 검색에 성공하고, 잘라낸 구간의 영상·음성이 같은 원본 시간대에 대응하며 비교 기준과 등록 증거 검증을 통과하면 승인될 수 있습니다. 생략된 앞뒤 맥락은 따로 확인해야 합니다.' },
  { title: '음성을 바꾸거나 오디오를 제거했어요.', text: '파일이 다른 경우 음성 비교 기준에 미달하거나 비교할 음성이 없으면 유사도 경로로 승인하지 않습니다. 일부 음성 변경은 샘플 비교에서 놓칠 수 있으므로 항상 탐지된다는 뜻은 아닙니다.' },
  { title: '얼굴·입모양, 자막·로고, 장면을 바꿨어요.', text: '변경 내용이 비교 샘플에 반영되어 기준에 미달하면 확인을 보류합니다. 작은 변화나 짧은 편집은 놓칠 수 있으며, 불일치만으로 딥페이크나 편집 여부를 확정하지 않습니다.' },
  { title: '등록은 되어 있는데 검증 완료가 아니에요.', text: '등록이 비활성화되었거나 보증서가 미발급·무효이면 완료로 표시하지 않습니다. 블록체인 기록이 남아 있는 것과 현재 검증 조건을 충족하는 것은 다릅니다.' },
]
</script>

<template>
  <div class="vs-page">
    <header class="vs-hero">
      <div class="vs-hero-inner">
        <span class="eyebrow">검증 결과 안내</span>
        <h1>공유하기 전,<br /><span>결과의 의미까지 확인하세요.</span></h1>
        <p>누가 등록했는지, 등록 영상과 어떻게 일치하는지.<br />결과별로 확인된 범위와 다음에 살펴볼 내용을 안내합니다.</p>
        <nav class="vs-jump" aria-label="검증 안내 바로가기"><a href="#states">상태의 의미</a><a href="#methods">확인 방식</a><a href="#examples">상황별 해석</a></nav>
      </div>
    </header>

    <section class="section" id="states">
      <div class="inner">
        <span class="eyebrow">결과 읽기</span>
        <h2>어떤 결과를 받으셨나요?</h2>
        <p class="intro">상태와 상세 사유를 함께 확인하면 다음에 무엇을 해야 할지 알 수 있습니다.</p>
        <div class="grid two">
          <article v-for="state in states" :key="state.id" class="card state" :class="state.id">
            <span class="state-label"><span aria-hidden="true">{{ state.icon }}</span>{{ state.label }}</span>
            <h3>{{ state.title }}</h3><p>{{ state.text }}</p>
            <div class="next"><span>다음으로</span><p>{{ state.action }}</p></div>
          </article>
        </div>
        <p class="note">이 페이지는 결과를 이해하기 위한 안내입니다. 이용 채널에 따라 ‘진본 확인 보류’, ‘등록 기록 없음’, ‘확인 중’처럼 문구가 다르게 표시될 수 있습니다.</p>
      </div>
    </section>

    <section class="section alternate" id="methods">
      <div class="inner">
        <span class="eyebrow">확인 방식</span>
        <h2>같은 완료 배지, 서로 다른 확인 범위.</h2>
        <p class="intro">두 방식 모두 등록 기록과 보증서가 유효해야 합니다. 결과의 ‘확인 방식’을 꼭 함께 읽어주세요.</p>
        <div class="grid two">
          <article class="card method exact">
            <span class="tag">파일 전체 비교</span><h3>등록 파일과 정확 일치</h3>
            <p>파일 전체에서 계산한 디지털 지문(SHA-256)이 같습니다.</p>
            <div class="basis"><span>확인한 것</span><strong>파일 전체의 동일성</strong></div>
            <p class="small">등록 파일을 그대로 제출한 경우에 해당합니다. 오디오가 없는 파일도 확인할 수 있습니다.</p>
          </article>
          <article class="card method sampled">
            <span class="tag">대표 장면 · 음성 비교</span><h3>영상·음성 비교 기준 통과</h3>
            <p>비교한 장면과 음성 지문이 등록 영상의 같은 시간대에 대응합니다.</p>
            <div class="basis"><span>확인한 것</span><strong>비교한 샘플의 대응 관계</strong></div>
            <p class="small">파일 전체가 같다는 뜻은 아닙니다. 샘플 사이의 편집이나 작은 변화는 놓칠 수 있습니다.</p>
          </article>
        </div>

        <div class="segment-card">
          <div><h3>등록 영상의 어느 구간과 일치하나요?</h3><p>6초짜리 제출 영상이 등록 영상의 3~9초 구간에 순서대로 대응하는 예시입니다.</p></div>
          <figure class="timeline">
            <div class="time-axis" aria-hidden="true"><span>0초</span><span>3초</span><span>9초</span><span>12초</span></div>
            <div class="track-row"><span>등록 영상</span><div class="track" aria-hidden="true"><i v-for="n in 12" :key="n" /></div></div>
            <div class="track-row"><span>제출 영상</span><div class="track" aria-hidden="true"><i v-for="n in 12" :key="n" :class="n > 3 && n <= 9 ? 'matched' : 'empty'" /></div></div>
            <div class="match-axis" aria-hidden="true"><span>3~9초 대응</span></div>
            <figcaption><strong>일부 구간이 일치해도 앞뒤 맥락은 따로 확인하세요.</strong> 생략된 내용까지 보증하지 않습니다. 위 도식은 구간 대응의 개념 예시이며, 실제 승인은 후보 검색·영상·음성 비교와 등록 증거 검증을 모두 통과해야 합니다.</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section" id="criteria">
      <div class="inner">
        <span class="eyebrow">판정 원리</span>
        <h2>영상 비교와 등록 증거를 함께 봅니다.</h2>
        <ol class="flow">
          <li><span class="step-number" aria-hidden="true">1</span><h3>등록 영상 찾기</h3><p>파일 지문으로 정확히 같은 기록을 찾습니다. 없으면 지각해시로 유사 후보를 검색합니다.</p></li>
          <li><span class="step-number" aria-hidden="true">2</span><h3>영상·음성 비교</h3><p>파일이 다른 경우 대표 장면과 음성 지문을 비교합니다. 정확 일치라면 이 단계를 건너뜁니다.</p></li>
          <li><span class="step-number" aria-hidden="true">3</span><h3>등록 증거 확인</h3><p>등록 상태, 블록체인 기록과 보증서의 유효성, 해당 영상과의 연결을 확인합니다.</p></li>
        </ol>
        <div class="callout"><strong>영상이 일치해도 등록 증거가 유효해야 검증 완료입니다.</strong><p>등록 후보의 정보가 표시되는 것만으로 제출 영상 전체가 확인된 것은 아닙니다.</p></div>
        <details class="criteria-detail">
          <summary>영상·음성 비교의 상세 기준</summary>
          <div class="detail-body">
            <p>파일이 다르면 후보 검색 후 <strong>1초 간격 대표 프레임과 음성 지문</strong>을 비교합니다. 모든 프레임을 검사하는 방식은 아닙니다.</p>
            <div class="thresholds"><div><span>영상 샘플 대응 비율</span><strong>95% 이상</strong></div><div><span>음성 샘플 대응 비율</span><strong>90% 이상</strong></div></div>
            <p><strong>이 수치는 승인 기준이며, 정확도나 조작 탐지율이 아닙니다.</strong> 순서가 보존되고 영상·음성의 최적 원본 대응 시간 오프셋이 같아야 합니다. 반복 장면 등으로 대응 시점이 다르면 확인을 보류합니다.</p>
            <p>음성 비교 정보가 없으면 유사도 경로로 승인하지 않습니다. 일부 불일치를 허용하므로 작은 화면 변화·짧은 편집·일부 음성 교체를 놓칠 수 있습니다.</p>
            <p>일부 결과는 캐시를 사용하므로 모든 요청에서 등록 증거를 새로 조회하는 것은 아닙니다. <a href="/developers/api/verify">검증 API 상세 보기 →</a></p>
          </div>
        </details>
      </div>
    </section>

    <section class="section alternate" id="examples">
      <div class="inner examples">
        <span class="eyebrow">상황별 해석</span><h2>이럴 때는 어떻게 읽어야 하나요?</h2>
        <p class="intro">이해를 돕기 위한 예시입니다. 실제 결과는 비교 기준과 등록 증거 확인에 따라 달라집니다.</p>
        <details v-for="example in examples" :key="example.title"><summary>{{ example.title }}</summary><p>{{ example.text }}</p></details>
        <div class="scope">
          <strong>등록 영상은 비교 기준으로 등록된 파일입니다.</strong>
          <p>촬영 원본 여부, 영상 속 사건의 사실성, AI 생성 여부, 제작자·저작권자 여부는 보증하지 않습니다. 등록 시각은 촬영 시각과 다르며, 등록자 표시명은 기관 소속·직함의 인증을 뜻하지 않습니다.</p>
        </div>
      </div>
    </section>

    <section class="closing"><h2>공유하기 전, 영상의 출처를 확인하세요.</h2><p>등록자와 등록 시각, 영상의 비교 결과를 함께 살펴보세요.</p><a class="primary" href="https://jinbon-web.vercel.app">영상 확인하기 <span aria-hidden="true">↗</span></a></section>
  </div>
</template>

<style scoped>
.vs-page { color: var(--jb-ink); }
.vs-hero { padding: 88px 24px; background: linear-gradient(150deg, var(--jb-blue-light), var(--jb-bg) 75%); border-bottom: 1px solid var(--jb-border); }
.vs-hero-inner { max-width: 1120px; margin: auto; }
.eyebrow { display: block; color: var(--jb-blue); font-size: 13px; font-weight: 700; margin-bottom: 18px; }
h1 { font-size: clamp(30px, 3.3vw, 44px); line-height: 1.35; letter-spacing: -.04em; font-weight: 750; margin: 0 0 24px; }
h1 span { color: var(--jb-blue); }
.vs-hero p { color: var(--jb-text-secondary); font-size: 19px; line-height: 1.8; margin: 0; }
.vs-jump { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 28px; }
.vs-jump a { padding: 9px 16px; border: 1px solid var(--jb-border); border-radius: 10px; background: var(--jb-bg); font-size: 14px; font-weight: 600; }
.vs-jump a:hover { border-color: var(--jb-blue); color: var(--jb-blue); }
.section { padding: 80px 24px; scroll-margin-top: 80px; }
.alternate { background: var(--jb-bg-alt); }
.inner { max-width: 1040px; margin: auto; }
h2 { font-size: 30px; line-height: 1.45; letter-spacing: -.025em; font-weight: 700; margin: 0 0 20px; }
h3 { font-size: 19px; line-height: 1.5; font-weight: 650; letter-spacing: -.02em; margin: 0 0 12px; }
.intro { color: var(--jb-text-secondary); font-size: 16px; line-height: 1.85; margin: 0 0 32px; }
.grid { display: grid; gap: 20px; }
.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.card { padding: 28px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); }
.card p { font-size: 15px; line-height: 1.8; color: var(--jb-text-secondary); margin: 0; }
.state { display: flex; flex-direction: column; align-items: flex-start; }
.state-label { display: inline-flex; align-items: center; gap: 8px; border-radius: 6px; padding: 4px 9px; font-size: 12px; font-weight: 650; margin-bottom: 18px; }
.complete .state-label { color: var(--jb-green); background: var(--jb-green-bg); }
.similar .state-label { color: var(--jb-yellow); background: var(--jb-yellow-bg); }
.unverified .state-label { color: var(--jb-neutral-fg); background: var(--jb-gray-bg); }
.unavailable .state-label { color: var(--jb-blue); background: var(--jb-blue-light); }
.next { width: 100%; border-top: 1px solid var(--jb-border); margin-top: 22px; padding-top: 16px; }
.next > span { font-size: 11px; font-weight: 600; color: var(--jb-blue); }
.next p { margin-top: 5px; font-size: 14px; color: var(--jb-text); }
.note { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.8; margin: 20px 0 0; }
.tag { display: inline-block; padding: 4px 9px; border-radius: 6px; font-size: 11px; font-weight: 600; color: var(--jb-blue); background: var(--jb-blue-light); margin-bottom: 18px; }
.exact { border-top: 3px solid var(--jb-green); }
.sampled { border-top: 3px solid var(--jb-blue); }
.method h3 { font-size: 23px; }
.basis { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 8px; background: var(--jb-bg-alt); border-radius: 8px; padding: 14px; margin: 24px 0 18px; font-size: 13px; }
.basis span { color: var(--jb-text-secondary); }
.card .small { font-size: 13px; }
.segment-card { margin-top: 24px; padding: 28px; border: 1px solid var(--jb-border); border-radius: 16px; background: var(--jb-bg); }
.segment-card p { color: var(--jb-text-secondary); font-size: 14px; line-height: 1.8; margin: 0; }
.timeline { margin: 24px 0 0; }
.time-axis { position: relative; height: 22px; margin-left: 80px; color: var(--jb-text-secondary); font-size: 11px; font-variant-numeric: tabular-nums; }
.time-axis span { position: absolute; }
.time-axis span:first-child { left: 0; }
.time-axis span:nth-child(2) { left: 25%; transform: translateX(-50%); }
.time-axis span:nth-child(3) { left: 75%; transform: translateX(-50%); }
.time-axis span:last-child { right: 0; }
.track-row { display: flex; align-items: center; gap: 16px; margin: 10px 0; }
.track-row > span { font-size: 12px; flex: 0 0 64px; color: var(--jb-text-secondary); }
.track { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 4px; flex: 1; }
.track i { height: 24px; border: 1px solid var(--jb-blue-border); border-radius: 4px; background: var(--jb-blue-light); }
.track .matched { background: var(--jb-green-bg); border-color: var(--jb-green); }
.track .empty { background: transparent; border: 1px dashed var(--jb-border); }
.match-axis { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 4px; margin-left: 80px; }
.match-axis span { grid-column: 4 / 10; border: solid var(--jb-green); border-width: 0 2px 2px; border-radius: 0 0 6px 6px; padding: 4px 0 7px; color: var(--jb-green); font-size: 12px; font-weight: 600; text-align: center; }
figcaption { color: var(--jb-text-secondary); font-size: 12px; line-height: 1.8; margin-top: 16px; }
figcaption strong { color: var(--jb-ink); }
.flow { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; list-style: none; padding: 0; margin: 32px 0; }
.step-number { display: grid; place-items: center; width: 28px; height: 28px; background: var(--jb-blue-light); color: var(--jb-blue); border-radius: 50%; font-size: 12px; font-weight: 700; margin-bottom: 16px; }
.flow p { font-size: 15px; line-height: 1.8; color: var(--jb-text-secondary); margin: 0; }
.callout, .scope { padding: 24px 28px; background: var(--jb-blue-light); border-radius: 14px; }
.callout strong, .scope strong { font-size: 15px; }
.callout p, .scope p { font-size: 14px; line-height: 1.8; color: var(--jb-text-secondary); margin: 8px 0 0; }
.criteria-detail { border: 1px solid var(--jb-border); border-radius: 14px; margin-top: 24px; padding: 0 24px; }
summary { cursor: pointer; font-size: 16px; font-weight: 600; padding: 24px 0; }
.detail-body { padding-bottom: 8px; }
.detail-body p, .examples details p { color: var(--jb-text-secondary); font-size: 15px; line-height: 1.9; margin: 0 0 20px; }
.detail-body strong { color: var(--jb-ink); }
.detail-body a { color: var(--jb-blue); text-decoration: underline; text-underline-offset: 4px; }
.thresholds { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; margin: 20px 0; }
.thresholds > div { padding: 18px; border-radius: 10px; background: var(--jb-bg-alt); }
.thresholds span { display: block; color: var(--jb-text-secondary); font-size: 13px; }
.thresholds strong { display: block; color: var(--jb-blue); font-size: 23px; margin-top: 6px; }
.examples { max-width: 800px; }
.examples details { border-bottom: 1px solid var(--jb-border); }
.scope { margin-top: 32px; }
.closing { padding: 72px 24px 88px; text-align: center; background: var(--jb-blue-light); }
.closing p { color: var(--jb-text-secondary); line-height: 1.8; margin: 0 0 28px; }
.primary { display: inline-flex; align-items: center; justify-content: center; gap: 14px; padding: 13px 22px; border: 1px solid transparent; border-radius: 10px; color: white; background: var(--jb-blue-solid); font-size: 15px; font-weight: 650; }
.primary:hover { background: var(--jb-blue-solid-hover); }
@media (max-width: 1000px) { .vs-hero { padding: 64px 24px; } .card { padding: 24px; } }
@media (max-width: 768px) {
  .vs-hero { padding: 48px 20px; }
  h1 { font-size: 32px; }
  .vs-hero p { font-size: 17px; }
  .section { padding: 52px 20px; }
  h2 { font-size: 26px; }
  .two, .flow, .thresholds { grid-template-columns: 1fr; }
  .grid { gap: 16px; }
  .segment-card, .callout, .scope { padding: 24px; }
  .track-row { flex-direction: column; align-items: stretch; gap: 6px; }
  .track-row > span { flex: auto; }
  .time-axis, .match-axis { margin-left: 0; }
  .closing { padding: 52px 20px; }
}
</style>
