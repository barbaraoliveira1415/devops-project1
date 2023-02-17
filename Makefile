install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py #format these two locations
lint: 
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py #ignore warnings every python file
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build containers
	docker build -t deploy-fastapi .
run:
	docker run -p 127.0.0.1:8080:8080 7e66137da068
deploy:
	#deploy
all: install lint test deploy