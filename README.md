# ex-sqlite-python

An example of searching for data in an SQLite database in response to a request

## request

This is a sample.

```json
{
  "body": "eyJ0ZXN0IjoiYm9keSJ9",
  "resource": "/{proxy+}",
  "path": "/path/to/resource",
  "httpMethod": "POST",
  "isBase64Encoded": true,
  "queryStringParameters": {
    "item_no1": "1",
    "item_no2": "2",
    "item_no3": "3"
  },
  "multiValueQueryStringParameters": {
    "item_numbers": [
      "4",
      "5",
      "6"
    ]
  },
  ...
```

## Sqlite DB

```sh
# On your local machine, create a 'data' directory and then:
$ sqlite3 data/test.db
SQLite version 3.39.5 2022-10-14 20:58:05
Enter ".help" for usage hints.
sqlite> .database
main: /Users/kenichi-shirakura/data/test.db r/w
sqlite> .table
sqlite> CREATE TABLE test (col1 int, col2 text, col3 text);
sqlite> .table
more
sqlite> INSERT INTO test VALUES (1, '1_aaa', '1_bbb');
sqlite> INSERT INTO test VALUES (2, '2_aaa', '2_bbb');
sqlite> select * from test;
1|1_aaa|1_bbb
2|2_aaa|2_bbb
sqlite>
```

## Runtime

Note that in lambda_function.lambda_handler, the executable file name and the function to be executed are already determined.

Create a zip file with the following command and upload it to Lambda to test the function:

```sh
zip -r my-deployment-package.zip lambda_function.py data/test.db
```
