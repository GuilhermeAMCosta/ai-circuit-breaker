PYTHONPATH := $(shell pwd)

run:
	@PYTHONPATH="${PYTHONPATH}" python ./app/main.py