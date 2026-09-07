---
theme: default
title: 1 млрд токенов в сутки на потребительских видеокартах | Сапронов Александр
layout: cover
info: |
  ## Data Fest Siberia 7
  Доклад для Open Data Science
  Новосибирск, 10 октября 2026
hideInToc: true
colorSchema: light
drawings:
  persist: false
transition: slide-left
duration: 30min
fonts:
  sans: Inter
  serif: Inter
  mono: JetBrains Mono
  weights: '400,500,600'
---

<div class="title">

# 1 млрд токенов <span class="title-sub">в сутки</span><br>на потребительских видеокартах

</div>

<CoverBrand />

<div class="cover-meta">
  <div class="cover-author">Александр Сапронов</div>
  <div class="cover-contacts"><a href="https://t.me/axsapronov">t.me/axsapronov</a></div>
  <div class="cover-date">Data Fest Siberia 7 · Новосибирск · 10 октября 2026</div>
</div>

<div class="cover-proof">
  <img class="cover-proof-chart" src="/img/tokens-chart.svg" alt="Total tokens per day — пик 2026-09-01, 1 043 495 767 токенов">
</div>

<!--
Приветствие, представление, 1-2 минуты.
-->

---
layout: two-cols
hideInToc: true
---

# План доклада

::left::

<Toc minDepth="1" maxDepth="1" />

::right::

<div class="speaker-card">
  <img class="speaker-photo" src="/img/headshot.png" alt="Александр Сапронов">
  <div class="speaker-name">Александр Сапронов</div>
  <div class="speaker-role">IT Manager (CTO)</div>
  <div class="speaker-bio">Решаю бизнес задачи в IT. <br>МТС, Avito, Welltory</div>
  <div class="speaker-contacts"><a href="https://t.me/axsapronov">t.me/axsapronov</a> · <a href="mailto:a@sapronov.me">a@sapronov.me</a></div>
</div>

---
hideInToc: false
title: Зачем собирать свою ИИ-инфраструктуру?
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# ИИ в 2026 — удобная и дорогая технология

<img class="data-chart" src="/img/ai-spend-milestones.svg" alt="AI Spend per Employee vs Model Releases and Technology Milestones, Ramp AI Index Top 1% 2023–2026: flat 2023–2024 (~$160/employee), 4× growth mid-2025 ($2,470), explosion to ~$9,000 by Sep 2026">

<!--
ИИ - это дорогая технология, которая стремится снизить себестоимость на масштабе.
Идея «удобная и дорогая технология» — на графике Ramp Top-1% ($/сотрудник/мес). Три фазы:
1) 2023 – early 2025 — FLAT, ~$160: Chat + RAG, удобно, но расход плоский;
2) mid-2025 – early 2026 — ACCELERATION, 4× YoY до $2,470: Claude Code + MCP + Computer Use — первый настоящий agentic era;
3) mid-2026 → — EXPLOSION, ~$9,000: frontier agents, 1M+ context, GPT-6 Astra.
Каждая эра (Chat → ReAct → Reasoning → Agents → Multi-agent → Computer Use → Frontier)
умножает токенов на задачу в ~10×, и каждая ключевая модель (GPT-5, Claude, Gemini, GPT-6) —
новая ступень расхода. Удобно: агенты делают работу. Дорого: платит вся компания — «AI tax».
-->

<div class="hook-line">Компании хотят возврата инвестиций, так что открывайте кошелек шире</div>

---
hideInToc: true
class: timeline-slide
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# IT в 2026 — полоса юридических препятствий

<RegulatoryTimeline />


<div class="hook-line">Для данных существуют границы и незаконное пересечение имеет последствия</div>

<!--

Риски
- Юридические
- Финансовые
- Репутационные
-->

<!--
Полный регуляторный таймлайн (даты вступления в силу):
2000 COPPA (США, дети <13) · 2002 ePrivacy (ЕС, cookies) · 2006 152-ФЗ (РФ, ПДн)
2014 242-ФЗ (РФ, локализация ПДн) · 2018 GDPR (ЕС, штрафы до 4% выручки, DPO, 72ч)
2020 CCPA (США) + Schrems II (CJEU, недействителен Privacy Shield → только SCC + TIA)
2020 LGPD (Бразилия) · 2021 PIPL (Китай, до 5% выручки)
2023 DPDP (Индия) + 12+ штатов США (VCDPA, CPA, CTDPA, OCPA, UCPA, ICPA)
2024 EU AI Act (риск-модель) · 2025 420-ФЗ (РФ, штрафы до 500 млн ₽ / 3% выручки, уголовка до 10 лет)
2025 EU Data Act (portability, cloud switching) · 2026 EU AI Act — full application (high-risk, Art. 50)

Ключевой нарратив: IT-отрасль прошла путь от «wild west» до heavily regulated industry.
IT-компания сегодня обязана иметь: consent-менеджмент, data localization, breach notification
(72ч в ЕС / 24ч в РФ), DPO, transfer impact assessments (Schrems II), AI governance,
audit trails, right to be forgotten. Это не опциональная надстройка, а базовый compliance-контур.
-->

