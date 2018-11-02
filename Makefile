grunt = node_modules/grunt/bin/grunt

mkdocs = PYTHONPATH=.:../guild mkdocs

build: $(grunt)
	$(grunt) build

.PHONY: site

site:
	$(grunt) exec:site

site-pdb-support:
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
	PYTHONPATH=guild python custom.py

spellcheck:
	find pages -iregex '.*\.md$$' \
	  -exec aspell -l en --home-dir . -x check '{}' \;

clean-caches:
	rm -rf /tmp/guild-ai-cmd-help

update-submodules:
	git submodule foreach git pull origin master

lint:
	PYTHONPATH=guild pylint -rn -f parseable *.py
