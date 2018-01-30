grunt = node_modules/.bin/grunt
mkdocs = PYTHONPATH=. mkdocs

build: $(grunt)
	$(grunt) build

.PHONY: site

site:
	$(mkdocs) build

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