---
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Гибридная инфраструктура — способ решения

<img class="data-chart" src="/img/hybrid-infra.svg" alt="Схема гибрида: Cloud (быстро) + Self-hosted (надежно), закрытые риски">

<div class="hook-line">Cloud — чтобы быстро двигаться, self-hosted — чтобы долго двигаться</div>

<!--
Cloud - чтобы быстро двигаться, Self-hosted - чтобы долго двигаться

- **Cloud** — frontier-модели: сложный reasoning, пики трафика, эксперименты
- **Self-hosted** — рутина, приватные данные, 24/7-нагрузка: без лимитов и без счёта

Риски
- Юридические
- Финансовые
- Репутационные
-->

---
layout: section
hideInToc: true
title: С чего начать Self-hosted?
---

<SectionCard kicker="" title="С чего начать Self-hosted?" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
title: Подготовка — что ожидают пользователи, как запускать
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Что ожидают пользователи

<img class="data-chart" src="/img/user-expectations.svg" alt="Ожидания 2026: скорость 80–100 ток/с, контекст 256k токенов, объём 50M токенов/сутки на чел., качество не хуже Claude 3.5 Sonnet, OpenAI/Anthropic-совместимый API, статистика и управление доступами">

<div class="hook-line">Dogfooding — ключ к пониманию требований</div>

<!--
Требования сформулированы через dogfooding: моя команда первые месяцы работала через
эту инфраструктуру, и «боль» стала списком требований. Поиск по Reddit и блогам 2026
показал: это не «завышенные» запросы, а стандарт года.

Скорость: 80–100 tok/s на одиночный запрос — нижняя граница «не раздражает».
Опрос r/LocalLLaMA: 8–12 tok/s — минимум для кода, 15–25 — «терпимо для чата».
8000 токенов при 16 tok/s = 8 минут на один ответ — точка, где бросают локальные модели.
Overthinking (Qwen3.8, Simon Willison 2026-08-16) = 5–10× больше output = 5–10× дольше ожидание.

Конкурентность: 3–4 человека одновременно без просадки — стандарт 2026 для команды
3–4 разработчиков. Порог: «4+ concurrent users — vLLM batching wins» (Ollama 12 vs vLLM 80 tok/s).
Агенты (pi.dev, Cursor, Kilo) создают 3–10 параллельных запросов на человека, а не 1.
Люди прощают, что один запрос медленнее, но не прощают, что все запросы одновременно становятся медленными.

Контекст: 256k — минимум для агентов-кодеров, а не «фича». Qwen3.6/3.8: 262k — дефолт.
Но реальное ожидание — 256k + стабильное качество на всём протяжении («gets dumber as context fills»)
+ быстрый prefill (TTFT < 2–3 с на 100k input). Типичный агентский цикл: 50–100k input, 5k output, пик 200k.

Объём: 100M токенов/день/человек — верхняя граница «агентского кодинга»
(1–2M/день — уже реальность; 100M/день = $570K/год на API = ~$1M+/год экономии при масштабе).
Для команды 3–4 человека — 300–400M токенов/день на кластер. Это точка, где стоимость API
превышает стоимость железа — self-hosting становится бизнес-кейсом, а не хобби.

API: OpenAI/Anthropic-совместимый — код-агенты (pi.dev, Cursor, Kilo) подключаются
без смены клиента; в 2026 это де-факто стандарт, а не «фича».

Статистика и управление доступами: счётчики токенов и запросов по пользователям
и моделям, API-ключи — кто сколько сжёг и на какой модели (GPUStack).

