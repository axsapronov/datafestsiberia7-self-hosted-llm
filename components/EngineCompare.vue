<script setup lang="ts">
// Сравнение inference-движков: лестница «сложность / возможности» (шкала 1–5).
// Сложность — порог входа (настройка, зависимости, параметры) — оранжевые точки.
// Возможности — что умеет движок (batching, квантизация, TP, API) — изумрудные.
// vLLM — featured («наш стек»): оптимум «сложность/возможности» (3/5 при 4/5).

interface Engine {
  name: string
  complexity: number
  capabilities: number
  when: string
  featured?: boolean
}

const ENGINES: Engine[] = [
  { name: 'Ollama', complexity: 1, capabilities: 1, when: '«Хочу просто попробовать ИИ»' },
  { name: 'llama.cpp', complexity: 2, capabilities: 3, when: '«Хочу запустить, но ресурсов немного»' },
  { name: 'vLLM', complexity: 3, capabilities: 4, when: '«Хочу production ИИ, ресурсы есть»', featured: true },
  { name: 'SGLang', complexity: 4, capabilities: 4, when: '«Хочу ИИ, готов страдать»' },
  { name: 'TensorRT-LLM', complexity: 5, capabilities: 5, when: '«Я богат, очень богат. Заверните всё»' },
]
</script>

<template>
  <div class="ec">
    <div class="ec-header">
      <div class="ec-h">Движок</div>
      <div class="ec-h">Сложность</div>
      <div class="ec-h">Возможности</div>
      <div class="ec-h">Когда брать</div>
    </div>

    <div class="ec-rows">
      <div v-for="e in ENGINES" :key="e.name" class="ec-row" :class="{ 'ec-row-featured': e.featured }">
        <div class="ec-name">
          <span class="ec-name-text">{{ e.name }}</span>
        </div>
        <div class="ec-dots ec-dots-complexity" :aria-label="`Сложность ${e.complexity} из 5`">
          <span v-for="i in 5" :key="'c' + i" class="ec-dot" :class="{ 'ec-dot-on': i <= e.complexity }"></span>
        </div>
        <div class="ec-dots ec-dots-caps" :aria-label="`Возможности ${e.capabilities} из 5`">
          <span v-for="i in 5" :key="'v' + i" class="ec-dot" :class="{ 'ec-dot-on': i <= e.capabilities }"></span>
        </div>
        <div class="ec-when">{{ e.when }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ec {
  width: 100%;
  margin-top: 1.5rem;
}

/* ── Шапка ──────────────────────────────────────────────────────────── */
.ec-header {
  display: grid;
  grid-template-columns: 168px 112px 112px 1fr;
  gap: 18px;
  align-items: baseline;
  padding: 0 0.4rem 0.55rem;
  border-bottom: 2px solid var(--ink);
}

.ec-h {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
}

/* ── Строки ─────────────────────────────────────────────────────────── */
.ec-row {
  display: grid;
  grid-template-columns: 168px 112px 112px 1fr;
  gap: 18px;
  align-items: center;
  padding: 0.68rem 0.4rem;
  border-bottom: 1px solid var(--hairline);
}

.ec-row:last-child {
  border-bottom: none;
}

.ec-row-featured {
  background: var(--surface-card);
}

.ec-name {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.ec-name-text {
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.ec-tag {
  font-family: var(--font-mono);
  font-size: 0.6rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent);
  background: rgba(59, 130, 246, 0.12);
  padding: 0.12rem 0.42rem;
  border-radius: 999px;
}

/* ── Точки-индикаторы (шкала 1–5) ───────────────────────────────────── */
.ec-dots {
  display: inline-flex;
  gap: 5px;
}

.ec-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: var(--hairline);
  display: inline-block;
}

.ec-dots-complexity .ec-dot-on {
  background: var(--badge-orange);
}

.ec-dots-caps .ec-dot-on {
  background: var(--badge-emerald);
}

.ec-when {
  font-size: 0.92rem;
  line-height: 1.35;
  color: var(--body);
}
</style>
