---
theme: default
title: Self-hosted LLM
layout: cover
info: |
  ## Data Fest Siberia 7
  Доклад для Open Data Science
  Новосибирск, 10 октября 2026
background: https://cover.sli.dev
drawings:
  persist: false
transition: slide-left
comark: true
duration: 35min
---

# Self-hosted LLM

Как запускать и обслуживать LLM-модели локально

<Carbon:Presentation class="text-4xl" />

author:

<PoweredBySlidev />

<!--
Приветствие, представление, 1-2 минуты.
-->

---

# План доклада

<Toc minDepth="1" maxDepth="1" />

---
layout: section
---

# 1. Почему self-hosted LLM

- Контроль над данными и приватность
- Стоимость: свой GPU против API-биллинг
- Офлайн-режим и кастомизация

<!--
Мотивация: приватность данных, стоимость API, независимость от провайдеров.
-->

---
layout: section
---

# 2. Стек: Ollama, vLLM, LM Studio

- **Ollama** — простой запуск и управление моделями
- **vLLM** — высокопроизводительный инференс (PagedAttention)
- **LM Studio** — GUI для подбора и запуска моделей

<!--
Краткий обзор инструментов, сравнение в таблице на следующем слайде.
-->

---
layout: section
---

# 3. Практика: от скачивания модели до API

- Выбор модели (размер, квантизация, контекст)
- Запуск и настройки
- Интеграция с приложениями (OpenAI-совместимое API)

<!--
Демо: запуск модели, запрос через API, замер скорости.
-->

---
layout: section
---

# 4. Производительность и стоимость

- Требования к GPU (VRAM)
- Токены/секунда, latency, batch
- Свой сервер vs API: экономика

<!--
Числа: VRAM для 7B/13B/70B при разных квантизациях, стоимость владения.
-->

---
layout: section
---

# 5. Заключение

- Self-hosted LLM — реалистичный вариант для production
- Начните с Ollama, масштабируйтесь на vLLM
- Спасибо! Вопросы?

<!--
Финал: Q&A, ссылки, контакты.
-->
