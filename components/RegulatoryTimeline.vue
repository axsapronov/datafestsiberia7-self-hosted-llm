<script lang="ts">
export interface EventItem {
  year: number
  label: string
  country: string
  tags: string[]
  /** Поднять подпись на второй ярус (где соседние подписи перекрываются) */
  far?: boolean
}

export interface Phase {
  color: string
  events: EventItem[]
}

export const defaultPhases: Phase[] = [
  {
    color: 'var(--badge-emerald)',
    events: [
      { year: 2000, label: 'COPPA', country: 'us', tags: ['#дети-до-13', '#родительское-согласие'] },
      { year: 2006, label: '152-ФЗ', country: 'ru', tags: ['#согласие-на-обработку', '#право-удалить-данные'] },
    ],
  },
  {
    color: 'var(--badge-violet)',
    events: [
      { year: 2014, label: '242-ФЗ', country: 'ru', tags: ['#локализация-пдн', '#российские-серверы'] },
      { year: 2018, label: 'GDPR', country: 'eu', tags: ['#штрафы-до-4%-выручки', '#72ч-на-утечку'] },
    ],
  },
  {
    color: 'var(--accent)',
    events: [
      { year: 2020, label: 'CCPA', country: 'us', tags: ['#отказ-от-рассылок', '#право-удалить'] },
      { year: 2021, label: 'PIPL', country: 'cn', tags: ['#штрафы-до-5%-выручки', '#данные-остаются-в-китае'] },
      { year: 2023, label: 'DPDP', country: 'in', tags: ['#первый-закон-индии', '#штрафы-до-30-млн-долл'], far: true },
    ],
  },
  {
    color: 'var(--badge-pink)',
    events: [
      { year: 2024, label: 'EU AI Act', country: 'eu', tags: ['#первый-закон-об-ai', '#ai-по-уровням-риска'] },
      { year: 2025, label: '420-ФЗ', country: 'ru', tags: ['#штрафы-до-500-млн', '#уголовка-за-утечки'] },
      { year: 2026, label: 'AI Act full', country: 'eu', tags: ['#high-risk-в-силу', '#маркировка-ai-контента'], far: true },
    ],
  },
]
</script>

<script setup lang="ts">
const props = withDefaults(
  defineProps<{
    phases?: Phase[]
  }>(),
  {
    phases: () => defaultPhases,
  },
)

const bandWidth = 100 / props.phases.length

const items = props.phases.flatMap((p, pi) => {
  const bandStart = pi * bandWidth
  const n = p.events.length
  return p.events.map((e, i) => {
    const x = bandStart + ((i + 1) / (n + 1)) * bandWidth
    return {
      ...e,
      x,
      side: i % 2 === 0 ? 'up' : 'down',
      tier: e.far ? 'far' : 'near',
      color: p.color,
    }
  })
})
</script>

<template>
  <div class="rt">
    <div class="rt-track">
      <div
        v-for="(p, pi) in phases"
        :key="pi"
        class="rt-band"
        :style="{ left: pi * bandWidth + '%', width: bandWidth + '%', background: p.color }"
      />
      <div class="rt-line" />

      <div
        v-for="e in items"
        :key="e.label"
        class="rt-event"
        :class="[e.side, e.tier]"
        :style="{ left: e.x + '%', '--ec': e.color }"
      >
        <span class="rt-stem" />
        <span class="rt-dot" />
        <span class="rt-year">{{ e.year }}</span>
        <div class="rt-labelbox">
          <div class="rt-title">
            <FlagIcon :code="e.country" />
            <span class="rt-label">{{ e.label }}</span>
          </div>
          <div v-if="e.tags.length" class="rt-tags">
            <span v-for="t in e.tags" :key="t" class="rt-tag">{{ t }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.rt {
  width: 100%;
}

/* Трек: базовая линия по центру, цветные полосы эр */
.rt-track {
  position: relative;
  height: 132px;
}
.rt-line {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 2px;
  transform: translateY(-50%);
  background: var(--hairline);
}
.rt-band {
  position: absolute;
  top: 50%;
  height: 6px;
  transform: translateY(-50%);
  border-radius: 3px;
  opacity: 0.5;
}

/* Событие: точка на линии, год у точки, подпись сверху/снизу
   в два яруса (near/far), чтобы соседние подписи не перекрывались */
.rt-event {
  position: absolute;
  top: 50%;
  height: 0;
  width: 0;
}
.rt-dot {
  position: absolute;
  left: 0;
  top: 0;
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--ec);
  border: 2px solid var(--canvas);
  transform: translate(-50%, -50%);
}
.rt-year {
  position: absolute;
  left: 0;
  transform: translateX(-50%);
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: var(--muted);
  white-space: nowrap;
}
/* Стебель: полоска от точки до подписи, цвет события */
.rt-stem {
  position: absolute;
  left: -1px;
  width: 2px;
  border-radius: 1px;
  background: var(--ec);
  opacity: 0.55;
}
.rt-event.up.near .rt-stem {
  top: -30px;
  height: 30px;
}
.rt-event.up.far .rt-stem {
  top: -96px;
  height: 96px;
}
.rt-event.down.near .rt-stem {
  top: 0;
  height: 30px;
}
.rt-event.down.far .rt-stem {
  top: 0;
  height: 96px;
}

.rt-event.up .rt-year {
  top: 10px;
}
.rt-event.down .rt-year {
  bottom: 10px;
}

.rt-labelbox {
  position: absolute;
  left: 0;
  transform: translateX(-50%);
  width: max-content;
  max-width: 180px;
  display: flex;
  flex-direction: column;
  gap: 3px;
  text-align: center;
}
.rt-event.up.near .rt-labelbox {
  bottom: 30px;
}
.rt-event.up.far .rt-labelbox {
  bottom: 96px;
}
.rt-event.down.near .rt-labelbox {
  top: 30px;
}
.rt-event.down.far .rt-labelbox {
  top: 96px;
}
.rt-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}
.rt-label {
  font-size: 0.92rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--ink);
  white-space: nowrap;
}
.rt-tags {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 3px;
}
.rt-tag {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.01em;
  color: var(--muted);
  background: var(--surface-soft);
  border-radius: 9999px;
  padding: 1px 7px;
  white-space: nowrap;
}
</style>
