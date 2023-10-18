# self-python
python/self testing framework

## setup
- clone repo
- create python virtual environment: `python -m venv venv`
- activate environment: `source venv/bin/activate`

## run tests
- install requirements: `pip install -r requierements.txt`
- run tests: `pytest`

## Alternative way of running tests
- `make install`
- `make test`,  `make-test-ui` etc. (see [Makefile](./Makefile))

## misc
- after running `make test` reports will be generated under [reports](./reports) folder