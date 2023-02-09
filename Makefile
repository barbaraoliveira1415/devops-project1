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
deploy:
	#deploy