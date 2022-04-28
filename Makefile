lint-Python:
	pylint --rcfile=.pylintrc Python/

lint-algorithms_and_data_structure:
	pylint --rcfile=.pylintrc algorithms_and_data_structure/

test-unittests:
	@cd Python; python -m pytest -vv

test-algorithms_and_data_structure:
	@cd algorithms_and_data_structure; python -m pytest -vv
