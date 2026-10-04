<script setup lang="ts">
// Матрица моделей для consumer-железа: размерный класс → класс задач → примеры.
// Принцип: одна задача = одна модель в своём размерном классе.
// Consumer (RTX 3090/4090, 24–48 GB VRAM) — до 35B; 70B+ — только datacenter.
// Последняя колонка (≤ 35B) — featured: наш выбор Qwen3.8-27B-AWQ-MTP на 2×RTX 3090.

interface Model {
  name: string
  meta: string
  featured?: boolean
}

interface Column {
  size: string
  task: string
  dot: string
  models: Model[]
  featured?: boolean
}

const COLUMNS: Column[] = [
  {
    size: '≤ 3B',
    task: 'Документы, аудио, спец. задачи',
    dot: 'var(--success)',
    models: [
      { name: 'Mellum-4b', meta: 'Автодополнение кода' },
      { name: 'MinerU / PaddleOCR-VL', meta: 'PDF → Markdown · 1B' },
      { name: 'DeepSeek-OCR', meta: 'Batch OCR · 3B MoE · MIT' },
      { name: 'Whisper-Podlodka', meta: 'ASR · русский' },
    ],
  },
  {
    size: '≤ 8B',
    task: 'RAG · поиск',
    dot: 'var(--warning)',
    models: [
      { name: 'bge-m3', meta: 'dense + sparse + ColBERT' },
      { name: 'Qwen3-Embedding', meta: 'код · 32K · MRL' },
      { name: 'Qwen3-Reranker-4B', meta: 'cross-encoder · 32K' },
      { name: 'ruBERT-ruLaw', meta: 'юридический RAG' },
    ],
  },
  {
    size: '≤ 15B',
    task: 'Рефакторинг · Базовый SDLC',
    dot: 'var(--badge-violet)',
    models: [
      { name: 'Mellum2-12B-A2.5B', meta: 'Оркестрация задач · выполнение команд' },
      { name: 'Devstral-Small-2-24B', meta: 'Mistral · agentic · 24B' },
      { name: 'DeepSeek Coder V2 Lite', meta: 'MoE · 2.4B active · MIT' },
    ],
  },
  {
    size: '≤ 35B',
    task: 'Проектирование и реализация',
    dot: 'var(--accent)',
    featured: true,
    models: [
      { name: 'Qwen3.8-27B', meta: 'MTP · 262K контекст · vision', featured: true },
      { name: 'T-pro-it-2.1', meta: 'RU RAG · tools > Qwen3-32B' },
    ],
  },
]
</script>

<template>
  <div class="mm">
    <div v-for="c in COLUMNS" :key="c.size" class="mm-col" :class="{ 'mm-col-featured': c.featured }">
      <div class="mm-head">
        <span class="mm-dot" :style="{ background: c.dot }"></span>
        <span class="mm-size">{{ c.size }}</span>
      </div>
      <div class="mm-task">{{ c.task }}</div>
      <ul class="mm-models">
        <li v-for="m in c.models" :key="m.name" class="mm-model" :class="{ 'mm-model-featured': m.featured }">
          <div class="mm-model-top">
            <span class="mm-name">{{ m.name }}</span>
            <span v-if="m.featured" class="mm-badge">Наш выбор</span>
          </div>
          <span class="mm-meta">{{ m.meta }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.mm {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-top: 0.5rem;
}

.mm-col {
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 14px;
  padding: 0.9rem 1rem;
  margin-top: 1.5rem;
}

.mm-col-featured {
  border: 1.5px solid var(--accent);
}

.mm-head {
  display: flex;
  align-items: center;
  gap: 8px;
}

.mm-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  flex-shrink: 0;
}

.mm-size {
  font-size: 1.7rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--ink);
}

/* min-height на 2 строки — списки моделей начинаются на одной высоте
   во всех колонках, независимо от переноса task-подписи */
.mm-task {
  margin-top: 0.2rem;
  margin-bottom: 0.8rem;
  min-height: 2.5em;
  font-size: 0.82rem;
  font-weight: 500;
  line-height: 1.25;
  color: var(--body);
}

.mm-models {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.95rem;
}

.mm-model-top {
  display: flex;
  align-items: center;
  gap: 6px;
}

.mm-name {
   font-size: 0.88rem;
   font-weight: 500;
   line-height: 1.25;
   letter-spacing: -0.01em;
   color: var(--ink);
}

.mm-model-featured .mm-name {
  font-weight: 600;
}

.mm-badge {
  font-family: var(--font-mono);
  font-size: 0.6rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent);
  background: rgba(59, 130, 246, 0.12);
  padding: 0.1rem 0.4rem;
  border-radius: 999px;
  white-space: nowrap;
}

.mm-meta {
  display: block;
  margin-top: 0.15rem;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  line-height: 1.35;
  color: var(--muted);
}
</style>
