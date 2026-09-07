<script setup lang="ts">
import { computed } from 'vue'

// Ссылка на слайде: вертикальная таб-ссылка на правом крае, по центру
// по вертикали. Живёт в 3.5rem-поле слайда и не перекрывает контент.
// label — короткая подпись (по умолчанию — домен ссылки),
// dark — для тёмных слайдов (layout center-dark).
const props = withDefaults(
  defineProps<{
    href: string
    label?: string
    dark?: boolean
  }>(),
  {
    label: '',
    dark: false,
  },
)

const text = computed(() => {
  if (props.label) return props.label
  try {
    return new URL(props.href).hostname.replace(/^www\./, '')
  } catch {
    return props.href
  }
})
</script>

<template>
  <a
    class="slide-link"
    :class="{ 'slide-link-dark': dark }"
    :href="href"
    target="_blank"
    rel="noopener"
    :title="href"
  >
    <svg
      class="slide-link-icon"
      width="13"
      height="13"
      viewBox="0 0 24 24"
      fill="none"
      aria-hidden="true"
    >
      <path
        d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
      <path
        d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      />
    </svg>
    <span class="slide-link-label">{{ text }}</span>
  </a>
</template>

<style scoped>
/* Вертикальная таб на правом крае: right 0.55rem — в поле слайда
   (контент заканчивается на right 3.5rem), пересечений с контентом нет. */
.slide-link {
  position: absolute;
  top: 50%;
  right: 0.55rem;
  transform: translateY(-50%);
  z-index: 20;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.45rem;
  padding: 0.7rem 0.5rem;
  background: var(--canvas);
  border: 1px solid var(--hairline);
  border-radius: 999px;
  box-shadow: 0 1px 4px rgba(17, 17, 17, 0.07);
  color: var(--muted);
  text-decoration: none;
  cursor: pointer;
  transition: color 0.15s ease, border-color 0.15s ease;
}

.slide-link:hover {
  border-color: var(--accent);
  color: var(--ink);
}

/* Иконка-цепочка поворотом вдоль направления вертикального текста */
.slide-link-icon {
  flex-shrink: 0;
  transform: rotate(90deg);
}

.slide-link-label {
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  line-height: 1;
  color: inherit;
}

/* Тёмная версия для тёмных слайдов (center-dark) */
.slide-link-dark {
  background: var(--surface-dark-elevated);
  border-color: rgba(255, 255, 255, 0.14);
  color: var(--on-dark-soft);
  box-shadow: none;
}

.slide-link-dark:hover {
  border-color: var(--accent);
  color: var(--on-dark);
}
</style>
