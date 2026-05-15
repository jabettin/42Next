EXERCISES	:= $(wildcard ex*)
PY_FILES	:= $(foreach d, $(EXERCISES), $(wildcard $(d)/*.py))

.PHONY: all flake8 mypy $(EXERCISES) clean

all: flake8 mypy

flake8:
	@echo "=== flake8 ==="
	@flake8 --max-line-length=79 $(PY_FILES) && echo "OK"

mypy:
	@echo "=== mypy ==="
	@mypy --strict $(PY_FILES) && echo "OK"

$(EXERCISES):
	@echo "=== $@ ==="
	@flake8 --max-line-length=79 $(wildcard $@/*.py) && \
	 mypy --strict $(wildcard $@/*.py) && echo "OK"

clean:
	@rm -rf .mypy_cache __pycache__ $(addsuffix /__pycache__, $(EXERCISES))
