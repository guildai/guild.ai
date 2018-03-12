grunt = node_modules/.bin/grunt
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

stage: build-and-index
	cp now.json.in site/now.json
	cd site && now deploy && now alias www-staging.guild.ai

promote-staging:
	target=`now alias ls | grep www-staging.guild.ai | cut -d' ' -f3` \
	  && now alias set $$target www.guild.ai

clean-staging:
	now rm www-guild-ai -sy

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

clean-caches:
	rm -rf /tmp/guild-ai-cmd-help