Главная боль 2026 (тред «I'm done with local LLMs for coding», 648 upvotes):
не «локальная модель хуже Claude», а «локальная модель медленнее и менее предсказуема».
Люди готовы на локальную модель, если: скорость ≥ 80–100 tok/s, контекст 256k без деградации,
tool use на уровне Claude Code, и стабильные (не «иногда 30, иногда 5») 80+ tok/s.
-->

---
title: Чем запустить LLM модель?
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Чем запустить LLM модель?


<EngineCompare />

<img class="model-load-path" src="/img/model-loading.svg" alt="Путь модели: скачиваем с HuggingFace (X GB) → сохраняем на диск (X GB) → загружаем в RAM (1.2X GB) → загружаем в VRAM (1–2X GB). X — размер модели; коэффициенты — сколько нужно относительно размера модели">

<div class="hook-line">Движок — это способ раскладки модели в VRAM + API обращения к модели</div>

<!--
Шкала оценок (1–5, точки: оранжевые — сложность, изумрудные — возможности).
Сложность — порог входа (настройка, зависимости, понимание параметров).
Возможности — что умеет движок (batching, квантизация, TP, API, hardware-coverage).
Лестница: чем выше по списку, тем сложнее и тем мощнее. vLLM — оптимум «сложность/возможности»
(3/5 vs 4/5), поэтому путь до 1 млрд токенов — Ollama → llama.cpp → vLLM.

Схема под таблицей — путь модели: скачиваем с HuggingFace (X GB) → сохраняем на диск (X GB) →
загружаем в RAM (1.2X GB) → загружаем в VRAM (1–2X GB). X — размер модели на диске,
коэффициенты — сколько нужно относительно размера модели:
- RAM 1.2X — транзитный буфер: модель читается в RAM, потом копируется в VRAM; +10–20% overhead (OS, буферы, CUDA context).
- VRAM 1–2X — веса (1X) + KV-cache (растёт с контекстом и конкурентностью: 0 → 1X+ на длинном) + 10–20% overhead.
  Короткий контекст ~1.1–1.3X, длинный (128K+) — 2X и выше.
Модель не грузится «напрямую в GPU» — она идёт через RAM. Движок организует эту раскладку весов в VRAM + API.
Наш стек (Qwen3.8-27B-AWQ, 16 GB на диске, 2×RTX 3090): RAM ≥ 32 GB (2X, с запасом),
VRAM ~20–24 GB на 32K контекст (1.3–1.5X), до ~39 GB на 256K (2.4X).
Источники: Runpod / Netra / Modular (VRAM = веса + KV-cache, overhead 10–20%) · GIGAGPU (RAM при загрузке).

Полное сравнение движков (детали для речи):
- vLLM — де-факто стандарт production-сервинга. NVIDIA (CUDA), AMD ROCm, TPU, Gaudi, CPU.
  Safetensors, AWQ, GPTQ, FP8, INT8, bitsandbytes. PagedAttention, continuous batching,
  OpenAI API, самый широкий hardware-coverage и экосистема. Default-выбор для self-hosted production.
- SGLang — максимальный throughput + structured output. GPU-first. RadixAttention (prefix-cache):
  до ~29% быстрее vLLM на H100, до 6.4× на prefix-heavy нагрузках; xGrammar для JSON/structured output.
  Берём, если workload уйдёт в агентов с длинным общим system prompt.
- TensorRT-LLM — максимальная производительность, только NVIDIA. FP8/FP4 (NVFP4), AWQ/GPTQ (W4A16/W4A8), INT8.
  Самый высокий peak throughput и минимальная латентность на H100/H200/B200, но нужна компиляция модели
  (длинный cold start, пересборка при смене модели). На 3090 нецелесообразно — не наш сценарий.
- llama.cpp — edge / CPU / consumer GPU. GGUF (Q4_K_M, Q5_K_M, Q8_0). Чистый C/C++, без зависимостей,
  offload слоёв CPU↔GPU, работает на 8 GB VRAM и даже на чистом CPU.
- Ollama — одна команда, OpenAI-совместимый API, реестр готовых моделей. Dev, эксперименты, прототипы.
- TGI (Hugging Face) — maintenance mode (2026): брать только если уже сидите в HF-стеке.
- LMDeploy (TurboMind) — ~1.5–1.8× throughput vs vLLM на A100/H100 (Llama-3.1-8B: ~16 200 tok/s на H100).

Форматы моделей: GGUF → локальный/edge (llama.cpp/Ollama); AWQ/FP8 → production-сервер (vLLM/SGLang).
Наш стек (Qwen3.8-27B-AWQ-MTP, 2×RTX 3090, Ampere): vLLM — основной production-движок (AWQ, TP=2, MTP);
SGLang — альтернатива при prefix-heavy нагрузке; llama.cpp/Ollama — edge и CPU-фолбэк;
TensorRT-LLM — не наш сценарий (H100+ и компиляция моделей).
Источники: LeetLLM 2026 · Particula (SGLang vs vLLM) · PremAI 2026 · CloudAI H100 benchmarks 2026 ·
Digital Applied (GGUF vs AWQ vs GPTQ vs MLX) · Spheron (LMDeploy) · vLLM docs · BuildMVPFast (TGI).
-->

---
layout: section
hideInToc: true
title: Поехали запускать!
---

<SectionCard kicker="" title="Поехали запускать!" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
title: Начинаем — запуск первой модели, ollama
class: stepper-slide
---

# Начинаем — запуск первой модели, ollama

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<Stepper
  :steps="[
    { num: '01', title: 'Видеокарта, которая есть', meta: 'Tesla M40 · 24GB', imgs: [{ src: '/img/hardware/step-00.jpg', alt: 'Tesla M40 — видеокарта, которая уже была' }] },
    { num: '02', title: 'Скачиваем', chip: 'ollama pull' },
    { num: '03', title: 'Запускаем', chip: 'ollama serve' },
    { num: '04', title: 'Получаем', metric: '10–20', unit: 'ток/сек' },
    { num: '05', title: 'Начало пути', meta: 'к 1 млрд токенов/сутки', art: 'excited', dark: true },
  ]"
/>

<div class="hook-line">ollama — отличный способ "начать", прямо сейчас</div>

