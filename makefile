.PHONY: lint, commit

lint:
	poetry run pre-commit run --all-files

commit:
	poetry run cz commit
