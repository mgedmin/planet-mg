.PHONY: all
all: .env cache log

.PHONY: test
test: .env
	.env/bin/python venus/runtests.py

.PHONY: update
update: .env log
	@printf '\n\n--- %s update started\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log
	.env/bin/python venus/planet.py config.ini 2>&1 | tee -a log/update.log
	@printf '~~~ %s update done\n\n' "$$(date +'%Y-%m-%d %H:%M:%S')" >> log/update.log

# Implementation

.env:
	virtualenv $@

cache:
	mkdir $@

log:
	mkdir $@
