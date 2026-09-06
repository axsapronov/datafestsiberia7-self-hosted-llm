.PHONY: install run build pdf pptx check clean

install:
	pnpm install
	pnpm add -D playwright-chromium

run:
	pnpm run dev

build: pdf pptx

pdf:
	pnpm run export

pptx:
	pnpm run export --formats pptx

check:
	pnpm run format

clean:
	rm -rf dist *.pdf *.pptx
