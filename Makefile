# define the name of the virtual environment directory
VENV := venv

all: venv run

venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 src/main.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

deploy: venv
	./$(VENV)/bin/python3 -m pycob.deploy

.PHONY: all venv run
