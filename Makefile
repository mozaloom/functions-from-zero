install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=calcCli --cov=mylib test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C,E1120 *.py

all: install lint test