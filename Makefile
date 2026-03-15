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

backend_up: ##@Environment Start backend server
	poetry run uvicorn main:app --host 0.0.0.0 --port 8000

help: ##@Help Show this help 
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

clean: ##@Code Remove Python cache files and directories
	@echo "Cleaning Python cache files..."
	@echo "Removing __pycache__ directories with sudo..."
	@for dir in $$(find . -type d -name "__pycache__"); do \
		echo "Removing: $$dir"; \
		sudo rm -rf "$$dir"; \
	done
	@echo "Python cache cleaned!"

%::
	@echo $(MESSAGE)

.PHONY: env deactivate help clean backend_up