<script setup lang="ts">
// VRAM-бюджет: 2×RTX 3090 = 48 GB; бюджет = 48 × 0.90 ≈ 43 GB.
// Шкала: 0–64 GB = 100% трека; FP16-бар (65 GB) превышает всю шкалу,
// линия 48 GB (75%) — край железа, пунктир 43 GB (67.5%) — бюджет.

interface Seg {
  gb: number
  cls: 'weights' | 'kv' | 'overhead' | 'free' | 'fp16'
  label?: string
}

interface BarRow {
  name: string
  sub: string
  verdict: string
  ok: boolean
  segs: Seg[]
}

const SCALE = 64
const BUDGET_PCT = (43.2 / SCALE) * 100
const VLLM_PCT = (24 / SCALE) * 100
const HW_PCT = (48 / SCALE) * 100

const rows: BarRow[] = [
  {
    name: 'FP16',
    sub: 'без квантизации',
    verdict: '✗ OOM',
    ok: false,
    segs: [{ gb: 65, cls: 'fp16', label: '65 GB' }],
  },
  {
    name: 'AWQ INT4',
    sub: 'W4A16',
    verdict: '',
    ok: true,
    segs: [
      { gb: 16, cls: 'weights', label: '16' },
      { gb: 4, cls: 'kv', label: '4' },
      { gb: 4, cls: 'overhead', label: '4' },
    ],
  },
]

const pct = (gb: number) => (gb / SCALE) * 100
const ticks = [0, 16, 32, 48, 64]
</script>

<template>
  <div class="vb">
    <div class="num-cap vb-formula text-center">
      VRAM = веса (квантизация) + KV-cache (контекст × concurrency) + overhead (~10–15%)
    </div>

    <div class="vb-plot">
      <div v-for="r in rows" :key="r.name" class="vb-row">
        <div class="vb-label">
          <div class="vb-name">{{ r.name }}</div>
          <div class="vb-sub">{{ r.sub }}</div>
          <div class="vb-verdict" :class="{ 'vb-verdict-bad': !r.ok }">{{ r.verdict }}</div>
        </div>
        <div class="vb-track">
          <div
            v-for="(s, i) in r.segs"
            :key="i"
            class="vb-seg"
            :class="`vb-seg-${s.cls}`"
            :style="{ width: pct(s.gb) + '%' }"
          >
            <span v-if="s.label" class="vb-seg-label">{{ s.label }}</span>
          </div>
        </div>
      </div>

      <div class="vb-lines" aria-hidden="true">
        <div class="vb-line vb-line-hw" :style="{ left: HW_PCT + '%' }">
          <span class="vb-line-label vb-line-label-hw">48 GB</span>
        </div>
        <div class="vb-line vb-line-budget" :style="{ left: VLLM_PCT + '%' }">
          <span class="vb-line-label vb-line-label-budget">≈ 24 GB</span>
        </div>
      </div>

      <div class="vb-ticksrow">
        <div></div>
        <div class="vb-ticks">
          <span
            v-for="t in ticks"
            :key="t"
            class="vb-tick"
            :class="{ 'vb-tick-end': t === 64 }"
            :style="t === 64 ? undefined : { left: pct(t) + '%' }"
          >
            {{ t === 64 ? '64 GB' : t }}
          </span>
        </div>
      </div>
    </div>


    <div class="vb-steps">
      <div class="vb-step">
        <div class="vb-step-head"><span class="vb-step-num">01</span>Объем памяти</div>
        <div class="vb-step-text">VRAM кластера × 0.90 − overhead</div>
        <div class="vb-step-val">48 GB → ≈ 43 GB</div>
      </div>
      <div class="vb-arrow" aria-hidden="true">
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
          <path d="M7 4l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
      <div class="vb-step">
        <div class="vb-step-head"><span class="vb-step-num">02</span>Модель</div>
        <div class="vb-step-text">максимальная: веса + KV ≤ бюджет</div>
        <div class="vb-step-val">→ 27B · Qwen3.8</div>
      </div>
      <div class="vb-arrow" aria-hidden="true">
        <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
          <path d="M7 4l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
      <div class="vb-step">
        <div class="vb-step-head"><span class="vb-step-num">03</span>Квантизация</div>
        <div class="vb-step-text">по поколению GPU</div>
        <div class="vb-step-val">Ampere → AWQ · Hopper → FP8 · CPU → GGUF</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.vb {
  width: 100%;
  margin-top: 0.4rem;
}

