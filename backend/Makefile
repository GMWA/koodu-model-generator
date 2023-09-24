.DEFAULT_GOAL=help

CONFIG_FILE=./.env
VENVPATH=venv
PYTHON=$(VENVPATH)/bin/python3
UVICORN=$(VENVPATH)/bin/uvicorn

##venv: setUp the virtualenv (this step is integrated with the instal-xxx target
venv: $(VENVPATH)/bin/activate
$(VENVPATH)/bin/activate: requirements.txt
	test -d $(VENVPATH) || python3 -m venv $(VENVPATH); \
	. $(VENVPATH)/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt; \
	touch $(VENVPATH)/bin/activate;

$(CONFIG_FILE):
	echo "> Adding config file..."
	cp .env.example $(CONFIG_FILE)

##install-deps: setup your prod environment
install-deps: venv $(CONFIG_FILE)

##run: run the api locally
run: install-deps
	$(UVICORN) modelgenerator.server:app --reload

##docker-build: using docker to build the back image
docker-build:
	docker build --tag modelgenerator_back:latest -f Dockerfile .

##docker-run: using docker to run the back image
docker-run: docker-build
	docker run -ti -p 8000:8000 -v data:/app/data --rm modelgenerator_back:latest

##clean: clean the virtualenv
clean:
	rm -rf $(VENVPATH)

##help: show help
help : Makefile
	@sed -n 's/^##//p' $<

.PHONY : help venv install-deps lint docker-run docker-build run clean