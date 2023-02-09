install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py #format these two locations
lint: 
	#flake8 or #pylint
test:
	#test
deploy:
	#deploy