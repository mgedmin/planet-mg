BROWSER = xdg-open

.PHONY: all
all: .env/.deps cache log venus/planet.py

.PHONY: test
test: all
	.env/bin/python venus/runtests.py

.PHONY: test-js
test-js:
	(cd theme && python -m SimpleHTTPServer 8009) &
	$(BROWSER) http://localhost:8009/test.html

.PHONY: update
update: all
	@printf '\n\n--- %s update started\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log
	.env/bin/python venus/planet.py config.ini 2>&1 | tee -a log/update.log
	@printf '~~~ %s update done\n\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log

.PHONY: update-offline
update-offline: all
	@printf '\n\n--- %s offline update started\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log
	.env/bin/python venus/planet.py -o config.ini 2>&1 | tee -a log/update.log
	@printf '~~~ %s offline update done\n\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log

.PHONY: update-cron
update-cron: all
	@-git pull -q
	@printf '\n\n--- %s cron update started\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log
	@savelog -l -q -c 168 output/atom.xml >> log/update.log 2>&1
	@cp output/atom.xml.0 output/atom.xml >> log/update.log 2>&1
	@savelog -l -q -c 168 output/index.html >> log/update.log 2>&1
	@cp output/index.html.0 output/index.html >> log/update.log 2>&1
	@.env/bin/python venus/planet.py config.ini >> log/update.log 2>&1
	@printf '~~~ %s cron update done\n\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log

.PHONY: preview
preview: output/index.html
	$(BROWSER) output/index.html

.PHONY: live-preview
live-preview: output/index.html
	(cd output && python -m SimpleHTTPServer 8000) &
	$(BROWSER) http://localhost:8000/

# Implementation

.env:
	virtualenv $@

.env/.deps: .env requirements.txt
	.env/bin/pip install -r requirements.txt
	touch $@

cache:
	mkdir $@

log:
	mkdir $@

venus/planet.py:
	git submodule update --init

output/index.html:
	$(MAKE) update

