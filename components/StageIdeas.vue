<script setup lang="ts">
import { PARAMS, STAGES } from './stage-data'
import type { ParamId } from './stage-data'

const props = withDefaults(
  defineProps<{
    stage?: 's1' | 's2' | 's3'
  }>(),
  {
    stage: 's1',
  },
)

const stageData = () => STAGES[props.stage]

const paramLabel = (id: ParamId) => PARAMS[id].label
const paramColor = (id: ParamId) => PARAMS[id].color
</script>

<template>
  <div class="si-grid">
    <div v-for="idea in stageData().ideas" :key="idea.num" class="si-card">
      <div class="si-top">
        <span class="si-num">{{ idea.num }}</span>
      </div>
      <div class="si-title">{{ idea.title }}</div>
      <div class="si-text">{{ idea.text }}</div>
      <div v-if="idea.params?.length || idea.feature" class="si-chips">
        <span v-for="p in idea.params" :key="p" class="si-chip">
          <span class="si-chip-dot" :style="{ background: paramColor(p) }" aria-hidden="true"></span>
          {{ paramLabel(p) }}
        </span>
        <span v-if="idea.feature" class="si-chip">
          <span class="si-chip-dot si-chip-dot-muted" aria-hidden="true"></span>
          {{ idea.feature }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.si-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.7rem;
  width: 100%;
}

.si-card {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  padding: 0.75rem 1.1rem;
}

.si-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.si-num {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--muted);
}

.si-title {
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1.25;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.si-text {
  font-size: 0.82rem;
  line-height: 1.4;
  color: var(--body);
}

.si-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 0.7rem;
  margin-top: 0.15rem;
}

.si-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
}

.si-chip-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.si-chip-dot-muted {
  background: var(--muted);
}
</style>
