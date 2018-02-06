grunt = node_modules/.bin/grunt

build: $(grunt)
	$(grunt) build

.PHONY: site

site:
	$(grunt) exec:site

index: $(grunt)
	$(grunt) index

build-and-index: $(grunt)
	$(grunt) build-and-index

serve: $(grunt)
	$(grunt) serve

watch: $(grunt)
	$(grunt) watch

clean: $(grunt)
	$(grunt) clean

$(grunt):
	npm install

test-custom:
	python custom.py

spellcheck:
	find pages -iregex '.*\.md$$' -exec aspell -l en --home-dir . -x check '{}' \;
