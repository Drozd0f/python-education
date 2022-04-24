lint:
	pylint --rcfile=.pylintrc Python/

test-unittests:
	@cd Python; python -m pytest -vv
