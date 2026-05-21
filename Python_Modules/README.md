`This project is part of the 42 curriculum`

## General information ##
>It is important to note that the subject files attached to their subjects, respectively. Are not in sync with your subject file.
>
>_As 42Next is still in it's formative time, the possibility of subject files being updated or reworked is high_

## Instructions ##
>Within the root of this repository sits a Makefile which contains a script for mypy and flake8.
>
>To use this Makefile, copy it from the root repository into your current working directory and run `make`.
>
>This will execute mypy and flake8 on all the .py files within your current working directory
>
>To clean up the newly created mypy instance, run: `make clean`




```make
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