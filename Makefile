HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
	print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
	@{$$help{$$_}},"\n" for keys %help;

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command. Use 'make help' for list of commands."
else
MESSAGE = "Done"
endif

env: ##@Environment Activate Poetry shell for backend
	poetry shell

up:  ##@Docker Start docker-compose services
	docker-compose up -d  

down:  ##@Docker Stop docker-compose services
	docker-compose down

rebuild: ##@Docker Rebuild and restart services
	docker-compose down && docker-compose up -d --build

backend_up: ##@Environment Start backend server
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000

help: ##@Help Show this help 
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

%::
	@echo $(MESSAGE)

.PHONY: env deactivate help