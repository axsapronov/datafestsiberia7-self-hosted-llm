# AGENTS.md

## Проект

Слайды для доклада **«Self-hosted LLM»** на конференции **Data Fest Siberia 7**
(10 октября 2026, Новосибирск, офис koronatech, ул. Николаева 12/1).
Доклад — на русском языке, аудитория — data scientists / ML-инженеры.

## Стек

- **Slidev** (v52+) — Markdown-слайды на Vite + Vue 3 + UnoCSS
- Node.js >= 20.12.0
- Пакет-менеджер: pnpm (также работают npm/yarn)

## Команды

```bash
pnpm install      # установка зависимостей
pnpm run dev      # dev-сервер, http://localhost:3030
pnpm run build    # сборка статического SPA (dist/)
pnpm run export   # экспорт в PDF (нужен playwright-chromium)
pnpm format       # форматирование slides.md
```

Экспорт PDF: `pnpm add -D playwright-chromium`, затем `pnpm run export`.
Результат — PDF в корне проекта (не коммитится).

## Структура

```
slides.md          # главный файл слайдов (точка входа)
components/        # кастомные Vue-компоненты
layouts/           # кастомные layout-ы
public/            # статические ассеты (картинки и т.п.)
snippets/          # кодовые сниппеты для импорта в слайды
styles/            # глобальные стили (index.css)
vite.config.ts     # расширение конфигурации Vite
```

## Правила работы со слайдами

- Разделитель слайдов — строка `---` в начале строки.
- Первый frontmatter файла (headmatter) — настройки всего дека
  (`theme`, `title`, `info` и т.д.).
- Frontmatter каждого слайда — настройки слайда (`layout`, `clicksNoNav`,
  `transition` и т.д.).
- Заметки докладчика — в HTML-комментариях `<!-- ... -->` в конце слайда.
- Язык контента — русский; код, команды, термины — без перевода.
- Использовать встроенные layout-ы: `cover`, `section`, `two-cols`,
  `image-left/right`, `quote`, `center` и др. Кастомные layout-ы — только
  при явной необходимости, в `layouts/`.
- Анимации: `v-click` / `<v-clicks>` для поэлементного показа;
  подчёркивание — `v-mark.underline`.
- Код: блоки с подсветкой ```` ```lang ````, подсветка строк `{2,3}`,
  повторное показ по клику `{1|2-3}`; длинные сниппеты выносить в
  `snippets/` и импортировать `<<< @/snippets/file.py`.
- Диаграммы — `mermaid`, формулы — KaTeX.
- Слайды — короткие и читаемые: минимум текста на слайд,
  16:9 (960×540). Не переполнять слайд — лучше разбить на два.

## Проверка

1. `pnpm run dev` — проверить, что все слайды рендерятся в
   http://localhost:3030, анимации и layout-ы работают.
2. `pnpm run export` — убедиться, что PDF собирается без ошибок
   (финальная проверка перед конференцией).

## AI-инструменты

- MCP-сервер Slidev доступен на `http://localhost:3030/__mcp`
  (когда запущен dev-сервер) — для просмотра и навигации по слайдам.
- Официальный skill: `npx skills add slidevjs/slidev`.
- Документация: https://sli.dev (syntax guide, layouts, exporting).

## Чего не делать

- Не коммитить `node_modules/`, `dist/`, `*.local`, `components.d.ts`
  (см. `.gitignore`).
- Не менять тему без согласования — тема фиксируется в headmatter.
- Не удалять заметки докладчика — они нужны на выступлении.
