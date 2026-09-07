// Единый источник данных для слайдов «Проблемы» и «Идеи» каждого этапа.
// Палитра параметров совпадает с public/img/user-expectations.svg.

export type ParamId = 'speed' | 'context' | 'volume' | 'quality' | 'api' | 'manage'

export interface Param {
  id: ParamId
  label: string
  color: string
  expected: string
}

export const PARAMS: Record<ParamId, Param> = {
  speed: { id: 'speed', label: 'СКОРОСТЬ', color: '#3b82f6', expected: '80–100 ток/сек' },
  context: { id: 'context', label: 'КОНТЕКСТ', color: '#8b5cf6', expected: '256k токенов' },
  volume: { id: 'volume', label: 'ОБЪЁМ', color: '#ec4899', expected: '50M токенов/сутки на чел.' },
  quality: { id: 'quality', label: 'КАЧЕСТВО', color: '#10b981', expected: '≥ Claude 3.5 Sonnet' },
  api: { id: 'api', label: 'API', color: '#f59e0b', expected: 'OpenAI / Anthropic' },
  manage: { id: 'manage', label: 'УПРАВЛЕНИЕ', color: '#0ea5e9', expected: 'Статистика и управление доступами' },
}

export const PARAM_ORDER: ParamId[] = ['speed', 'context', 'volume', 'quality', 'api', 'manage']

export type Status = 'ok' | 'warn' | 'bad'

export interface ProblemRow {
  param: ParamId
  actual: string
  status: Status
  note?: string
}

export interface StageFeature {
  title: string
  value?: string
  text: string
}

export interface IdeaItem {
  num: string
  title: string
  text: string
  params?: ParamId[]
  feature?: string
}

export interface StageData {
  name: string
  problems: ProblemRow[]
  features: StageFeature[]
  ideas: IdeaItem[]
}

export const STAGES: Record<'s1' | 's2' | 's3', StageData> = {
  s1: {
    name: 'M40 + Ollama',
    problems: [
      { param: 'speed', actual: '10–20 ток/сек', status: 'bad' },
      { param: 'context', actual: '4k-32k (дефолт Ollama)', status: 'bad' },
      { param: 'volume', actual: '1 пользователь, всё очень долго', status: 'bad' },
      { param: 'quality', actual: 'Непонятно', status: 'bad' },
      { param: 'api', actual: 'Ollama API (OpenAI-совместимый)', status: 'warn' },
      { param: 'manage', actual: 'Урезанная статистика и доступы', status: 'bad' },
    ],
    features: [
      { title: 'Шум · Telsa M40', value: '250W', text: 'вентилятор на 100% под нагрузкой, NVIDIA уже не поддерживает' },
      { title: 'Холодный старт', value: 'keep_alive 5m', text: 'модель выгружается из VRAM спустя 5 минут, по-умолчанию' },
      { title: 'Не production', value: '', text: 'тяжело организовать доступ по ключам, без доступа через VPN' },
    ],
    ideas: [
      { num: '01', title: 'Отказаться от Tesla M40', text: 'запустить серверы с RTX 3060/4070 Ti', feature: 'шум' },
      { num: '02', title: 'Заменить ollama на llama.cpp', text: 'больше инструкций, больше опыта, меньше посредников', params: ['volume', 'speed'] },
      { num: '03', title: 'Объединить серверы в Proxmox кластер', text: 'централизованный контроль за RAM, VRAM, SSD ', feature: 'надёжность' },
      { num: '04', title: 'Настроить оркестратор', text: 'статистика, управление пользователям, API-ключам', params: ['manage'] },

    ],
  },
  // TODO(спикер): весь блок S2 — данные не собраны (в деке цифр нет). Заполнить до финального экспорта.
  s2: {
    name: '3060/4070 Ti + llama.cpp',
    problems: [
      { param: 'speed', actual: '50-70 ток/сек', status: 'warn' },
      { param: 'context', actual: '32-64k', status: 'bad' },
      { param: 'volume', actual: '2-3 пользователя, но тормоза', status: 'bad' },
      { param: 'quality', actual: 'Не ясно как подобрать модель', status: 'warn' },
      { param: 'api', actual: 'OpenAI-совместимый', status: 'ok' },
      { param: 'manage', actual: 'GPUStack', status: 'ok' },
    ],
    features: [
      { title: 'Модели еле влезают', value: '', text: 'RAM помогает запихать модель' },
      { title: '2-3 пользователя — предел', value: '', text: 'не хватает пропускной способности' },
      { title: 'GPUStack — унификация', value: '', text: 'ключи, статистика, модели через UI' },
    ],
    ideas: [
      { num: '01', title: 'Перейти на пары RTX 3090', text: 'Это даст 48 GB VRAM' },
      { num: '02', title: 'Заменить llama.cpp на vLLM', text: 'Движок адаптирован под production нагрузку' },
      { num: '03', title: 'Подобрать версию модели под железо', text: 'Изучить виды квантизации, особенности алгоритмов' },
      { num: '04', title: 'Настроить контроль температура-мощность', text: 'Написать демона, который сам будет следить за перегревом' },
      { num: '05', title: 'Написать свой балансировщик', text: 'sticky session + prefix-aware', },
      { num: '06', title: 'Встроить ИИ в рабочий процесс', text: 'CI review, SDLC, RAG',},
    ],
  },
  s3: {
    name: '8×3090 + vLLM + GPUStack',
    problems: [
      { param: 'speed', actual: '80-100 ток/сек на пользователя', status: 'ok' },
      { param: 'context', actual: '256K (262144)', status: 'ok' },
      { param: 'volume', actual: '1 млрд токенов/сутки (пик), 600-750M в среднем', status: 'ok' },
      { param: 'quality', actual: 'Qwen3.8: Terminal-Bench 73, DeepSWE 42.2', status: 'ok' },
      { param: 'api', actual: 'GPUStack — OpenAI-совместимый', status: 'ok' },
      { param: 'manage', actual: 'GPUStack: счётчики по пользователям и API-ключам', status: 'ok' },
    ],
    features: [
      { title: 'MTP crash', value: 'vLLM 0.27.1', text: 'wild write, рантайм умер на 3-й день — лечится 0.28.0' },
      { title: 'Нет FP8', value: 'Ampere', text: 'квант — AWQ (INT4), а не FP8' },
      { title: '24GB — потолок', value: 'max-num-seqs 2', text: '256K + 27B весов: параллельность 8 → 2 запроса' },
    ],
    ideas: [
      { num: '01', title: 'MTP: 3 спекулятивных токена', text: '18 → 45 tok/s (×2.5) на 3090', params: ['speed'] },
      { num: '02', title: '256K контекст', text: '--max-model-len 262144, KV-cache ~18GB', params: ['context'] },
      { num: '03', title: 'OMP_NUM_THREADS=1, без async scheduling', text: 'TTFT 4.2s → 1.8s', params: ['speed'] },
      { num: '04', title: 'vLLM 0.28.0', text: 'фикс MTP crash — стабильность 24/7', feature: 'особенность · надёжность' },

      { num: '06', title: 'мониторинг с первого дня', text: 'Prometheus + Grafana + GPUStack: алерты, а не логи', params: ['manage'] },
    ],
  },
}
