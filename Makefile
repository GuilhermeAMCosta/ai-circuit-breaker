BASE_DIR := app
PYTHONPATH := $(shell pwd)

run:
	@PYTHONPATH="${PYTHONPATH}" python ${BASE_DIR}/main.py
