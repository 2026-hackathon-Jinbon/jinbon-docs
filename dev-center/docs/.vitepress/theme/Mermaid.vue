<template>
  <div class="mermaid-wrapper" ref="el"></div>
</template>

<script setup>
import { ref, onMounted, watch, useSlots } from "vue";

const props = defineProps({ code: { type: String, default: "" } });
const el = ref(null);
const slots = useSlots();

let mermaidInstance = null;
let idCounter = 0;

async function render() {
  if (!el.value) return;
  if (!mermaidInstance) {
    const m = await import("mermaid");
    mermaidInstance = m.default;
    mermaidInstance.initialize({
      startOnLoad: false,
      theme: "base",
      themeVariables: {
        primaryColor: "#EEF4FF",
        primaryTextColor: "#111827",
        primaryBorderColor: "#C3D3FC",
        secondaryColor: "#F7F8FC",
        lineColor: "#98A2B3",
        fontFamily: "Arial, Apple SD Gothic Neo, sans-serif",
      },
    });
  }
  const raw = props.code || el.value.textContent || "";
  const code = decodeURIComponent(raw);
  if (!code.trim()) return;
  const id = `mermaid-${Date.now()}-${idCounter++}`;
  try {
    const { svg } = await mermaidInstance.render(id, code.trim());
    el.value.innerHTML = svg;
  } catch (e) {
    el.value.innerHTML = `<pre style="color:red">${e.message}</pre>`;
  }
}

onMounted(render);
watch(() => props.code, render);
</script>

<style scoped>
.mermaid-wrapper {
  display: flex;
  justify-content: center;
  margin: 1.5rem 0;
  overflow-x: auto;
}
.mermaid-wrapper :deep(svg) {
  max-width: 100%;
  height: auto;
}
</style>
