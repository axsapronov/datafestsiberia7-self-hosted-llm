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
  <div class="speaker-bio">Решаю бизнес задачи в IT. МТС, Avito, Welltory</div>
  <div class="speaker-contacts"><a href="https://t.me/axsapronov">t.me/axsapronov</a> · <a href="mailto:a@sapronov.me">a@sapronov.me</a></div>
</div>

---
hideInToc: false
title: Зачем собирать свою ИИ-инфраструктуру
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
title: Какую инфраструктуру собирать?
---

<SectionCard kicker="Часть 1" title="Что дают consumer GPU" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>



---
layout: section
title: Начало — запуск первой модели
---

<SectionCard kicker="Часть 1" title="Что дают consumer GPU" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>


---
layout: section
title: Продолжение — пользователи и электричество
---

<SectionCard kicker="Часть 1" title="Что дают consumer GPU" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>


---
layout: section
title: Текущее состояние — себестоимость
---

<SectionCard kicker="Часть 1" title="Что дают consumer GPU" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>



---
hideInToc: true
---

# Почему не API

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

<div class="num-cap">Стоимость нашего объёма через API (blended $0.14–0.50/1M)</div>

| Объём в месяц | API |
|---|---:|
| 100M токенов | $14–50 |
| 500M токенов | $70–250 |
| 1B токенов | $140–500 |

::right::

<v-clicks>
- **Приватность** — данные не уходят наружу. Для RU-рынка с чувствительным кодом это не «nice to have», а требование
- **Автономность** — нет rate limits, инцидентов провайдера, региональных блокировок
- **Контроль** — я вижу каждый токен: где сгенерирован, сколько стоит, почему запрос занял 8 секунд
</v-clicks>

<!--
Злодей истории — API. «API дорогой, локально дешевле» — скучная аргументация.
Для нас критичны три вещи: приватность (RU-рынок, чувствительный код),
автономность (uptime, блокировки), контроль (каждый токен виден).
-->

---
hideInToc: true
---

# Путь: от 2 серверов до фермы

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<div class="hw-grid">
  <div class="hw-cell"><img src="/img/hardware/step-00.jpg" alt="№0. Вроде 24GB, но очень шумные, но очень медленные. Нет tensor ядер. Много геморроя, так как уже не поддерживаются NVidia"></div>
  <div class="hw-cell"><img src="/img/hardware/step-01.jpg" alt="№1. Два сервера по 3060+4070Ti+Xeon 3 поколения"></div>
  <div class="hw-cell"><img src="/img/hardware/step-02.jpg" alt="№2 Удалось закупиться и появился 2 сервера , по 1x3090, и предыдущий 4070+4070.Тогда использали китайские материнские платы (хуанан). Пошли в gpustack"></div>
  <div class="hw-cell"><img src="/img/hardware/step-03.jpg" alt="№3"></div>
  <div class="hw-cell"><img src="/img/hardware/step-04.jpg" alt="Эксперимент с 5x3090 на сервере"></div>
  <div class="hw-cell"><img src="/img/hardware/step-05.jpg" alt="Наведение порядка"></div>
  <div class="hw-cell"><img src="/img/hardware/step-06.jpg" alt="Наведение порядка"></div>
  <div class="hw-cell"><img src="/img/hardware/step-07.jpg" alt="Наведение порядка"></div>
  <div class="hw-cell hw-cell-label">
    <div class="big">8×3090</div>
    <div class="small">+ RAG-узел</div>
    <div class="small">2×4070 Ti · 4×3060</div>
  </div>
</div>

<div class="hook-line">Начиналось с двух серверов и кучи компромиссов — китайские SSD, хуанан, ollama. До порядка дошёл только через GPUStack.</div>

<!--
Реальный путь фермы — из истории закупки, не из документации.
Старт: 2 сервера (3090 + 4070), Xeon 3-го поколения. Китайские SSD «съедали мозг» —
первый настоящий конфликт. Эксперименты с ollama — не потянули нагрузку.
Рост: докупил 2 сервера по 1×3090 + предыдущий 4070+4070. Китайские материнские платы (хуанан).
Перешёл на GPUStack — появился auto-restart и monitoring.
Хаос: сервер 5×3090, затем 4 сервера (3090+3060, 3090, 4070+4070, 3090+3090) —
разношёрстное железо, без порядка.
Порядок: pve4 с 4×3090 приведён в порядок → 8×3090 под инференс + RAG-узел (2×4070 Ti + 4×3060).
-->

---
layout: section
title: Что дают consumer GPU
---

<SectionCard kicker="Часть 1" title="Что дают consumer GPU" tone="violet" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
hideInToc: true
---

# Qwen — это не Claude

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

<div class="col-cap ok">Что он умеет</div>

