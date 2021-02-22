from elasticsearch import Elasticsearch

from mhs_poc.config.settings import ELASTICSEARCH_CONFIG

# To-do: This can be a class
ES_CONNECTION = Elasticsearch(
    [ELASTICSEARCH_CONFIG["host"]],
    http_auth=(ELASTICSEARCH_CONFIG["username"], ELASTICSEARCH_CONFIG["password"]),
    schema="http",
    port=ELASTICSEARCH_CONFIG["port"],
    timeout=60,
)
