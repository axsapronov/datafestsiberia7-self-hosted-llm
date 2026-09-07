<script setup lang="ts">
// GPUStack — панель управления self-hosted.
// Слева — 4 возможности панели, каждая со своей мини-визуализацией.
// Справа — 2×2 сетка: 3 скриншота реального UI (Каталог, Deployments, Chat)
// + мини-график Usage & Billing (кто сколько сжёг).

interface Capability {
  dot: string
  label: string
  desc: string
}

// 4 возможности панели — цвета совпадают с палитрой параметров дека
// (api → #f59e0b, manage → #0ea5e9 из stage-data.ts).
const CAPS: Capability[] = [
  { dot: '#10b981', label: 'Модели', desc: 'Hugging Face → replicas N → auto-restart' },
  { dot: '#8b5cf6', label: 'Движки', desc: 'подключаемые inference-рантаймы' },
  { dot: '#f59e0b', label: 'API', desc: 'OpenAI-совместимый, доступ по моделям' },
  { dot: '#0ea5e9', label: 'Статистика', desc: 'токены и запросы по пользователям и ключам' },
]

// Usage & Billing: мини-график «кто сколько сжёг» (токены по пользователям).
const USAGE = [
  { name: 'pi.dev', value: 42, color: '#0ea5e9' },
  { name: 'Cursor', value: 28, color: '#8b5cf6' },
  { name: 'Kilo', value: 12, color: '#f59e0b' },
]
const USAGE_MAX = Math.max(...USAGE.map((u) => u.value))
</script>

<template>
  <div class="gs">
    <!-- ── Слева: 4 возможности панели ─────────────────────────────── -->
    <div class="gs-left">
      <div v-for="cap in CAPS" :key="cap.label" class="gs-card">
        <div class="gs-card-head">
          <span class="gs-dot" :style="{ background: cap.dot }" aria-hidden="true"></span>
          <span class="gs-label">{{ cap.label }}</span>
        </div>
        <div class="gs-desc">{{ cap.desc }}</div>

        <!-- Мини-визуализация — своя для каждой возможности -->
        <div class="gs-mini">
          <!-- Модели: статус деплоя -->
          <span v-if="cap.label === 'Модели'" class="gs-pill gs-pill-run">
            <span class="gs-pill-dot" aria-hidden="true"></span>Running · 1/1
          </span>

          <!-- Движки: подключаемые рантаймы -->
          <span v-else-if="cap.label === 'Движки'" class="gs-engines">
            <span class="gs-chip">llama.cpp</span>
            <span class="gs-chip">vLLM</span>
            <span class="gs-chip">SGLang</span>
            <span class="gs-chip">TensorRT-LLM</span>
          </span>

          <!-- API: OpenAI-совместимый endpoint + ключ -->
          <span v-else-if="cap.label === 'API'" class="gs-api">
            <span class="gs-code">POST /v1/chat/completions</span>
            <span class="gs-kv">Bearer · per-model</span>
          </span>

          <!-- Статистика: скорость + счётчик -->
          <span v-else class="gs-stats">
            <span class="gs-metric">343<span class="gs-metric-unit"> tok/s</span></span>
            <span class="gs-kv">tokens / user / key</span>
          </span>
        </div>
      </div>
    </div>

    <!-- ── Справа: 2×2 — 3 скриншота + Usage-график ───────────────── -->
    <div class="gs-right">
      <div class="gs-cell">
        <div class="gs-shot">
          <img src="/img/gpustack/quick-start-qwen3.png" alt="GPUStack Catalog: выбор модели из каталога (Qwen, GLM, Gemma, Nemotron)" />
          <span class="gs-shot-label">Каталог</span>
        </div>
        <div class="gs-shot-cap">выбираем модель из каталога</div>
      </div>

      <div class="gs-cell">
        <div class="gs-shot">
          <img src="/img/gpustack/model-running.png" alt="GPUStack Deployments: модель в статусе Running, реплики 1/1" />
          <span class="gs-shot-label">Deployments</span>
        </div>
        <div class="gs-shot-cap">Running · реплики · auto-restart</div>
      </div>

      <div class="gs-cell">
        <div class="gs-shot">
          <img src="/img/gpustack/quick-chat.png" alt="GPUStack Chat: ответ модели, Token Usage 62, Output 343.28 Tokens/s" />
          <span class="gs-shot-label">Chat</span>
        </div>
        <div class="gs-shot-cap">343 tok/s · Token Usage</div>
      </div>

      <div class="gs-cell">
        <div class="gs-shot gs-shot-usage">
          <span class="gs-shot-label">Usage &amp; Billing</span>
          <div class="gs-usage">
            <div v-for="u in USAGE" :key="u.name" class="gs-usage-row">
              <span class="gs-usage-name">{{ u.name }}</span>
              <span class="gs-usage-track">
                <span class="gs-usage-fill" :style="{ width: (u.value / USAGE_MAX) * 100 + '%', background: u.color }"></span>
              </span>
              <span class="gs-usage-val">{{ u.value }}M</span>
            </div>
          </div>
        </div>
        <div class="gs-shot-cap">кто сколько сжёг — по пользователям</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gs {
  display: flex;
  gap: 1.1rem;
  width: 100%;
  height: 398px;
  margin-top: 0.4rem;
  align-items: stretch;
}

