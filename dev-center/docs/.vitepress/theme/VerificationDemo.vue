<script setup lang="ts">
import { computed, ref } from 'vue'

const examples = [
  {
    id: 'exact', label: '같은 파일', file: '발표 영상.mp4', caption: '등록했던 파일을 그대로 전달한 경우',
    status: '파일 정확 일치', title: '등록 파일과 정확히 같아요.',
    description: '파일 전체의 디지털 지문이 같고, 등록 기록과 보증서도 유효한 경우입니다.',
    scope: '파일 전체의 동일성', next: '등록자와 등록 시각을 함께 확인하세요. 등록 전 편집 여부나 영상 속 내용의 사실성까지 확인한 것은 아닙니다.',
    timeline: '등록 파일과 제출 파일 전체가 같은 예시입니다.',
  },
  {
    id: 'segment', label: '짧게 자른 영상', file: '발표 영상_일부.mp4', caption: '등록 영상에서 일부 구간을 가져온 경우',
    status: '영상·음성 비교 기준 통과', title: '등록 영상의 일부 구간과 대응해요.',
    description: '후보 검색과 영상·음성 비교 기준을 통과하고, 등록 기록과 보증서도 유효한 경우입니다.',
    scope: '비교한 장면과 음성의 대응 관계', next: '생략된 앞뒤 맥락도 살펴보세요. 파일 전체의 동일성을 뜻하지 않으며, 작은 변화나 짧은 편집은 놓칠 수 있습니다.',
    timeline: '6초짜리 제출 영상이 등록 영상의 3~9초 구간에 대응하는 개념 예시입니다.',
  },
  {
    id: 'missing', label: '등록 기록 없음', file: '다른 영상.mp4', caption: '비교할 등록 기록을 찾지 못한 경우',
    status: '등록 기록을 찾지 못함', title: '아직 비교할 기준이 없어요.',
    description: '현재 진본에서 비교할 등록 영상을 찾지 못한 경우입니다. 이 결과만으로 가짜나 조작 영상이라고 판단할 수 없습니다.',
    scope: '일치 여부를 확인할 수 없음', next: '영상을 전달한 사람에게 사전 등록 여부를 확인하세요. 등록된 파일이나 지원하는 링크로 다시 확인할 수 있습니다.',
    timeline: '제출 영상에 대응하는 등록 기록을 찾지 못한 예시입니다.',
  },
]
const selected = ref('exact')
const example = computed(() => examples.find(item => item.id === selected.value)!)
</script>

