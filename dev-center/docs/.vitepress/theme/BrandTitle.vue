<script setup lang="ts">
import { watch } from 'vue'
import { useRoute, useRouter, withBase } from 'vitepress'

const route = useRoute()
const router = useRouter()
let clicks: number[] = []

function resetClicks() {
  clicks = []
}

function revealDeveloperCenter() {
  const now = performance.now()
  clicks = clicks.filter(time => now - time <= 1500)
  clicks.push(now)
  if (clicks.length === 5) {
    resetClicks()
    void router.go(withBase('/developers/guide/introduction'))
  }
}

watch(() => route.path, resetClicks)
</script>

<template>
  <div class="VPNavBarTitle brand-title">
    <a class="brand-home" :href="withBase('/')" aria-label="진본 홈으로">
      <img class="logo" :src="withBase('/logo.png')" alt="" width="28" height="28" />
    </a>
    <button type="button" class="brand-name" aria-label="진본, 빠르게 다섯 번 누르면 개발자 센터로 이동"
      @click="revealDeveloperCenter" @blur="resetClicks" @keydown="event => { if (event.repeat) event.preventDefault() }">진본</button>
  </div>
</template>

<style scoped>
.brand-title { display: flex; align-items: center; height: var(--vp-nav-height); border-bottom: 1px solid transparent; }
.brand-home { display: grid; place-items: center; min-height: 44px; }
.brand-name { min-width: 44px; min-height: 44px; padding: 0 6px; font: inherit; font-size: 16px; font-weight: 700; letter-spacing: -.01em; color: var(--vp-c-text-1); cursor: pointer; user-select: none; -webkit-user-select: none; touch-action: manipulation; }
.brand-home:focus-visible, .brand-name:focus-visible { outline: 2px solid var(--vp-c-brand-1); outline-offset: 2px; border-radius: 5px; }
@media (min-width: 960px) {
  :global(.VPNavBar.has-sidebar) .brand-title { border-bottom-color: var(--vp-c-divider); }
}
</style>