/* ── Левая колонка: 4 карточки возможностей ───────────────────────── */
.gs-left {
  flex: 0 0 34%;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.gs-card {
  flex: 1;
  min-height: 0;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.22rem;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  padding: 0.45rem 0.8rem;
}

.gs-card-head {
  display: flex;
  align-items: center;
  gap: 0.45rem;
}

.gs-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  flex-shrink: 0;
}

.gs-label {
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.gs-desc {
  font-size: 0.72rem;
  line-height: 1.3;
  color: var(--body);
}

.gs-mini {
  margin-top: 0.1rem;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.35rem;
  min-height: 1.25rem;
}

/* Модели: статус-пилюля */
.gs-pill-run {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  line-height: 1.2;
  color: var(--success);
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.25);
  padding: 0.14rem 0.5rem;
  border-radius: 999px;
}
.gs-pill-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--success);
}

/* Движки: чипы рантаймов */
.gs-engines {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
}
.gs-chip {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  font-weight: 500;
  color: var(--body);
  background: var(--surface-soft);
  border: 1px solid var(--hairline);
  padding: 0.1rem 0.42rem;
  border-radius: 6px;
}

/* API: код-чип */
.gs-api {
  display: flex;
  flex-direction: column;
  gap: 0.15rem;
}
.gs-code {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 500;
  line-height: 1.2;
  color: var(--ink);
  background: var(--surface-soft);
  border: 1px solid var(--hairline);
  padding: 0.14rem 0.5rem;
  border-radius: 6px;
  white-space: nowrap;
}

/* Статистика: метрика */
.gs-stats {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
}
.gs-metric {
  font-family: var(--font-mono);
  font-size: 1rem;
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--ink);
}
.gs-metric-unit {
  font-size: 0.72rem;
  font-weight: 500;
  color: var(--muted);
}

.gs-kv {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  font-weight: 500;
  line-height: 1.2;
  letter-spacing: 0.03em;
  color: var(--muted);
}

/* ── Правая колонка: 2×2 сетка ────────────────────────────────────── */
.gs-right {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 0.55rem;
  min-width: 0;
}

.gs-cell {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  min-width: 0;
}

.gs-shot {
  position: relative;
  flex: 1;
  min-height: 0;
  border: 1px solid var(--hairline);
  border-radius: 10px;
  overflow: hidden;
  background: var(--surface-soft);
}

.gs-shot img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

.gs-shot-label {
  position: absolute;
  top: 0.4rem;
  left: 0.4rem;
  font-family: var(--font-mono);
  font-size: 0.62rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--ink);
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid var(--hairline);
  padding: 0.08rem 0.4rem;
  border-radius: 6px;
}

.gs-shot-cap {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  letter-spacing: 0.02em;
  color: var(--muted);
}

/* Usage-ячейка: мини-график вместо скриншота */
.gs-shot-usage {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.5rem;
  padding: 1.1rem 0.9rem 0.8rem;
}
.gs-shot-usage .gs-shot-label {
  position: static;
  background: none;
  border: none;
  padding: 0;
  color: var(--muted);
}
.gs-usage {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.gs-usage-row {
  display: grid;
  grid-template-columns: 52px 1fr 34px;
  align-items: center;
  gap: 0.45rem;
}
.gs-usage-name {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  color: var(--body);
}
.gs-usage-track {
  height: 10px;
  background: var(--hairline-soft);
  border-radius: 999px;
  overflow: hidden;
}
.gs-usage-fill {
  display: block;
  height: 100%;
  border-radius: 999px;
}
.gs-usage-val {
  font-family: var(--font-mono);
  font-size: 0.66rem;
  font-weight: 600;
  color: var(--ink);
  text-align: right;
}
</style>
