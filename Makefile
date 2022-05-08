COMPOSE ?= docker-compose -f database/docker-compose.yml

run: build
	$(COMPOSE) up -d

build:
	$(COMPOSE) build

rm:
	$(COMPOSE) stop
	$(COMPOSE) rm -f

copy_csv:
	@docker cp database/csv_tables/ database-db-1:/usr/src/csv_tables
	@echo "Copy is done"

lint-Python:
	pylint --rcfile=.pylintrc Python/

lint-algorithms_and_data_structure:
	pylint --rcfile=.pylintrc algorithms_and_data_structure/

test-unittests:
	@cd Python; python -m pytest -vv

test-algorithms_and_data_structure:
	@cd algorithms_and_data_structure; python -m pytest -vv
