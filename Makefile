grunt = node_modules/.bin/grunt
now = /usr/local/bin/now
now_redirect = /usr/local/bin/now-redirect

mkdocs = PYTHONPATH=. mkdocs

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

stage: build-and-index $(now)
	cp now.json.in site/now.json
	cd site && $(now) deploy && $(now) alias www-staging.guild.ai

promote-staging: $(now)
	target=`$(now) alias ls | grep www-staging.guild.ai | cut -d' ' -f3` \
	  && $(now) alias set $$target www.guild.ai

ensure-redirect: $(now) $(now_redirect)
	$(now-redirect) www.guild.ai && $(now) alias guild.ai

$(now):
	@echo -n "This operation requires now. "
	@echo "Install it using 'npm install -g now'."

$(now):
	@echo -n "This operation requires now-reirect. "
	@echo "Install it using 'npm install -g now-redirect'."

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
	find pages -iregex '.*\.md$$' \
	  -exec aspell -l en --home-dir . -x check '{}' \;

clean-caches:
	rm -rf /tmp/guild-ai-cmd-help
