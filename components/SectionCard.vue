<script setup lang="ts">
defineProps({
  kicker: { type: String, default: '' },
  title: { type: String, required: true },
  // tone: canvas | emerald | violet | orange | pink
  tone: { type: String, default: 'canvas' },
})
</script>

<template>
  <div class="section-card">
    <div v-if="kicker" class="sc-kicker" :class="`tone-${tone}`">{{ kicker }}</div>
    <h1 class="sc-title">{{ title }}</h1>
    <slot />
  </div>
</template>

<style scoped>
/* Секция-разделитель: badge-pill (DESIGN.md) + display-lg 48px/600 */
.section-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1.25rem;
  text-align: center;
}
.sc-kicker {
  display: inline-flex;
  align-items: center;
  padding: 4px 14px;
  border-radius: 9999px;
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: var(--ink);
  background: var(--surface-card);
}
.sc-kicker.tone-emerald { background: var(--badge-emerald); }
.sc-kicker.tone-violet { background: var(--badge-violet); }
.sc-kicker.tone-orange { background: var(--badge-orange); }
.sc-kicker.tone-pink { background: var(--badge-pink); }
.sc-kicker.tone-canvas { background: var(--canvas); }
.sc-title {
  margin: 0;
  font-size: 3rem;
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.031em;
  color: var(--ink);
}
</style>