- Агентный кодинг: держит длинную историю, tool calls, генерирует код
- RAG с контекстом 256K
- Работает 24/7 без лимитов и без счёта

::right::

<div class="col-cap no">Чего он не умеет</div>

- Качество не top-tier: сложный reasoning, длинные тексты — «решает» vs «почти решает»
- Заменяет Claude/GPT не для всех задач — только для своих

<div class="hook-line">Ожидания нужно резать сразу — и команда будет довольна.</div>

<!--
Честные ожидания: consumer-кластер решает реальные задачи (агентный кодинг, RAG, 24/7),
но не заменяет топ-модели по качеству. Разрыв виден на SWE-задачах: 42.2 vs «почти решает».
-->

---
hideInToc: true
---

# 12 моделей, 1 победитель

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

Протестировал на 2×3090: **8 — мусор** для агентного кодинга, 3 — нормальные, 1 — та, что у меня каждый день.

<v-clicks>
- **Агентный кодинг** (pi.dev, Cursor, Kilo) — не чат и не RAG
- **Контекст 256K** — история + код + tool calls; меньше — не работает
- **MTP** — критично для скорости на 3090
- **VRAM 24GB×2** (TP=2) — не влезает — отпадает
- **Русский язык** — для RAG-сервиса
</v-clicks>

<!--
Критерии — «какая подходит для наших задач на нашем железе», а не «какая самая умная».
Terminal-Bench и DeepSWE — рабочие метрики из пайплайна, не MMLU из таблицы.
-->

---
hideInToc: true
---

# Бенчмарки: 2×RTX 3090, vLLM, AWQ

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<table>
  <thead>
    <tr><th>Модель</th><th class="num">tok/s</th><th class="num">TTFT (8K)</th><th class="num">Terminal-Bench</th><th class="num">DeepSWE</th></tr>
  </thead>
  <tbody>
    <tr class="featured"><td><b>Qwen3.8-27B-AWQ-MTP</b></td><td class="num"><b>75</b></td><td class="num"><b>1.8s</b></td><td class="num"><b>73.0</b></td><td class="num"><b>42.2</b></td></tr>
    <tr><td>Qwen3.6-27B</td><td class="num">64</td><td class="num">2.0s</td><td class="num">63.4</td><td class="num">13.3</td></tr>
    <tr><td>GLM-4.6</td><td class="num">48</td><td class="num">2.4s</td><td class="num">61.2</td><td class="num">17.5</td></tr>
    <tr><td>Gemma4-26B</td><td class="num">66</td><td class="num">2.0s</td><td class="num">52.4</td><td class="num">8.9</td></tr>
    <tr><td>DeepSeek-V3.2 · Llama 4 Scout (MoE)</td><td class="num">—</td><td class="num">—</td><td class="num">—</td><td>не влезает</td></tr>
  </tbody>
</table>

<div class="num-cap">Qwen3.8 — лучший *для моих задач на моём железе*, а не лучший в мире. Для другого стека победитель мог бы быть другим</div>

<!--
DeepSeek-V3.2 (MoE 671B) и Llama 4 Scout (MoE 109B) — не влезает. Точка.
GLM-4.6: нет MTP, на SWE-задачах в 2.4 раза слабее Qwen3.8.
Честно: GPT-5.6 и Claude Opus не тестировал — они не влезут на 3090.
-->

---
hideInToc: true
---

# MTP: ×2.5–2.7 на 3090

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

<div class="code-cap">Speculative decoding</div>

```text
обычный:   [T1] → [T2] → [T3]     3 шага
MTP:       [T1 T2 T3] → verify    1 шаг
```

::right::

<v-clicks>
- Модель предсказывает **3 токена сразу**, а не 1; если «верификатор» соглашается — 3 токена за стоимость 1
- На коротких промптах: **18 → 45 tok/s (×2.5)**; на длинных генерациях — до **×2.7**
- Это не магия, а архитектура Qwen. На H100 выигрыш меньше, на «узком» consumer-железе — **решающий**
</v-clicks>

<!--
MTP-головы — архитектурное решение Qwen. Decode на 3090 упирается в пропускную способность памяти,
поэтому спекулятивное декодирование даёт здесь больше, чем на H100.
-->

---
hideInToc: true
---

# 3090: что НЕ работает (честно)

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<v-clicks>
- **Нет нативного FP8** — Ampere, не Ada и не Hopper. Поэтому квантую в AWQ (INT4), а не FP8
- **NVLink-мосты не используются** — TP=2 работает по PCIe 4.0; для 27B этого достаточно (замерено)
- **24GB VRAM — потолок** — 256K контекст + 27B веса = постоянный расчёт «что влезает, а что нет»
</v-clicks>

<div class="hook-line">Я не собирал H100-кластер. Я собирал то, что было доступно и по карману — и этого хватило.</div>

