---
theme: default
title: 1 млрд токенов в сутки на потребительских видеокартах
layout: cover
info: |
  ## Data Fest Siberia 7
  Доклад для Open Data Science
  Новосибирск, 10 октября 2026
hideInToc: true
colorSchema: light
mdc: true
drawings:
  persist: false
transition: slide-left
comark: true
duration: 30min
fonts:
  sans: Radio Canada Big
  serif: Source Serif 4
  mono: Geist Mono
---

<div class="title-hero">
# 1 млрд токенов в сутки на потребительских видеокартах
</div>

<div class="subtitle">Как запускать и обслуживать LLM-модели локально</div>

<CoverBrand />

<div class="cover-meta">
  <div class="cover-author">Александр Сапронов</div>
  <div class="cover-contacts"><a href="mailto:a@sapronov.me">a@sapronov.me</a> · <a href="https://t.me/axsapronov">t.me/axsapronov</a></div>
  <div class="cover-date">Data Fest Siberia 7 · Новосибирск · 10 октября 2026</div>
</div>

<style>
.title-hero h1 { font-size: 4.6rem; line-height: 1.02; color: var(--ink); }
.subtitle { margin-top: 1.4rem; font-size: 1.4rem; color: var(--ink-dim); }
.cover-brand { position: absolute; top: 2rem; right: 2.5rem; display: flex; gap: 1rem; align-items: center; }
.brand-logo { height: 44px; width: auto; }
.cover-meta { position: absolute; bottom: 2.5rem; left: 2.5rem; display: flex; flex-direction: column; gap: 0.3rem; }
.cover-author { font-size: 1.3rem; font-weight: 600; color: var(--ink); }
.cover-contacts { font-family: 'Geist Mono', monospace; font-size: 0.95rem; color: var(--ink-dim); }
.cover-contacts a { color: var(--ink-dim); text-decoration: none; }
.cover-contacts a:hover { color: var(--sapphire); }
.cover-date { font-family: 'Geist Mono', monospace; font-size: 0.95rem; color: var(--ink-dim); }
</style>

<!--
Приветствие, представление, 1-2 минуты.
-->

---
hideInToc: true
---

# План доклада

<Toc minDepth="1" maxDepth="1" />

---
layout: center
title: 1. Почему self-hosted LLM
---

<SectionCard kicker="Раздел 1" title="Почему self-hosted LLM" />

---
hideInToc: true
---

# Почему self-hosted LLM

<v-clicks>
- Контроль над данными и приватность
- Стоимость: свой GPU против API-биллинг
- Офлайн-режим и кастомизация
</v-clicks>

<!--
Мотивация: приватность данных, стоимость API, независимость от провайдеров.
-->

---
layout: center
title: 2. Стек: Ollama, vLLM, LM Studio
---

<SectionCard kicker="Раздел 2" title="Стек: Ollama, vLLM, LM Studio" />

---
hideInToc: true
---

# Стек: Ollama, vLLM, LM Studio

<v-clicks>
- **Ollama** — простой запуск и управление моделями
- **vLLM** — высокопроизводительный инференс (PagedAttention)
- **LM Studio** — GUI для подбора и запуска моделей
</v-clicks>

<!--
Краткий обзор инструментов, сравнение в таблице на следующем слайде.
-->

---
hideInToc: true
---

# Сравнение: Ollama vs vLLM vs LM Studio

| | **Ollama** | **vLLM** | **LM Studio** |
|---|---|---|---|
| Задача | Простой локальный запуск моделей | Высокопроизводительный сервинг | GUI для подбора и запуска |
| Порог входа | CLI, одна команда | CLI + конфигурация | GUI, без кода |
| Производительность | Хорошая | Высокая (PagedAttention, continuous batching) | Хорошая |
| API | OpenAI-совместимое | OpenAI-совместимое | OpenAI-совместимое (локально) |
| Кому подходит | Старт, прототипы | Production, большие нагрузки | Не-инженеры, каталог моделей |

---
layout: center
title: 3. Практика: от скачивания модели до API
---

<SectionCard kicker="Раздел 3" title="Практика: от скачивания модели до API" />

---
hideInToc: true
---