<!--
Старт истории — «железо, которое есть». Tesla M40: 24GB вроде бы хватает,
но очень шумная, очень медленная, без tensor-ядер, и NVIDIA её уже не поддерживает —
запускать на ней что-то — само по себе геморрой.
Берём с ollama модель, которая влезает в 24GB, запускаем — видим 10–20 tok/s
с контекстом 16k. Работает. Но это не то, что нужно (спид 80–100 tok/s, контекст 256k).
Отсюда начинается долгий путь.
-->

---
title: Итого — шумит, тормозит, тупит
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Итого — шумит, тормозит, тупит

<StageProblems stage="s1" />

<div class="hook-line">Ollama «просто работает» — но дефолты собраны для демо, а не для команды</div>

<!--
Таблица: 6 параметров (СКОРОСТЬ, КОНТЕКСТ, ОБЪЁМ, КАЧЕСТВО, API, УПРАВЛЕНИЕ) —
ожидание (слайд «Что ожидают пользователи») vs на этапе M40 + Ollama.
Статус: ✓ — соответствует ожиданию, ~ — частично, ✗ — нет. S1 — почти весь столбец ✗:
это «демо-рантайм», а не инфраструктура.
Особенности этапа (3 карточки):
1. Шум · M40 — 250W: вентилятор на 100% под нагрузкой, NVIDIA уже не поддерживает.
2. Холодный старт — keep_alive 5m: модель выгружается из VRAM, следующий запрос платит загрузкой.
3. Реплики — нет реестра: новый узел = скачать заново или копировать blobs вручную.
Вывод: это не «Ollama сломан», а «Ollama — демо-рантайм». Путь — не тюнинг Ollama, а смена рантайма.
TODO(спикер): контекст — 4096 (дефолт) или 16k (из заметок «Начало»)? quality — какая модель влезла в 24GB?
-->

---
title: Что дальше? Больше видеокарт и llama.cpp
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Что дальше? Больше видеокарт и llama.cpp

<StageIdeas stage="s1" />

<!--
Шесть идей — сетка 2×3, у каждой тег(и) параметра (цветная точка = палитра user-expectations.svg):
01 consumer GPU: 3060 · 4070 Ti · 3090 — особенность · шум (M40 — 250W, вентилятор на 100%).
02 llama.cpp + CUDA — [ОБЪЁМ, СКОРОСТЬ]: --parallel N — N слотов, у каждого свой контекст.
03 контекст — подбираем сами — [КОНТЕКСТ]: num_ctx 4096 → --ctx-size под задачу, до 256K.
04 модель держим в VRAM — [СКОРОСТЬ]: без keep_alive — нет холодных стартов.
05 GPUStack — статистика — [УПРАВЛЕНИЕ]: счётчики токенов и запросов по моделям, пользователям, API-ключам.
06 GPUStack — реплики — особенность · надёжность: replicas N + auto-restart после crash.
Переход к следующему слайду: как это выглядело в железе — шаг за шагом.
-->

---
title: GPUStack — оркестратор ИИ
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# GPUStack — оркестратор ИИ

<GpuStackPanel />

<div class="hook-line">Кластер стал сервисом: модели, реплики, ключи, статистика — одна панель</div>

<!--
GPUStack — open-source GPU-кластер-менеджер: AI gateway для self-hosted кластера.
Одна панель: деплой моделей, воркеры, API-ключи, статистика использования.

Слайд — 2 колонки. Слева 4 возможности панели, каждая со своей мини-визуализацией:
- Модели: скачивание с Hugging Face / ModelScope / локального пути, replicas N,
  auto-restart при ошибке (exponential backoff, до 5 минут) → пилюля «Running · 1/1».
- Движки: подключаемые — vLLM, SGLang, TensorRT-LLM, MindIE + custom → чипы рантаймов.
  В нашем стеке: llama.cpp (этап 2), vLLM (этап 3).
- API: OpenAI-совместимый /v1/chat/completions; API-ключи: доступ по моделям,
  срок действия, SSO → код-чип endpoint + Bearer.
- Статистика: токены и запросы по пользователям и API-ключам (Usage & Billing) →
  метрика 343 tok/s. Это ответ на ожидание «статистика и управление доступами».

Справа 2×2: 3 скриншота реального UI + Usage-график.
- Каталог — выбор модели из каталога (Qwen, GLM, Gemma, Nemotron…).
- Deployments — Running, реплики 1/1 (0.8B-модель из каталога — демо; у нас — 27B AWQ на 2×3090).
- Chat — playground: ответ + Token Usage 62 + Output 343.28 Tokens/s.
- Usage & Billing — мини-график «кто сколько сжёг» (токены по пользователям).
Наш стек на этом этапе: 2 сервера (3060 + 4070 Ti) под Proxmox, GPUStack + llama.cpp.
Источники: docs.gpustack.ai — Overview, Model Deployment Management,
API Key Management, Model Route Management, Usage.
-->

---
layout: section
hideInToc: true
title: Продолжаем тюнить
---

<SectionCard kicker="" title="Продолжаем тюнить" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
title: Продолжаем — Proxmox, GPUStack, llama.cpp
class: stepper-slide
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Продолжаем — Proxmox, GPUStack, llama.cpp