<!--
Риторика «consumer GPU — это компромисс» верна, но компромисс посчитан:
нет FP8/NVLink, 24GB потолок — и при этом 1 млрд токенов/сутки.
-->

---
layout: section
title: "Как это реально запускать: GPUStack + vLLM"
---

<SectionCard kicker="Часть 2" title="Как запускать: GPUStack + vLLM" tone="orange" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
hideInToc: true
---

# Финальная архитектура

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

```mermaid
flowchart TB
  A["pi.dev / Cursor / Kilo Code"] --> LB["Балансировщик (Go, 400 строк)<br/>least-loaded · prefix-aware · failover"]
  LB --> R1["R1 · 2×3090<br/>vLLM TP=2 · MTP"]
  LB --> R2["R2 · 2×3090<br/>vLLM TP=2 · MTP"]
  LB --> R3["R3 · 2×3090<br/>vLLM TP=2 · MTP"]
  LB --> R4["R4 · 2×3090<br/>vLLM TP=2 · MTP"]
  A -.-> RAG["RAG-узел · 2×4070 Ti + 4×3060<br/>bge-m3 · reranker · dev"]
  R1 & R2 & R3 & R4 --> GS["GPUStack — auto-restart, monitoring"]
```

<!--
Клиенты — код-агенты. Балансировщик — 400 строк Go (часть 3).
Каждая реплика — 2×3090, TP=2, MTP, конфиг из этой части.
GPUStack управляет репликами и поднимает их после crash.
RAG-узел — отдельное железо: 4070 Ti и 3060 под bge-m3, reranker и dev.
-->

---
hideInToc: true
---

# Первый запуск: 18 tok/s

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

<div class="code-cap">vLLM 0.27.1, конфиг по умолчанию</div>

```bash
vllm serve Qwen3.8-27B-AWQ-MTP \
  --tensor-parallel-size 2
```

::right::

18 tok/s. TTFT 4.2s. «Работает, но это не то».

<v-clicks>
- **Не настроил MTP** — модель с MTP-головами гонялась в обычном режиме: 1 токен за итерацию
- **Не настроил KV-cache** — контекст 32K по умолчанию, 256K не заявлен
- **OMP_NUM_THREADS по умолчанию** — CPU-многопоточность создаёт overhead, а не ускорение
</v-clicks>

<!--
Все три ошибки — дефолты. Первый конфиг — baseline, и именно он показал, где боль.
-->

---
hideInToc: true
---

# Тюнинг: 4 итерации, по одной переменной

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

| Итерация | Что изменил | Результат |
|---|---|---|
| 1 | MTP: 3 спекулятивных токена | 18 → 45 tok/s (×2.5) |
| 2 | 256K контекст + max-num-seqs 2 | 256K влез: KV-cache съедает ~18GB |
| 3 | OMP_NUM_THREADS=1, без async scheduling | TTFT 4.2s → 1.8s |
| 4 | mamba-cache-mode align | +5 tok/s |

<v-clicks>
- **Итог: 18 → 75 tok/s (×4.2), контекст 32K → 256K.** Цена: параллельность 8 → 2 запроса — для агента ок, он генерирует последовательно
- **Crash:** MTP в vLLM 0.27.1 — wild write, vLLM умер на 3-й день. Лечится upgrade на 0.28.0
</v-clicks>

<!--
Каждая итерация — одна переменная, иначе не понять, что дало эффект.
max-num-seqs 2 — честный компромисс: жертвуем параллельностью ради 256K контекста.
2 недели на нестабильном 0.27.1 — потерянное время; версия рантайма — часть тюнинга.
-->

---
hideInToc: true
---

# Финальный конфиг

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

```bash
vllm serve Qwen3.8-27B-AWQ-MTP \
  --tensor-parallel-size 2 \
  --max-model-len 262144 \
  --max-num-seqs 2 \
  --speculative-config '{"method": "mtp",
    "num_speculative_tokens": 3}' \
  --mamba-cache-mode align \
  --disable-async-scheduling \
  --gpu-memory-utilization 0.92
# OMP_NUM_THREADS=1
```

::right::

<div class="num-cap">Что я НЕ делал (и почему)</div>

<v-clicks>
- **NVFP4** — не поддерживается на Ampere
- **TRT-LLM / TensorRT** — не нужны, vLLM достаточно
- **8 параллельных запросов** — для агента 2 достаточны; 8 — это жертва контекстом и TTFT ради throughput, который мне не нужен
</v-clicks>

<!--
Полный финальный конфиг — 4 параметра тюнинга + дефолты, которые важно не трогать.
NVFP4 и TRT-LLM из 0.28.0 — фичи Hopper/Blackwell, на Ampere бесполезны.
-->

---
layout: section
title: Цена и мораль
---

