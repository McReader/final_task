# RSS reader

Pure Python command-line RSS reader.

## Usage

```
rss_reader [-h] [--version] [--json]
                [--verbose] [--limit LIMIT]
                [--date DATE]
                [--to-html TO_HTML | --to-fb2 TO_FB2]
                [source]

Pure Python command-line RSS reader.

positional arguments:
  source             RSS URL

options:
  -h, --help         show this help message and exit
  --version          Print version info
  --json             Print result as JSON in stdout
  --verbose          Outputs verbose status messages
  --limit LIMIT      Limit news topics if this
                     parameter provided
  --date DATE        Read articles starting from
                     this date. The following format
                     should be used yyyymmdd (e.g 20191206)
  --to-html TO_HTML  Export news to .html file
  --to-fb2 TO_FB2    Export news to .fb2 file
```

## Offline Mode

To fetch the feed without an internet connection, you may use `--date` param.

```bash
rss_reader https://news.yahoo.com/rss/ --date 20191206
```

This command will return all the cached news published from the specified date. The util
throws an error if no entries found in the cache

It is possible to omit source url, if the `--date` option is used. In that case all cached news from all the sources will be returned

```bash
rss_reader --date 20191206
```

## Export

Either `--to-html` or `--to-fb2` options should be used to export the results of the util.

```
rss_reader https://news.yahoo.com/rss/ --to-html=test.html # for HTML export

rss_reader https://news.yahoo.com/rss/ --to-fb2=test.fb2 # for FB2 export
```

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
