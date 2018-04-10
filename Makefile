coverage:
	pytest --cov-report html \
		--cov . \
		--cov-branch
