install:
	pip install -r requirements.txt

test:
	pytest --junitxml=reports/xml/report.xml --template=html1/index.html --report=reports/html/report.html --base-url https://demoqa.com

test-ui:
	pytest --headed tests/ui_tests/ --base-url https://demoqa.com

test-api:
	pytest tests/api_tests/ --base-url https://demoqa.com

test-report-xml:
	pytest --junitxml=reports/report.xml --base-url https://demoqa.com