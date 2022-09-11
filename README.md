# RSS reader

Pure Python command-line RSS reader.

## Testing

To run the tests you need to execute the following command

```bash
python -m unittest discover -s src -p '*_test.py'
```

Coverage is analysed using [coverage](https://pypi.org/project/coverage/) package. To run tests with coverage report, use

```bash
python -m coverage run -m unittest discover -s src -p '*_test.py'
```

To print the report to the terminal, use

```bash
python -m coverage report
```