<Stepper
  :steps="[
    { num: '01', title: '2 сервера', meta: '3060 + 4070 Ti · Xeon 3-го поколения · 24GB VRAM каждый', imgs: [{ src: '/img/hardware/step-01.jpg', alt: 'Сервер №1 — 3060 + 4070 Ti + Xeon 3-го поколения' }, { src: '/img/hardware/step-02.jpg', alt: 'Сервер №2 — 3060 + 4070 Ti + Xeon 3-го поколения' }] },
    { num: '02', title: 'Виртуализация', chip: 'Proxmox', meta: 'RAM · VRAM · SSD — одна консоль' },
    { num: '03', title: 'Оркестрация', chip: 'GPUStack', meta: 'модели · запуск · auto-restart' },
    { num: '04', title: 'Движок инференса', chip: 'llama.cpp', meta: 'модель в VRAM' },
    { num: '05', title: 'Можно пользоваться', metric: '50–70', unit: 'ток/сек', dark: false },
  ]"
/>

<div class="hook-line">Первые пользователи и первый счёт за электричество — кластер уже инфраструктура</div>

<!--
Появилось 2 сервера: 3060 + 4070 Ti + Xeon 3-го поколения, 24GB VRAM каждый.
Серверы объединили в Proxmox-кластер — централизованный контроль RAM, VRAM, SSD.
GPUStack — скачивание моделей, запуск, auto-restart; статистика по пользователям и API-ключам.
llama.cpp — рантайм: контекст под задачу, модель держим в VRAM (без холодных стартов).
Итог: 50–70 ток/сек, первые пользователи.
Цена этапа: электричество 24/7 (начался счёт), китайские материнские платы (хуанан).
-->

---
title: Итого — для 1 отдела хватит
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Итого — для 1 отдела хватит

<StageProblems stage="s2" />

<div class="hook-line">llama.cpp умеет запускать модели в RAM, когда не хватает VRAM</div>

<!--
TODO(спикер): данные S2 (3060/4070 Ti + llama.cpp) не собраны — все ячейки таблицы TODO.
Особенности этапа: китайские материнские платы (хуанан), электричество, первые пользователи.
Заполнить до финального экспорта.
-->

---
title: Что дальше? RTX 3090 + vLLM
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Что дальше? RTX 3090 + vLLM

<StageIdeas stage="s2" />

<!--
TODO(спикер): идеи S2 не собраны. Кандидаты: докупить 3090, TP, переход на vLLM.
Заполнить до финального экспорта.
-->

---
title: Подбор модели под железо
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Подбор модели под железо

<VramBudget />

<div class="hook-line">На Ampere нет FP8 — поэтому 27B на 2×3090 живёт в AWQ INT4</div>

<!--
Как подбирать версию модели под железо — алгоритм (6 шагов):
1. БЮДЖЕТ VRAM: суммарная VRAM кластера × gpu-memory-utilization (≈0.90) − overhead (~10–15%).
2. ЦЕЛЕВОЙ WORKLOAD: макс. контекст (8K / 32K / 128K?), целевая concurrency (1 / 4 / 16?) →
   KV-cache = f(контекст, concurrency, архитектура).
3. РАЗМЕР МОДЕЛИ: weights_VRAM ≈ params × bytes/param × 1.2; weights + KV ≤ бюджет →
   максимальный размер, который влезает.
4. ФОРМАТ ПОД GPU-АРХИТЕКТУРУ:
   - Ampere (RTX 3090/4090, A100): AWQ / GPTQ INT4 (W4A16); FP8 недоступен.
   - Hopper/Blackwell (H100/H200/B200): FP8 / NVFP4 — максимум throughput; AWQ — запасной.
   - CPU / edge / мало VRAM: GGUF Q4_K_M / Q5_K_M / Q8_0.
5. ПРОВЕРКА: weights + KV + overhead ≤ бюджет? Если OOM — лестница снижения:
   контекст ↓ → concurrency ↓ → квант ниже (Q4) → KV-cache FP8/INT8 (--kv-cache-dtype fp8)
   → CPU offload → больше GPU (TP).
6. ВАЛИДАЦИЯ КАЧЕСТВА: бенчмарк на целевых задачах (code / RAG / chat) vs FP16 baseline
   → фиксация модели + кванта в документацию.

Формулы:
- Веса: weights_VRAM ≈ params × bytes/param × 1.2 (×1.2 — embeddings, CUDA context).
  bytes/param: FP16/BF16 = 2 (27B ≈ 65 GB, 70B ≈ 168 GB) · FP8 = 1 (27B ≈ 32, 70B ≈ 84) ·
  AWQ/GPTQ INT4 = 0.5 (27B ≈ 16, 70B ≈ 42) · GGUF Q4_K_M ≈ 0.55 (27B ≈ 17) · GGUF Q8_0 ≈ 1.07 (27B ≈ 34).
