import json
from io import StringIO


def ingest_json_to_ES(es, json_data_file, es_index_name) -> None:
    """
    Receive a json_data_file and ingest it to ES index
    """
    data_file = open(json_data_file, "r+")
    line = data_file.readline()
    # print(line)
    bulkInsert = StringIO()
    # print(bulkInsert)
    count = 0

    while line:
        bulkInsert.write(json.dumps({"index": {"_index": es_index_name}}))
        bulkInsert.write("\n")
        bulkInsert.write(line.strip())
        bulkInsert.write("\n")
        count += 1

        if count >= 500:
            es.bulk(body=bulkInsert.getvalue())
            # print(res)
            count = 0
            bulkInsert.close()
            bulkInsert = StringIO()

        line = data_file.readline()

    if count > 0:
        es.bulk(body=bulkInsert.getvalue())
        # print(res)
        count = 0
        bulkInsert.close()

    data_file.close()


def create_es_mapping(es_connection, index_name: str, mapping: dict) -> None:
    es_connection.indices.clear_cache(index=index_name, ignore_unavailable=True)
    es_connection.indices.delete(index=index_name, ignore_unavailable=True)
    es_connection.indices.create(index=index_name, body=mapping)


def run_es_ingestion(
    es_connection, index_name: str, mapping: dict, data_file: str, ingest: bool = True
):
    create_es_mapping(es_connection, index_name, mapping)

    if ingest:
        ingest_json_to_ES(es_connection, data_file, index_name)
