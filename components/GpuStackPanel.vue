<script setup lang="ts">
// GPUStack — панель управления self-hosted.
// 2×2 сетка из 4 карточек 16:9: каждая — скриншот реального UI в формате 16:9
// (public/img/gpustack/gpustack-*.png) + подпись-возможность
// (Модели / Движки / API / Статистика) поверх изображения.
// Карточки 16:9 (стандарт для UI-скриншотов) — картинки того же формата
// вписываются без полей (object-fit: contain).

interface Capability {
  dot: string
  label: string
  desc: string
  img: string
  alt: string
}

// 4 возможности панели — цвета совпадают с палитрой параметров дека
// (api → #f59e0b, manage → #0ea5e9 из stage-data.ts).
const CAPS: Capability[] = [
  {
    dot: '#10b981',
    label: 'Модели',
    desc: 'Hugging Face → replicas N → auto-restart',
    img: '/img/gpustack/gpustack-models.png',
    alt: 'GPUStack Catalog: сетка моделей (NVIDIA Nemotron, Qwen3.5-0.8B, Qwen3.5-2B и другие) — стрелка указывает на выбранную модель Qwen3.5-0.8B',
  },
  {
    dot: '#8b5cf6',
    label: 'Движки',
    desc: 'подключаемые inference-рантаймы',
    img: '/img/gpustack/gpustack-engines.png',
    alt: 'GPUStack Inference Backends: vLLM, SGLang, MindIE, VoxBox, llama.cpp, PaddleX, Text-Embeddings-Inference',
  },
  {
    dot: '#f59e0b',
    label: 'API',
    desc: 'OpenAI-совместимый, доступ по моделям',
    img: '/img/gpustack/gpustack-api.png',
    alt: 'GPUStack Chat: диалог с моделью и панель параметров (Temperature, Max Tokens, Top P)',
  },
  {
    dot: '#0ea5e9',
    label: 'Статистика',
    desc: 'токены и запросы по пользователям и ключам',
    img: '/img/gpustack/gpustack-stats.png',
    alt: 'GPUStack Chat: Token Usage 62, Output 343.28 Tokens/s — статистика использования',
  },
]
</script>

<template>
  <div class="gs">
    <div v-for="cap in CAPS" :key="cap.label" class="gs-card">
      <img :src="cap.img" :alt="cap.alt" class="gs-img" />
      <div class="gs-overlay">
        <div class="gs-card-head">
          <span class="gs-dot" :style="{ background: cap.dot }" aria-hidden="true"></span>
          <span class="gs-label">{{ cap.label }}</span>
        </div>
        <div class="gs-desc">{{ cap.desc }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.gs {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, auto);
  gap: 0.55rem;
  /* Заполняем ширину слайда (подпись снизу убрана) — карточки 16:9 крупнее и читабельнее */
  width: 92%;
  margin: 0.4rem auto 0;
}

.gs-card {
  position: relative;
  /* 16:9 — стандарт для UI-скриншотов: картинки того же формата вписываются без полей */
  aspect-ratio: 16 / 9;
  border: 1px solid var(--hairline);
  border-radius: 12px;
  overflow: hidden;
  background: #fff;
}

.gs-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  /* contain — показываем картинку целиком, браузер ничего не обрезает */
  object-fit: contain;
  object-position: center;
  display: block;
}

/* Подпись поверх изображения: градиент для читаемости на светлом UI */
.gs-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  padding: 0.55rem 0.85rem 1.6rem;
  background: linear-gradient(
    to bottom,
    rgba(255, 255, 255, 0.97) 0%,
    rgba(255, 255, 255, 0.85) 55%,
    rgba(255, 255, 255, 0) 100%
  );
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
  font-size: 1.05rem;
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--ink);
}

.gs-desc {
  font-size: 0.78rem;
  line-height: 1.3;
  color: var(--body);
}
</style>
