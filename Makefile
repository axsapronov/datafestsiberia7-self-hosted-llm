.PHONY: install run build pdf pptx check clean

install:
	pnpm install
	pnpm add -D playwright-chromium

run: img
	pnpm run dev

build: img pdf pptx

pdf:
	pnpm run export

pptx:
	pnpm run export --format pptx

check:
	pnpm run format

clean:
	rm -rf dist *.pdf *.pptx slides-export.pptx

img:
	uv run python setup/gen_ai_spend_chart.py
