<script setup lang="ts">
defineProps({
  kicker: { type: String, default: '' },
  title: { type: String, required: true },
  art: { type: String, default: '' },
})
</script>

<template>
  <div class="section-card">
    <div v-if="kicker" class="sc-kicker">{{ kicker }}</div>
    <h1 class="sc-title">{{ title }}</h1>
    <img v-if="art" :src="art" class="sc-art" />
    <slot />
  </div>
</template>

<style scoped>
.section-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  text-align: center;
  height: 100%;
}
.sc-kicker {
  font-family: 'Geist Mono', monospace;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.16em;
  color: var(--sapphire);
}
.sc-title {
  font-size: 3rem;
  line-height: 1.1;
  color: var(--ink);
}
.sc-art {
  width: 200px;
  margin-top: 1.5rem;
}
</style>
