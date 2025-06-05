# Playwright Python Example

This project contains UI and API tests for the [DemoQA](https://demoqa.com) QA training platform. Tests are written with [Pytest](https://docs.pytest.org/) and use [Playwright](https://playwright.dev/python/) for browser automation and API requests.

## Setup

1. Clone this repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies and Playwright browsers:
   ```bash
   pip install -r requirements.txt
   playwright install --with-deps
   ```
4. Copy `.env.example` to `.env` and adjust the `DOMAIN` variable if needed.

## Running tests

To run all tests use `pytest`:

```bash
pytest
```

You can run specific test types using markers:

```bash
pytest -m ui    # run UI tests only
pytest -m api   # run API tests only
```

The provided `Makefile` offers shortcuts:

```bash
make install   # install dependencies
make test      # run tests and generate reports
```

### Reports

After running `make test` reports are stored in the `reports` directory (HTML under `reports/html` and JUnit XML under `reports/xml`).

## Docker

A `Dockerfile` is available to execute the tests inside a container:

```bash
docker build -t playwright-tests .
docker run --rm playwright-tests
```
