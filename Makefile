.PHONY: format
format:
	ruff format .

.PHONY: lint-fix
lint-fix:
	ruff check --fix .

.PHONY: format-check
format-check:
	ruff format --check .

.PHONY: lint
lint:
	ruff check  --output-format=github .

.PHONY: format-html
format-html:
	djlint --configuration=.djlintrc --reformat .

.PHONY: check-html
check-html:
	djlint --configuration=.djlintrc --check .

.PHONY: tidy
tidy:
	$(MAKE) format
	$(MAKE) lint-fix
	$(MAKE) format-html

.PHONY: test
test:
	pytest -vv