- KV-cache (на 1 запрос): bytes/token = 2 × n_layers × n_kv_heads × head_dim × bytes_per_element;
  множитель 2 — храним и K, и V. GQA (мало KV-голов) сильно снижает размер.
  Пример: 27B dense, GQA, BF16 KV ≈ 1–4 GB на 32K контекст; при concurrency 4 — умножаем на 4.
  KV-cache не квантуется вместе с весами — отдельный потребитель VRAM (можно FP8/INT8 KV: --kv-cache-dtype fp8).
- Бюджет: weights + KV × concurrency + overhead ≤ VRAM × gpu-memory-utilization.

Форматы — когда что брать:
- FP16/BF16: 80 GB+ GPU, потеря 0% — эталон, валидация качества.
- FP8 / NVFP4: Hopper/Blackwell, потеря <1% — production на H100, максимум throughput.
- AWQ INT4 (W4A16): любая NVIDIA вкл. Ampere, потеря ~1–3% — default для RTX 3090/4090,
  лучшее качество среди 4-bit (защита «важных» весов до квантизации).
- GPTQ INT4 (W4A16): любая NVIDIA, потеря ~2–5% (чуть хуже AWQ на code) — запасной, если AWQ-чека нет.
- GGUF Q4_K_M / Q5_K_M / Q8_0: CPU, любая GPU, Mac; Q4 ~3–5%, Q8 <1% — edge, Ollama, мало VRAM, CPU offload.
Правила: Ampere → AWQ (FP8 нет); H100+ → FP8 (AWQ — fallback). Качество критично → AWQ > GPTQ;
VRAM критична → GGUF Q4_K_M (лучший баланс размер/качество). Длинный контекст → KV FP8/INT8
или снизить max-model-len. MoE (35B-A3B, DeepSeek): активные параметры малы — 35B-A3B в Q4
живёт на 24 GB, 120+ tok/s. Инструменты квантизации: auto-round (github.com/intel/auto-round), gptq-forge.

Наш стек (Qwen3.8-27B, 2×RTX 3090 = 48 GB, бюджет ≈ 43 GB):
- FP16 ≈ 65 GB — OOM, не влезает.
- FP8 ≈ 32 GB — недоступно: на Ampere нет FP8.
- AWQ W4A16: 16 GB весов (TP=2) + KV 2–4 GB (32K, 1 req) + overhead ≈ 5 GB → ~20–25 GB ✅ — наш выбор.
- GGUF Q4_K_M ≈ 17 GB → ~22 GB — альтернатива (llama.cpp).
Продакшн-реальность: 256K контекст → KV-cache растёт до ~18 GB, итого ~39 GB — влезает,
но max-num-seqs = 2 (KV съедает бюджет — см. «Итоги»).

Источники: alesha.pro (квантизация LLM 2026; сколько VRAM нужно для LLM) · kunwar.page (формула KV-cache)
· spheron.network (GPU sizing 2026) · iternal.ai (on-prem, W4A16 vs W8A8) · particula.tech (AWQ vs GPTQ vs FP8)
· premiai.io (GGUF vs AWQ vs GPTQ vs bitsandbytes) · tomodahinata.com (serving economics, KV budget)
· codersera.com (Qwen 3.6 27B dense vs 35B MoE на RTX 3090) · hivenet.com (KV cache и контекст, GQA).
-->

---
title: Что настраивать в движке inference?
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Что настраивать в движке inference?

<EngineTuning />

<div class="hook-line">Один параметр за раз — иначе не поймёшь, что именно дало эффект</div>

<!--
Тюнинг — не магия и не «крутим всё подряд», а повторяемый алгоритм:
workload → базовый конфиг → измерить baseline → итеративно крутить 4 группы
→ стабилизировать. Метрики-цели: TTFT (задержка первого токена),
TPOT/ITL (задержка на токен в декодинге), throughput (tok/s на GPU), VRAM headroom.

Правила, которые надо озвучить:
1. Один параметр за раз — иначе невозможно понять, что дало эффект.
2. Сначала память, потом скорость: OOM лечится max-model-len ↓ →
   gpu-memory-utilization ↓, и только потом крутим batching.
3. KV-cache — главный потребитель VRAM: max-model-len 131k → 32k может
   освободить десятки GB; контекст — первая жертва при OOM.
4. Chunked prefill включаем, когда длинные промпты «застревают» декодинг
   (ITL spikes); размер чанка 2048–4096 балансирует TTFT и throughput.
5. Speculative decoding (MTP) — добавляем последним: +30–100% decode-скорость,
   но ест VRAM и может деградировать на длинном контексте.
6. Prefix-heavy workload (агенты, RAG с общим system prompt) → SGLang +
   RadixAttention или vLLM prefix caching — до 6x на общих префиксах.
7. Валидация: бенчмарк при целевой concurrency (не пик), затем 24–72h
   load-test и мониторинг — конфигурация фиксируется в документацию.

Источники:
- Sector88 — How to fix vLLM OOM: 2026 checklist (sector88.co/blog/how-to-fix-vllm-oom)
- SGLang — Hyperparameter tuning (mem-fraction-static, schedule policy)
  (github.com/sgl-project/sglang/blob/main/docs/advanced_features/hyperparameter_tuning.md)
