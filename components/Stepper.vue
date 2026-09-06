<script lang="ts">
export interface StepImage {
  src: string
  alt?: string
}

export interface Step {
  num: string
  title: string
  meta?: string
  /** Фото в теле карточки — одно или несколько (например, 2 сервера) */
  imgs?: StepImage[]
  /** Mono-подпись в теле карточки (команда, название инструмента) */
  chip?: string
  /** Крупная метрика в теле карточки */
  metric?: string
  unit?: string
  /** Векторная иллюстрация в теле карточки */
  art?: 'excited'
  /** Тёмная «featured»-карточка — единственный тёмный surface на слайде */
  dark?: boolean
}
</script>

<script setup lang="ts">
const props = defineProps<{
  steps: Step[]
}>()
</script>

<template>
  <div class="fls-row">
    <template v-for="(s, i) in props.steps" :key="s.num">
      <div class="fls-card" :class="{ 'fls-dark': s.dark }">
        <div class="fls-num">{{ s.num }}</div>
        <div class="fls-body" :class="{ 'fls-body-multi': (s.imgs?.length ?? 0) > 1 }">
          <template v-if="s.imgs?.length">
            <img
              v-for="(im, j) in s.imgs"
              :key="j"
              :src="im.src"
              :alt="im.alt ?? s.title"
              class="fls-img"
            />
          </template>
          <div v-else-if="s.metric" class="fls-metric">
            <span class="fls-metric-num">{{ s.metric }}</span>
            <span class="fls-metric-unit">{{ s.unit }}</span>
          </div>
          <div v-else-if="s.chip" class="fls-cmd">{{ s.chip }}</div>
          <svg
            v-else-if="s.art === 'excited'"
            class="fls-art"
            width="104"
            height="104"
            viewBox="0 0 120 120"
            fill="none"
            aria-hidden="true"
          >
            <!-- искры энтузиазма над головой -->
            <g stroke="currentColor" stroke-width="4" stroke-linecap="round">
              <path d="M60 8v12" />
              <path d="M24 20l9 9" />
              <path d="M96 20l-9 9" />
            </g>
            <!-- лицо -->
            <circle cx="60" cy="70" r="36" stroke="currentColor" stroke-width="4" />
            <!-- поднятые брови -->
            <path d="M41 55c4-5 10-5 14 0" stroke="currentColor" stroke-width="4" stroke-linecap="round" />
            <path d="M65 55c4-5 10-5 14 0" stroke="currentColor" stroke-width="4" stroke-linecap="round" />
            <!-- широко открытые глаза -->
            <circle cx="48" cy="66" r="5.5" fill="currentColor" />
            <circle cx="72" cy="66" r="5.5" fill="currentColor" />
            <!-- широкая открытая улыбка -->
            <path d="M47 78h26a13 13 0 0 1-26 0z" fill="currentColor" />
          </svg>
        </div>
        <div class="fls-title">{{ s.title }}</div>
        <div v-if="s.meta" class="fls-meta">{{ s.meta }}</div>
      </div>
      <div v-if="i < props.steps.length - 1" class="fls-arrow" aria-hidden="true">
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M7 4l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
    </template>
  </div>
</template>

<style scoped>
.fls-row {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  width: 100%;
}

/* Шаг: светлая карточка (surface-card), единая высота, номер сверху */
.fls-card {
  flex: 1;
  min-width: 0;
  min-height: 280px;
  display: flex;
  flex-direction: column;
  background: var(--surface-card);
  border: 1px solid var(--hairline);
  border-radius: 12px;
  padding: 0.85rem 0.8rem;
}

.fls-num {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--muted);
}

/* Среда карточки: фото / метрика / подпись — по центру, тянется */
.fls-body {
  flex: 1;
  min-height: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.fls-img {
  width: 100%;
  height: 108px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid var(--hairline);
}

/* Несколько фото в одной карточке (2 сервера) — ниже, чтобы влезть в 280px */
.fls-body-multi .fls-img {
  height: 72px;
}

.fls-cmd {
  font-family: var(--font-mono);
  font-size: 0.85rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  color: var(--ink);
  background: var(--canvas);
  border: 1px solid var(--hairline);
  border-radius: 8px;
  padding: 0.45rem 0.6rem;
  white-space: nowrap;
}

.fls-metric {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.2rem;
}
.fls-metric-num {
  font-size: 2.2rem;
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1;
  white-space: nowrap;
  color: var(--ink);
}
.fls-metric-unit {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--muted);
}

.fls-title {
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.01em;
  text-align: center;
  color: var(--ink);
}

.fls-meta {
  margin-top: 0.35rem;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.02em;
  text-align: center;
  color: var(--muted);
}

/* Иллюстрация: белый контур на тёмной featured-карточке */
.fls-dark .fls-art {
  color: var(--on-dark);
}

/* Стрелка между шагами — по вертикальному центру карточки */
.fls-arrow {
  flex: 0 0 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 280px;
  color: var(--muted-soft);
}

/* Тёмная featured-карточка — единственный тёмный surface, закрывает последовательность */
.fls-dark {
  background: var(--surface-dark);
  border-color: var(--surface-dark);
}
.fls-dark .fls-num {
  color: var(--on-dark-soft);
}
.fls-dark .fls-title {
  color: var(--on-dark);
}
.fls-dark .fls-meta {
  color: var(--on-dark-soft);
}
</style>
