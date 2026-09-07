<script setup lang="ts">
import { PARAMS, PARAM_ORDER, STAGES } from './stage-data'
import type { ParamId, Status } from './stage-data'

const props = withDefaults(
  defineProps<{
    stage?: 's1' | 's2' | 's3'
  }>(),
  {
    stage: 's1',
  },
)

const stageData = () => STAGES[props.stage]

const rowFor = (id: ParamId) => stageData().problems.find((p) => p.param === id)

const rowClass = (id: ParamId) => {
  const row = rowFor(id)
  return row ? `sp-row--${row.status}` : ''
}

const STATUS_SYMBOL: Record<Status, string> = { ok: '✓', warn: '~', bad: '✗' }
const STATUS_COLOR: Record<Status, string> = {
  ok: 'var(--success)',
  warn: 'var(--warning)',
  bad: 'var(--error)',
}
</script>

<template>
  <div class="sp-wrap">
    <table class="sp-table">
      <thead>
        <tr>
          <th>Параметр</th>
          <th>Ожидание</th>
          <th>Реальность</th>
          <th class="sp-status-head">Статус</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="id in PARAM_ORDER" :key="id" :class="rowClass(id)">
          <td>
            <span class="sp-param">
              <span class="sp-dot" :style="{ background: PARAMS[id].color }" aria-hidden="true"></span>
              {{ PARAMS[id].label }}
            </span>
          </td>
          <td class="sp-expected">{{ PARAMS[id].expected }}</td>
          <td class="sp-actual">{{ rowFor(id)?.actual ?? '—' }}</td>
          <td class="sp-status">
            <span v-if="rowFor(id)" class="sp-status-symbol" :style="{ color: STATUS_COLOR[rowFor(id)!.status] }">
              {{ STATUS_SYMBOL[rowFor(id)!.status] }}
            </span>
          </td>
        </tr>
      </tbody>
    </table>

    <div class="num-cap sp-cap">Особенности</div>

    <div class="sp-features">
      <div v-for="(f, i) in stageData().features" :key="i" class="sp-feature">
        <div class="sp-feature-top">
          <span class="sp-feature-title">{{ f.title }}</span>
          <span v-if="f.value" class="sp-feature-value">{{ f.value }}</span>
        </div>
        <div class="sp-feature-text">{{ f.text }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.sp-wrap {
  width: 100%;
}

/* Таблица: как глобальные table в styles/index.css, но компактнее (6 строк × ~0.9rem) */
.sp-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}

.sp-table th {
  text-align: left;
  font-weight: 500;
  color: var(--ink);
  padding: 0.4rem 0.7rem;
  border-bottom: 2px solid var(--ink);
}

.sp-table td {
  padding: 0.42rem 0.7rem;
  border-bottom: 1px solid var(--hairline);
  color: var(--body);
}

.sp-table tr:last-child td {
  border-bottom: none;
}

.sp-row--ok {
  background: color-mix(in srgb, var(--success) 6%, transparent);
}

.sp-row--warn {
  background: color-mix(in srgb, var(--warning) 8%, transparent);
}

.sp-row--bad {
  background: color-mix(in srgb, var(--error) 7%, transparent);
}

.sp-status-head {
  text-align: center;
}

.sp-param {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  color: var(--muted);
}

.sp-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.sp-expected {
  color: var(--muted);
}

.sp-actual {
  font-weight: 500;
  color: var(--ink);
}

.sp-status {
  text-align: center;
}

.sp-status-symbol {
  font-size: 1rem;
  font-weight: 600;
  line-height: 1;
}

.sp-cap {
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.sp-features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.7rem;
}

.sp-feature {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  padding: 0.6rem 0.8rem;
}

.sp-feature-top {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.5rem;
}

.sp-feature-title {
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.sp-feature-value {
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--warning);
  white-space: nowrap;
}

.sp-feature-text {
  font-size: 0.78rem;
  line-height: 1.4;
  color: var(--body);
}
</style>
