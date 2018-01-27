grunt = node_modules/.bin/grunt

build: $(grunt)
	$(grunt) build

serve: $(grunt)
	$(grunt) serve

watch: $(grunt)
	$(grunt) watch

clean: $(grunt)
	$(grunt) clean

$(grunt):
	npm install