- CROZ — Tuning vLLM: token batching и chunked prefill (croz.net/run-your-own-ai-at-scale-vol-1-tuning-vllm/)
- Kunwar — vLLM in production: every flag that matters (kunwar.page/chapter/048-vllm-in-production-every-flag-that-matters)
- Habr — vLLM Production Stack: автоподбор gpu_memory_utilization и maxNumSeqs × max-num-batched-tokens (habr.com/ru/articles/1016062/)
- NVIDIA Forum — MTP + 3 knob'а: max-num-batched-tokens 8192→4096, −30% TTFT (forums.developer.nvidia.com)
- Spheron — DeepSeek-V4 MoE: OOM at launch → reduce max-model-len first (spheron.network)
- Dre Dyson — Qwen3.6-27B deployment: gpu-memory-utilization 0.75, max-model-len 32768 (dredyson.com)
- llama.cpp — server README: n_batch, n_ctx, flash attention, threads (github.com/ggml-org/llama.cpp)
-->

---
title: Балансировка LLM трафика
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Почему Round Robin не работает для LLM

- **Запросы не однотипные**: chat — 10–20 с, агент — 1–3 мин (input 100k, output 5k) — в 100–10 000× дольше web-запроса
- **Стоимость ∝ токенам**: prefill + decode держат слот минуты, а Round Robin об этом не знает
- **KV-кэш на ноде**: диалог и общий system prompt должны оставаться на одной ноде — иначе каждый тур переплачивает prefill

<img class="data-chart" src="/img/lb-round-robin.svg" alt="6 запросов на 3 репликах за 12 секунд: Round Robin — длинный запрос R1 (8 с) на ноде A, следующий по кругу запрос R4 ждёт в очереди 2 с, B и C простаивают; least-loaded — те же запросы распределяются по текущей загрузке, очереди нет">

<div class="hook-line">Round Robin равномерно распределяет запросы — но LLM-запросы не равномерны. Мы распределяем нагрузку</div>

<!--
Контраст: web-запрос vs LLM-запрос.
- Web-запрос: ~50 мс, однородные → Round Robin хорош: запросы равны, делить поровну можно.
- LLM-запрос: 10 с — 10+ минут. Стоимость ∝ токенам: prefill (input, compute-bound) + decode (output, memory-bound).
  Агентский запрос: input 100k токенов (prefill — секунды) + output 5k токенов ≈ 1 мин при 80 tok/s.
- Почему RR ломается: RR распределяет «запросы», а не «нагрузку». Длинный запрос (R1) занимает слот 8 с,
  следующий по кругу (R4) падает на ту же ноду → очередь. Остальные ноды простаивают.
  Пользователь на «горячей» ноде видит просадку, остальные — пустоту.
- KV-кэш: multi-turn диалог каждый тур пересылает всю историю. Та же нода → cache hit,
  prefill в 5–10× быстрее; другая нода — пересчёт всего контекста. Общий system prompt (агенты) — то же.
- Схема на слайде условная: 6 запросов, 3 реплики, 12 с. R1 — «тяжёлый» (100k prefill + decode, 8 с),
  остальные — 1.5 с. Сверху — RR (по кругу). Снизу — least-loaded: каждый запрос — на наименее
  загруженную; ничья — round-robin среди минимальных.
- Переход: нагрузка — только половина дела. Вторая половина — KV-кэш (sticky) и health.
-->

---
title: Балансировка LLM трафика
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Свой балансер: load · sticky · health

| Сигнал | Источник | Правило |
|---|---|---|
| **Load** | vLLM `/metrics` (3 с) + in-flight WLC | сначала без очереди, затем least-loaded |
| **Session** | header `x-session-id` | pin: TTL 60 мин, rebind после 3 spill |
| **Prefix** | MD5(system prompt) | pin: TTL 5 мин, отпускается при перегрузе |
| **Health** | scrape + 5xx | LIVE ⇄ PROBING ⇄ EJECTED, активный probe |

<img class="data-chart" src="/img/lb-balancer.svg" alt="Пайплайн выбора реплики: пул LIVE ∪ PROBING → no-wait (waiting = 0) → least-loaded (min running) → pin (session → prefix) → affinity или load; health-машина: EJECTED → 2× scrape OK → PROBING → 15 s clean → LIVE, eject при 5xx burst / stuck 45 s / scrape fail ×2; EJECTED без user traffic, scrape продолжается">

<div class="hook-line">Мягкий sticky: KV-кэш работает, а трафик не кристаллизуется на одной ноде</div>

<!--
Три сигнала: load, sticky, health. Принципы: routing простой, health не зависит от user traffic.

