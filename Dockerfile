FROM python:3.11

COPY . /self

WORKDIR self

RUN pip install -r requirements.txt --upgrade

RUN PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-self python -m self install --with-deps chromium

CMD ["pytest"]