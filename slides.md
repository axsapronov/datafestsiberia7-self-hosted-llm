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

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

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
title: Что ожидают пользователи?
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
title: Как запустить LLM модель?
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Как запустить LLM модель?

- TODO
- Inference движки, ollama, llama.cpp, vllm, sglang, etc


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
title: GPUStack — панель управления self-hosted
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# GPUStack — панель управления self-hosted

- TODO
- Перечень возможностей (ai gateway)
- Скриншоты


---
title: Что настраивать в движке inference?
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Что настраивать в движке inference?

- TODO
- Обобщенный алгорим


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

<div class="hook-line">TODO (спикер): hook-line</div>

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

- TODO
- Квантование
- https://github.com/intel/auto-round
- Архитектура поколений видеокарт




---
title: Балансировка LLM трафика
hideInToc: true
---

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

# Балансировка LLM трафика

- TODO
- Учет загруженности видеокарты
- Учет температуры видеокарты
- Учет прогретости кэша




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
