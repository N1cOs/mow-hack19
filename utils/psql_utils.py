import csv
import os
import psycopg2
import psycopg2.extensions
from psycopg2.extras import execute_batch


psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

PSQL_CONNECT = "host=localhost user=gleb password=gleb2357 dbname=items"

INSERT_REGION = "INSERT INTO region VALUES (%d, %s)"

REGIONS_CSV_PATH = os.path.join(os.path.dirname(__file__), 'regions.csv')


def get_regions():
    batch_size = 50
    with open(REGIONS_CSV_PATH) as csv_file:
        reader = csv.reader(csv_file)
        next(reader) # skip header
        batch = []
        for line in reader:
            batch.append(line)
            if len(batch) == batch_size:
                yield batch
                batch.clear()
        if len(batch) != 0:
            yield batch


def insert_regions():
    with psycopg2.connect(PSQL_CONNECT) as conn:
        with conn.cursor() as curs:
            for batch_of_records in get_regions():
                execute_batch(curs, INSERT_REGION, batch_of_records)