# Практика: от скачивания модели до API

<v-clicks>
- Выбор модели (размер, квантизация, контекст)
- Запуск и настройки
- Интеграция с приложениями (OpenAI-совместимое API)
</v-clicks>

<!--
Демо: запуск модели, запрос через API, замер скорости.
-->

---
layout: two-cols-header
hideInToc: true
---

# От скачивания модели до API

::left::

<div class="code-cap">Запуск</div>

```bash
# Ollama
ollama pull llama3.2
ollama run llama3.2

# vLLM
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

::right::

<div class="code-cap">Запрос через API</div>

<<< @/snippets/openai-client.py

<style>
.code-cap {
  font-family: 'Geist Mono', monospace; font-size: 0.8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.1em; color: var(--sapphire);
}
</style>

---
layout: center
title: 4. Производительность и стоимость
---

<SectionCard kicker="Раздел 4" title="Производительность и стоимость" />

---
hideInToc: true
---

# Производительность и стоимость

<v-clicks>
- Требования к GPU (VRAM)
- Токены/секунда, latency, batch
- Свой сервер vs API: экономика
</v-clicks>

<!--
Числа: VRAM для 7B/13B/70B при разных квантизациях, стоимость владения.
-->

---
hideInToc: true
---

# Числа: VRAM, скорость, стоимость

<div class="num-cap">VRAM по моделям и квантизациям</div>

| Модель | FP16 | Q8_0 | Q4_K_M |
|---|---|---|---|
| 7B | ~14 GB | ~8 GB | ~4 GB |
| 13B | ~26 GB | ~14 GB | ~8 GB |
| 70B | ~140 GB | ~72 GB | ~40 GB |

<div class="num-cap">Скорость и стоимость владения</div>

| Конфигурация | Токены/с | Стоимость владения |
|---|---|---|
| 1× RTX 4090 (24 GB) | ~60–80 (7B Q4) | ~$1.6k единовременно |
| 1× A100 (80 GB) | ~40–60 (70B Q4) | ~$10k+ единовременно |
| API (уровня GPT-4o) | зависит от нагрузки | ~$5–15 / 1M токенов |

<style>
.num-cap {
  margin-top: 1.4rem;
  font-family: 'Geist Mono', monospace; font-size: 0.8rem; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.1em; color: var(--sapphire);
}
.num-cap:first-of-type { margin-top: 0.4rem; }
</style>

---
layout: center
title: 5. Заключение
---

<SectionCard kicker="Раздел 5" title="Заключение" />

---
hideInToc: true
---

# Заключение

<v-clicks>
- Self-hosted LLM — реалистичный вариант для production
- Начните с Ollama, масштабируйтесь на vLLM
</v-clicks>

---
layout: center
hideInToc: true
---

<div class="thanks">
  <h1 class="thanks-title">Спасибо!</h1>
  <div class="thanks-sub">Вопросы?</div>

  <div class="thanks-contact">
    <div class="thanks-name">Александр Сапронов</div>
    <div class="thanks-links"><a href="mailto:a@sapronov.me">a@sapronov.me</a> · <a href="https://t.me/axsapronov">t.me/axsapronov</a></div>
  </div>

  <QrCode url="https://github.com/axsapronov/datafestsiberia7-self-hosted-llm" :size="124" caption="Ссылка на слайды" />
</div>

<style>
.thanks { display: flex; flex-direction: column; align-items: center; gap: 1.1rem; text-align: center; }
.thanks-title { font-size: 4rem; line-height: 1.05; }
.thanks-sub { font-family: 'Source Serif 4', Georgia, serif; font-size: 2rem; color: var(--sapphire); }
.thanks-contact { display: flex; flex-direction: column; gap: 0.3rem; margin-top: 0.4rem; }
.thanks-name { font-size: 1.3rem; font-weight: 600; color: var(--ink); }
.thanks-links { font-family: 'Geist Mono', monospace; font-size: 1rem; color: var(--ink-dim); }
.thanks-links a { color: var(--ink-dim); text-decoration: none; }
.thanks-links a:hover { color: var(--sapphire); }
</style>

<!--
Финал: Q&A, ссылки, контакты.
-->