<template>
  <div class="demo">
    <div class="demo-options" role="group" aria-label="살펴볼 결과 예시 선택">
      <button v-for="(item, index) in examples" :key="item.id" type="button"
        :aria-pressed="selected === item.id" aria-controls="demo-result" @click="selected = item.id">
        <span class="option-number" aria-hidden="true">0{{ index + 1 }}</span>{{ item.label }}
      </button>
    </div>
    <div class="demo-workspace" :class="selected">
      <div class="demo-input">
        <span class="overline">비교할 영상 · 가상 예시</span>
        <div class="file-preview" aria-hidden="true">
          <div class="film-frame"><span class="frame-corner top" /><span class="file-format">MP4<span>영상 파일 예시</span></span><span class="frame-corner bottom" /><span class="frame-label">JINBON / EXAMPLE</span></div>
          <span class="file-name">{{ example.file }}</span>
        </div>
        <p class="input-caption">{{ example.caption }}</p>
        <figure class="timeline">
          <div class="track-row"><span>등록 영상</span><div class="track" :class="{ empty: selected === 'missing' }" aria-hidden="true"><i v-for="n in 12" :key="n" /></div></div>
          <div class="track-row"><span>제출 영상</span><div class="track submitted" aria-hidden="true"><i v-for="n in 12" :key="n" :class="{ faded: selected === 'segment' && (n <= 3 || n > 9) }" /></div></div>
          <figcaption>{{ example.timeline }}</figcaption>
        </figure>
      </div>
      <div id="demo-result" class="demo-result" role="region" aria-label="선택한 상황의 결과 예시">
        <span class="overline">결과를 이렇게 읽어보세요</span>
        <div aria-live="polite" aria-atomic="true" class="result-heading">
          <span class="status"><span aria-hidden="true">{{ selected === 'missing' ? '−' : '✓' }}</span>{{ example.status }}</span>
          <h3>{{ example.title }}</h3>
        </div>
        <p class="result-description">{{ example.description }}</p>
        <dl class="evidence">
          <div><dt>확인한 범위</dt><dd>{{ example.scope }}</dd></div>
          <template v-if="selected !== 'missing'">
            <div><dt>등록자 · 예시</dt><dd>김진본</dd></div>
            <div><dt>등록 시각 · 예시</dt><dd>2026. 09. 01. 10:30</dd></div>
            <div><dt>등록 기록 · 보증서</dt><dd>유효함 <span class="evidence-check" aria-hidden="true">✓</span></dd></div>
          </template>
          <div v-else><dt>등록자 · 등록 시각</dt><dd>확인할 기록 없음</dd></div>
        </dl>
        <div class="next-step"><strong>{{ selected === 'missing' ? '다음으로 할 일' : '함께 살펴볼 것' }}</strong><p>{{ example.next }}</p></div>
      </div>
    </div>
    <div class="demo-footer"><p>이해를 돕기 위한 가상 예시입니다. 실제 영상을 분석한 결과가 아니며, 짧게 자른 영상이 항상 승인되는 것은 아닙니다.</p><a href="/verification-status">모든 결과의 의미 보기 <span aria-hidden="true">→</span></a></div>
  </div>
</template>

