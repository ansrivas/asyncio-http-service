.DEFAULT_GOAL := help

help:          ## Show available options with this Makefile
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: clean
clean:         ## Clean the docker-container etc.
clean:
	docker-compose down -v && \
	docker rmi ansrivas/aiohttp-postgres:9.6

.PHONY : test
test:          ## Run all the tests
test:
	python setup.py test


.PHONY : prepare_dev
prepare_dev:   ## Install the application in current environment
prepare_dev:
	python setup.py develop
	docker-compose down -v ; \
	docker rmi ansrivas/aiohttp-postgres:9.6 ;\
	docker-compose up -d


.PHONY : dev_run
dev_run:	     ## Run application in a dev mode, where gunicorn workers will reload the application on every change.
dev_run:	prepare_dev
	gunicorn 'app.main:app' --env config_file=`pwd`/config/config.yaml --workers=8 --bind localhost:8000 --worker-class aiohttp.GunicornWebWorker --reload
