grunt = node_modules/.bin/grunt
mkdocs = ./mkdocs

site: refresh-assets
	$(mkdocs) build

.PHONY: dist

dist: $(grunt)
	$(grunt) dist

$(grunt):
	npm install

serve: site
	$(mkdocs) serve

watch-assets: $(grunt) refresh-assets
	$(grunt) watch

refresh-assets: $(grunt)
	$(grunt) dev

clean:
	rm -rf dist site