<SectionCard kicker="Часть 3" title="Цена и мораль" tone="pink" />

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

---
hideInToc: true
---

# NGINX не понимает LLM

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

::left::

<v-clicks>
- Round-robin — это как раздавать билеты в кино: кто пришёл, тот сел. Но LLM-запрос — не билет
- **LLM-запрос — это состояние (KV-cache).** Реплика с полным кэшем не «занята», она «дорогая»: каждый новый токен на ней стоит дороже
- NGINX — кондуктор в автобусе: знает, сколько людей в салоне, но не знает, кто едет 3 остановки, а кто — 30
</v-clicks>

::right::

<div class="num-cap">Мой роутер (Go, 400 строк)</div>

- **least-loaded** — минимальный active_seqs / max_seqs
- **prefix-aware** — тот же system prompt уже в кэше → туда
- **context-aware** — prompt > 100K → реплика с максимальным свободным KV-cache
- **failover** — 5s без ответа → убрать из пула, retry на другой

<!--
Round-robin «не сломан» — он просто отвечает на другой вопрос.
Ключевая мысль: балансировка LLM — про состояние (KV-cache), а не про соединения.
-->

---
hideInToc: true
---

# Бенчмарк: NGINX vs мой балансировщик

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

| Метрика | NGINX RR | Мой балансировщик |
|---|---:|---:|
| P50 latency | 2.1s | **1.4s** |
| P99 latency | 8.7s | **3.2s** |
| Throughput (tok/s, aggregate) | 180 | **210** |
| KV-cache hit rate | 12% | **34%** |
| Failover | 30s (timeout) | **5s** |

<div class="num-cap">P99 ниже в 2.7 раза, KV-cache hit rate выше почти в 3 раза — прямая работа prefix-aware routing · 400 строк Go, не 4000: для 30 реплик нужен K8s</div>

<!--
Failover 5s против 30s — разница между «сбоем» и «просто задержкой».
Prefix caching — «бесплатный» throughput: 12% → 34% hit rate без изменения железа.
-->

---
hideInToc: true
---

# Тономика: $3,200/год против $20–73K

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

| Параметр | Значение |
|---|---:|
| Железо (3×2×RTX 3090, б/у) | ~$4,200 (разово) |
| Электричество (6×350W, 24/7) | ~$1,800/год |
| Амортизация (3 года) | ~$1,400/год |
| **Итого** | **~$3,200/год** |
| API-эквивалент (blended $0.14–0.50/1M) | ~$20–73K/год |
| **1M токенов при пике** | **~$0.009** |
| **Payback** | **~1.5 месяца** |

<div class="num-cap">1 млрд токенов/сутки — пик (8–12 часов агентного кодинга); в среднем 300–500M/сутки. Пик определяет размер инфраструктуры, средний — экономику</div>

<!--
Цифры — для ядра фермы 6×3090 (замеры из блога); ферма с тех пор выросла до 8×3090 + RAG-узел.
Момент честности: «1 млрд» — это total (input + output), в агентных нагрузках доминирует input
(256K контекст, RAG, tool calls при генерации 1–5K). Prefill проходит на порядки быстрее decode.
-->

---
hideInToc: true
---

# Что я бы сделал по-другому

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<v-clicks>
1. **Железо:** 4×3090 (TP=4) вместо 3×(2×3090) — один узел проще. Но 1.4kW: блок питания не потянул
2. **Модель:** 3 кандидата вместо 12 — Qwen3.8, DeepSeek-V3.2, GLM-4.6; 3 дня до решения
3. **vLLM:** сразу 0.28.0 — 2 недели на нестабильном 0.27.1 это потерянное время
4. **Балансировщик:** не писал бы свой — GPUStack + NGINX; prefix-aware — 20% кода за ~5% gain
5. **Мониторинг:** Prometheus + Grafana с первого дня — 2 недели летал вслепую, crash на MTP нашёл по логам, а не по алерту
</v-clicks>

<!--
Это и есть «шоколад, который неприятно воняет»: каждый пункт — реальная ошибка с ценой.
Подчеркнуть: мониторинг — самая дешёвая и самая забытая вещь в списке.
-->

---
hideInToc: true
---

# Заключение

<div class="slidev-slide-number"><SlideCurrentNo /> / <SlidesTotal /></div>

<v-clicks>
- **1 млрд токенов в сутки — это не про железо.** Это про то, что я перестал быть пользователем API и стал оператором инфраструктуры
- Команда довольна: TTFT 1.8s, 75–100 tok/s на пользователя, 256K контекст, P99 3.2s, ~$0.009 за 1M токенов
- **Qwen — не Claude**, но для агентной нагрузки его хватает — и он на порядок дешевле API
</v-clicks>

<div class="hook-line">Это не конец, а checkpoint. Через 6 месяцев я это перепишу.</div>

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
