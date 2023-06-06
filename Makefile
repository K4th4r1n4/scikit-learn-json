# define name of virtual environment directory
SRC := scikit_learn_json
VENV := env

# different definitions for Windows and Linux
ifeq ($(OS), Windows_NT)
PYTHON := py.exe
PYENV := $(VENV)/Scripts/python.exe
else
PYTHON := python3
PYENV := $(VENV)/bin/$(PYTHON)
endif


my_debug:
	@echo "==== $(OS) ===="
	@echo "python: $(PYTHON)"
	@echo "pyenv: $(PYENV)"


all: venv lint test


venv:
	$(PYTHON) -m venv $(VENV)
	./$(PYENV) -m pip install .


lint:
	./$(PYENV) -m pip install '.[lint]'
	./$(PYENV) -m black $(SRC) --check --diff
	./$(PYENV) -m mypy $(SRC) --ignore-missing-imports
	./$(PYENV) -m flake8 $(SRC)
	./$(PYENV) -m isort $(SRC) --check-only --profile black -l=79 --diff


test:
	./$(PYENV) -m pip install '.[test]'
	./$(PYENV) -m coverage run --source $(SRC) -m pytest tests
	./$(PYENV) -m coverage report
	./$(PYENV) -m coverage xml


clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