<style scoped>
.demo { border: 1px solid var(--jb-border); border-radius: 24px; background: var(--jb-bg); overflow: hidden; }
.demo-options { display: flex; gap: 8px; padding: 16px; border-bottom: 1px solid var(--jb-border); background: var(--jb-bg-alt); }
.demo-options button { display: flex; align-items: center; justify-content: center; gap: 12px; flex: 1; padding: 14px 12px; border: 1px solid transparent; border-radius: 10px; font: inherit; font-size: 14px; font-weight: 600; color: var(--jb-text-secondary); cursor: pointer; transition: background-color .15s; }
.demo-options button:hover { background: var(--jb-blue-light); color: var(--jb-blue); }
.demo-options button[aria-pressed="true"] { background: var(--jb-bg); border-color: var(--jb-blue-border); color: var(--jb-blue); box-shadow: 0 2px 8px #00000006; }
.demo-options button:focus-visible { outline: 2px solid var(--jb-blue); outline-offset: 2px; }
.option-number { font-size: 11px; font-variant-numeric: tabular-nums; }
.demo-workspace { display: grid; grid-template-columns: 1fr 1.15fr; }
.demo-input { padding: 36px; background: var(--jb-bg-alt); border-right: 1px solid var(--jb-border); }
.overline { color: var(--jb-text-secondary); font-size: 12px; font-weight: 600; }
.file-preview { margin-top: 24px; border: 1px solid var(--jb-blue-border); border-radius: 14px; overflow: hidden; background: var(--jb-bg); }
.film-frame { height: 142px; position: relative; display: grid; place-items: center; color: var(--jb-blue); background: linear-gradient(130deg, var(--jb-blue-light), var(--jb-bg)); }
.file-format { display: grid; gap: 6px; text-align: center; font-size: 23px; font-weight: 650; letter-spacing: .08em; }
.file-format > span { font-size: 10px; font-weight: 400; letter-spacing: 0; color: var(--jb-text-secondary); }
.frame-corner { position: absolute; width: 14px; height: 14px; border: solid var(--jb-blue-border); }
.frame-corner.top { top: 16px; left: 16px; border-width: 1px 0 0 1px; }
.frame-corner.bottom { right: 16px; bottom: 16px; border-width: 0 1px 1px 0; }
.frame-label { position: absolute; bottom: 14px; left: 16px; font-size: 8px; letter-spacing: .1em; }
.file-name { display: block; border-top: 1px solid var(--jb-border); padding: 12px 16px; font-size: 13px; font-weight: 600; }
.input-caption { color: var(--jb-text-secondary); font-size: 13px; line-height: 1.7; margin: 12px 0 24px; }
.timeline { margin: 0; }
.track-row { display: flex; align-items: center; gap: 12px; margin: 12px 0; }
.track-row > span { flex: 0 0 58px; font-size: 11px; color: var(--jb-text-secondary); }
.track { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); flex: 1; gap: 3px; }
.track i { height: 20px; background: var(--jb-blue-light); border: 1px solid var(--jb-blue-border); border-radius: 3px; }
.submitted i { background: var(--jb-green-bg); border-color: var(--jb-green); }
.segment .submitted i { background: var(--jb-blue); border-color: var(--jb-blue); }
.segment .submitted i.faded, .track.empty i { background: transparent; border: 1px dashed var(--jb-border); }
.missing .submitted i { background: var(--jb-gray-bg); border-color: var(--jb-neutral-fg); }
figcaption { font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); margin-top: 16px; }
.demo-result { padding: 36px; min-width: 0; min-height: 565px; }
.result-heading { margin-top: 24px; }
.status { display: inline-flex; align-items: center; gap: 7px; color: var(--jb-green); background: var(--jb-green-bg); padding: 5px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }
.segment .status { color: var(--jb-blue); background: var(--jb-blue-light); }
.missing .status { color: var(--jb-neutral-fg); background: var(--jb-gray-bg); }
h3 { font-size: 25px; line-height: 1.5; letter-spacing: -.03em; font-weight: 700; margin: 16px 0 12px; }
.result-description { font-size: 14px; line-height: 1.85; color: var(--jb-text-secondary); margin: 0; }
.evidence { margin: 24px 0; border-top: 1px solid var(--jb-border); padding-top: 12px; }
.evidence > div { display: flex; justify-content: space-between; gap: 18px; padding: 8px 0; font-size: 12px; line-height: 1.7; }
dt { color: var(--jb-text-secondary); flex-shrink: 0; }
dd { margin: 0; text-align: right; font-weight: 600; }
.evidence-check { color: var(--jb-green); }
.next-step { padding: 16px 18px; border-radius: 10px; background: var(--jb-bg-alt); }
.next-step strong { font-size: 12px; }
.next-step p { margin: 6px 0 0; font-size: 13px; line-height: 1.8; color: var(--jb-text-secondary); }
.demo-footer { display: flex; align-items: center; gap: 24px; justify-content: space-between; padding: 20px 28px; border-top: 1px solid var(--jb-border); }
.demo-footer p { max-width: 660px; margin: 0; font-size: 12px; line-height: 1.8; color: var(--jb-text-secondary); }
.demo-footer a { flex-shrink: 0; color: var(--jb-blue); font-size: 13px; font-weight: 600; }
@media (max-width: 768px) {
  .demo { border-radius: 16px; }
  .demo-options { gap: 4px; padding: 8px; }
  .demo-options button { padding: 12px 8px; font-size: 12px; min-height: 48px; }
  .option-number { display: none; }
  .demo-workspace { grid-template-columns: 1fr; }
  .demo-input { padding: 24px; border-right: 0; border-bottom: 1px solid var(--jb-border); }
  .file-preview { margin-top: 16px; }
  .film-frame { display: none; }
  .file-name { border-top: 0; }
  .input-caption { margin-bottom: 18px; }
  .track-row { margin: 8px 0; }
  .track i { height: 14px; }
  .demo-result { padding: 24px; min-height: 0; }
  .result-heading { margin-top: 16px; }
  h3 { font-size: 22px; }
  .demo-footer { align-items: flex-start; flex-direction: column; gap: 12px; padding: 20px 24px; }
}
</style>
