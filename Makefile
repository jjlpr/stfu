venv:
	virtualenv venv --python=python3
	venv/bin/pip install -U pip

venv/bin/pip-compile: venv
venv/bin/pip-sync: venv
	venv/bin/pip install pip-tools

.PHONY: install
install: venv venv/bin/pip-sync soundfiles output.json
	venv/bin/pip-sync requirements/base.txt

.PHONY: install-test
install-test: venv venv/bin/pip-sync
	venv/bin/pip-sync requirements/test.txt

output.json:
	touch output.json

soundfiles:
	mkdir soundfiles