1. LOAD — scrape vLLM /metrics каждые 3 с (num_running, num_waiting, KV usage) + локальный in-flight (WLC):
   effective_running = max(scrape, in-flight); effective_waiting = waiting + max(0, in-flight − running).
   WLC — weighted least connections: каждый in-flight запрос учитывается по весу токенов
   (100k весит в 100× больше, чем 1k). Синхронизация со scrape: grace 15 с (запрос «в полёте»
   не сбрасывается idle-scrape'ом), backstop 15 мин на потерянные completion-сигналы.
   No-wait: если есть LIVE с waiting = 0 — берём только их. Least-loaded: min(effective_running),
   ничья — round-robin, LIVE предпочтительнее PROBING.

2. STICKY (soft affinity) — KV-кэш работает, трафик не кристаллизуется:
   - Session key: из заголовков (x-session-id, x-kilo-session, x-claude-code-session-id, x-opencode-session,
     x-kilocode-taskid, …) или body (conversation_id, thread_id). x-client-request-id исключён — это per-request id.
   - Prefix key: MD5 первых 4096 символов system prompt; для multi-tenant — + project_id.
   - Pin usable: LIVE + waiting = 0 + running ≤ min + slack (session 1, prefix 0).
     Session держится при 1 vs 0, ломается при 2 vs 0; общий system prompt не держит горячую ноду (slack 0).
   - Rebind: 3 spill подряд → session переезжает на новую ноду; force rebind: running(pin) − min ≥ 3 — сразу.
     Prefix: expunge при повторяющемся spill. TTL: 60 мин / 5 мин — чинит «через 10 минут всё на одной».
   - Новый bind только на LIVE; PROBING sticky не принимает.

3. HEALTH — без user traffic:
   - EJECT: 2× failed scrape, 5xx > 30%/мин, stuck (num_running > 0 и in-flight = 0 дольше 45 с), state ≠ running.
   - Возврат: 2× scrape OK → PROBING (без sticky, ограниченный трафик), 15 s clean → LIVE.
     Cooldown: 30 с базовый, экспоненциально до 300 с при повторных eject (защита от flap).
   - EJECTED: user traffic нет, но /metrics скрейпится дальше — это единственный путь возврата.
     Мёртвую реплику «не проверяем» пользовательскими запросами.

Чего не делаем (осознанно): composite score, consistent hashing, Power of Two, температура GPU
(лагging-сигнал; running/waiting — прямое измерение нагрузки), slow-start в routing — только в Grafana.
Observability: Traffic Share, Affinity %, Spill Rate, Force-Rebind Rate, LIVE/PROBING/EJECTED,
imbalance index + алерты (весь трафик на одной ноде, сломанный probe, prefix spill).
-->

---
title: Стабилизация — агенты, балансер, vllm
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Стабилизация — агенты, балансер, vllm


<Stepper
  :steps="[
    { num: '01', title: '3 сервера', meta: '4x(2x3090)· 48GB VRAM каждая пара', imgs: [{ src: '/img/hardware/step-03.jpg', alt: 'Сервер' }, { src: '/img/hardware/step-04.jpg', alt: 'Сервер' }] },
    { num: '03', title: 'Модель', chip: 'AWQ+MTP', meta: 'модели · запуск · auto-restart' },
    { num: '04', title: 'Движок инференса', chip: 'vLLM', meta: 'модель на 2 видеокартах' },
    { num: '05', title: 'Балансировщик', chip: 'свой балансер', meta: 'липкие сессии' },
    { num: '06', title: 'Нужно пользоваться', metric: '100+', unit: 'ток/сек для чел.', dark: false },
  ]"
/>

---
title: Итоги
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Итоги

<StageProblems stage="s3" />

<div class="hook-line">Итого: 12 видеокарт (8×3090, 2x4070, 2x3060) и 1 TB RAM</div>

<!--
Таблица: 6 параметров — ожидание vs на этапе 8×3090 + vLLM + GPUStack.
S3: скорость ~ (75 tok/s на пользователя, 210 aggregate), контекст ✓ (256K),
объём ✓ (1 млрд/сутки пик), качество ~ (Qwen3.8: TB 73, DeepSWE 42.2 — не ≥ Claude, но для своих задач хватает),
API ✓ (vLLM OpenAI-совместимый), управление ✓ (GPUStack счётчики).
Особенности этапа (3 карточки):
1. MTP crash — vLLM 0.27.1: wild write, рантайм умер на 3-й день — лечится 0.28.0.
2. Нет FP8 — Ampere: квант — AWQ (INT4), а не FP8.
3. 24GB — потолок — max-num-seqs 2: 256K + 27B весов, параллельность 8 → 2 запроса.
TODO(спикер): подтвердить черновик (75 tok/s, 1 млрд/сутки, Qwen3.8, MTP crash, max-num-seqs 2).
-->

---

# Заключение

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

- **1 млрд токенов в сутки — это не про железо.** Это про то, что я перестал быть пользователем API и стал оператором инфраструктуры



<div class="hook-line">Это не конец, а checkpoint.</div>

<!--
Финал: 24/7, без лимитов, без счетов, без зависимости от чужого uptime — и это стоит $3,200/год,
а не $20–73K. Roadmap: Qwen4 (3090 не потянет — нужен 4090/H100), RAG-сервис, AI Gateway.
-->

---
layout: center-dark
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

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Финал: Q&A, ссылки, контакты.
-->
