install:
	pip install -r requirements.txt

test-ui:
	pytest --headed tests/ui_tests/ --base-url https://demoqa.com

test-api:
	pytest tests/api_tests/ --base-url https://demoqa.com

test-report-xml:
	pytest --junitxml=report.xml --base-url https://demoqa.com