.vb-formula {
  margin-top: 0.2rem;
  margin-bottom: 1.1rem;
}

/* ── Бары ───────────────────────────────────────────────────────────── */
.vb-plot {
  position: relative;
  padding-top: 1.15rem;
}

.vb-row {
  display: grid;
  grid-template-columns: 168px 1fr;
  gap: 14px;
  align-items: center;
}

.vb-row + .vb-row {
  margin-top: 0.8rem;
}

.vb-label {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
  padding-left: 0.2rem;
}

.vb-name {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.vb-sub {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  color: var(--muted);
}

.vb-verdict {
  margin-top: 0.2rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--success);
}

.vb-verdict-bad {
  color: var(--error);
}

.vb-track {
  position: relative;
  display: flex;
  height: 44px;
  background: var(--hairline-soft);
  border: 1px solid var(--hairline);
  border-radius: 8px;
  overflow: hidden;
}

.vb-seg {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  min-width: 0;
  flex-shrink: 0;
}

.vb-seg:first-child {
  border-radius: 7px 0 0 7px;
}

.vb-seg-weights {
  background: var(--accent);
}

.vb-seg-kv {
  background: var(--badge-violet);
}

.vb-seg-overhead {
  background: var(--surface-strong);
}

.vb-seg-free {
  background: var(--surface-soft);
}

.vb-seg-fp16 {
  background: var(--error);
}

.vb-seg-label {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  color: #ffffff;
}

.vb-seg-overhead .vb-seg-label {
  color: var(--body);
}

.vb-seg-free .vb-seg-label {
  color: var(--muted-soft);
}

/* Вертикальные линии: край железа (48 GB) и бюджет (≈43 GB) */
.vb-lines {
  position: absolute;
  left: calc(168px + 14px);
  right: 0;
  top: 0;
  bottom: 1.35rem;
  pointer-events: none;
  z-index: 2;
}

.vb-line {
  position: absolute;
  top: 0;
  bottom: 0;
}

.vb-line-hw {
  border-left: 2px solid var(--ink);
}

.vb-line-budget {
  border-left: 1.5px dashed var(--accent);
}

.vb-line-label {
  position: absolute;
  top: -1.1rem;
  white-space: nowrap;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.03em;
}

.vb-line-label-hw {
  left: 0.45rem;
  color: var(--ink);
}

.vb-line-label-budget {
  right: 0.45rem;
  color: var(--accent);
}

/* Тicks */
.vb-ticksrow {
  display: grid;
  grid-template-columns: 168px 1fr;
  gap: 14px;
  margin-top: 0.35rem;
}

.vb-ticks {
  position: relative;
  height: 1rem;
}

.vb-tick {
  position: absolute;
  top: 0;
  transform: translateX(-50%);
  white-space: nowrap;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  color: var(--muted-soft);
}

.vb-tick:first-child {
  transform: none;
}

.vb-tick-end {
  left: auto;
  right: 0;
  transform: none;
}

/* Легенда */
.vb-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.1rem;
  margin-top: 0.9rem;
}

.vb-legend-lines {
  margin-top: 0.3rem;
}

.vb-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  letter-spacing: 0.02em;
  color: var(--muted);
}

.vb-sw {
  width: 10px;
  height: 10px;
  border-radius: 3px;
  flex-shrink: 0;
}

.vb-sw-soft {
  background: var(--surface-soft);
  border: 1px solid var(--hairline);
}

.vb-sw-dash {
  width: 16px;
  height: 0;
  border-top: 1.5px dashed var(--accent);
  border-radius: 0;
}

.vb-sw-hw {
  width: 16px;
  height: 0;
  border-top: 2px solid var(--ink);
  border-radius: 0;
}

/* Три шага */
.vb-steps {
  display: flex;
  align-items: stretch;
  gap: 0.55rem;
  margin-top: 1.1rem;
}

.vb-step {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  padding: 0.65rem 0.9rem;
}

.vb-step-head {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.vb-step-num {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--muted);
}

.vb-step-text {
  font-size: 0.78rem;
  line-height: 1.35;
  color: var(--body);
}

.vb-step-val {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  color: var(--ink);
  white-space: nowrap;
}

.vb-arrow {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  color: var(--muted-soft);
}
</style>
