FROM python:3.11

COPY . /playwright

WORKDIR playwright

RUN pip install -r requirements.txt --upgrade

RUN PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-playwright python -m playwright install --with-deps chromium

CMD ["pytest"]