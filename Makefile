.PHONY: run test

run:
	cd backend && .venv/bin/python src/app/main.py

test:
	cd backend && .venv/bin/py.test