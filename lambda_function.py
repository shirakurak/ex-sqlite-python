import json
import sqlite3

def lambda_handler(event, context):
    try:
        items = event['multiValueQueryStringParameters']['item_numbers']
        placeholders = ','.join(['?' for _ in items])
        query = f"SELECT col1, col2, col3 FROM more WHERE col1 IN ({placeholders})"

        with sqlite3.connect('data/test.db') as conn:
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute(query, items)
            rows = c.fetchall()
            result = [dict(row) for row in rows]

        return {
            'statusCode': 200,
            'body': result
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
