<script setup lang="ts">
// Тюнинг inference-движка: алгоритм (4 шага) + 4 группы
// параметров (справочник по движкам). Палитра групп — badge pastels системы.

interface Step {
  num: string
  title: string
  sub: string
  hub?: boolean
}

const STEPS: Step[] = [
  { num: '01', title: 'Сформулировать задачу', sub: 'тип · контекст · concurrency · SLA' },
  { num: '02', title: 'Бэкап конфига', sub: 'зафиксировать базовый конфиг' },
  { num: '03', title: 'Поменять параметр', sub: 'одна группа за раз', hub: true },
  { num: '04', title: 'Проверка и стабилизация', sub: 'TTFT · TPOT · OOM · load-test 24–72h' },
]

interface Group {
  letter: string
  name: string
  color: string
  vllm: string
  llama: string
}

const GROUPS: Group[] = [
  {
    letter: 'A',
    name: 'Память / KV-cache',
    color: 'var(--badge-emerald)',
    vllm: 'gpu-memory-utilization 0.85–0.92 · max-model-len',
    llama: 'n_ctx · n_gpu_layers',
  },
  {
    letter: 'B',
    name: 'Batching / scheduler',
    color: 'var(--accent)',
    vllm: 'max-num-seqs · max-num-batched-tokens 4096–16384 · chunked-prefill',
    llama: 'n_batch · threads = физ. ядра',
  },
  {
    letter: 'C',
    name: 'Ускорения',
    color: 'var(--badge-violet)',
    vllm: 'speculative decoding (MTP/EAGLE) · flash attn · prefix caching',
    llama: 'flash attention · MTP draft-tokens',
  },
  {
    letter: 'D',
    name: 'Железо / топология',
    color: 'var(--badge-orange)',
    vllm: 'tensor-parallel-size · pipeline-parallel-size · OMP_NUM_THREADS',
    llama: 'n_gpu_layers (offload) · --threads',
  },
]
</script>

<template>
  <div class="et">
    

    <div class="et-tablewrap">
      <table class="et-table">
        <thead>
          <tr>
            <th>Группа</th>
            <th>vLLM</th>
            <th>llama.cpp / Ollama</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="g in GROUPS" :key="g.letter">
            <td>
              <span class="et-group">
                <span class="et-group-dot" :style="{ background: g.color }" aria-hidden="true"></span>
                <span class="et-group-letter">{{ g.letter }}</span>
                {{ g.name }}
              </span>
            </td>
            <td class="et-params">{{ g.vllm }}</td>
            <td class="et-params">{{ g.llama }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="et-flowwrap">
      <div class="et-flow">
        <template v-for="(s, i) in STEPS" :key="s.num">
          <div class="et-step" :class="{ 'et-step-hub': s.hub }">
            <div class="et-step-top">
              <span class="et-step-num">{{ s.num }}</span>
              <span v-if="s.hub" class="et-hub-dots" aria-hidden="true">
                <i v-for="g in GROUPS" :key="g.letter" class="et-hub-dot" :style="{ background: g.color }"></i>
              </span>
            </div>
            <div class="et-step-title">{{ s.title }}</div>
            <div class="et-step-sub">{{ s.sub }}</div>
          </div>
          <div v-if="i < STEPS.length - 1" class="et-arrow" aria-hidden="true">
            <svg width="16" height="16" viewBox="0 0 20 20" fill="none">
              <path d="M7 4l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
        </template>
      </div>

      <div class="et-loop" aria-hidden="true">
        <svg class="et-loop-arrow" width="16" height="16" viewBox="0 0 20 20" fill="none">
          <path d="M13 4l-6 6 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        <span class="et-loop-line"></span>
        <span class="et-loop-label">нет · OOM · деградация — назад к шагу 03</span>
        <span class="et-loop-line"></span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.et {
  width: 100%;
  margin-top: 0.3rem;
}

.et-cap {
  margin-top: 0.2rem;
  margin-bottom: 0.9rem;
}

/* ── Поток алгоритма ─────────────────────────────────────────────────── */
.et-flowwrap {
  margin-top: 1rem;
}

.et-flow {
  display: flex;
  align-items: stretch;
  gap: 0.3rem;
}

.et-step {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 10px;
  padding: 0.5rem 0.55rem;
}

/* Шаг-хаб (смена параметра) — единственный акцентный surface в потоке */
.et-step-hub {
  background: var(--canvas);
  border: 1.5px solid var(--accent);
}

.et-step-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.3rem;
}

.et-step-num {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--muted);
}

/* 4 точки групп (A–D) внутри шага-хаба */
.et-hub-dots {
  display: inline-flex;
  gap: 3px;
}

.et-hub-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: inline-block;
}

.et-step-title {
  font-size: 0.88rem;
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.et-step-sub {
  font-family: var(--font-mono);
  font-size: 0.62rem;
  line-height: 1.3;
  color: var(--muted);
}

.et-arrow {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--muted-soft);
}

/* Возвратный цикл (деградация → назад к смене параметра) */
.et-loop {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 0.5rem;
  color: var(--muted-soft);
}

.et-loop-line {
  flex: 1;
  border-top: 1.5px dashed var(--hairline);
}

.et-loop-label {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  letter-spacing: 0.02em;
  color: var(--muted);
  white-space: nowrap;
}

/* ── Справочник по группам ──────────────────────────────────────────── */
.et-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.78rem;
}

.et-table th {
  text-align: left;
  font-weight: 500;
  color: var(--ink);
  padding: 0.35rem 0.6rem;
  border-bottom: 2px solid var(--ink);
}

.et-table td {
  padding: 0.42rem 0.6rem;
  border-bottom: 1px solid var(--hairline);
  color: var(--body);
  vertical-align: top;
}

.et-table tr:last-child td {
  border-bottom: none;
}

.et-group {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
  white-space: nowrap;
}

.et-group-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.et-group-letter {
  font-family: var(--font-mono);
  font-weight: 600;
  color: var(--muted);
}

.et-params {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  line-height: 1.45;
  color: var(--body);
}
</style>
