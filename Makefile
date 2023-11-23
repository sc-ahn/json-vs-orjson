MAKEFLAGS += --silent
path := .

.PHONY: help
help: ## what you are looking at
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

.PHONY: local-test
local-test: ## run tests locally
	@echo "Running tests locally"
	@poetry run pytest --log-cli-level=INFO

.PHONY: test
test: ## build docker image and run tests
	@echo "Building docker image"
	@docker build -t json-vs-orjson .
	@echo run image
	@docker run --rm -v .:/json-vs-orjson -it json-vs-orjson

.PHONY: report
report: ## generate report
	@echo "Starting report server"
	@poetry run python -m http.server --directory . 8888