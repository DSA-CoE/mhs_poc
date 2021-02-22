from _ingest_es_helper import run_es_ingestion
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch

from mhs_poc.config.settings import ELASTICSEARCH_CONFIG

ingest_config = {
    # Example index config
    # 'index_name': {
    #     'index_name': 'es_ploutos',
    #     'index_mapping': {
    #         "mappings": {
    #             "properties": {
    #                 "location": {"type": "keyword"},
    #                 "year": {"type": "short"},
    #                 "month": {"type": "short"},
    #                 "category": {"type": "keyword"},
    #                 "approved_allocation": {"type": "float"},
    #                 "revised_allocation": {"type": "float"},
    #                 "actual_expenditure": {"type": "float"},
    #                 "utilisation_pct": {"type": "float"}
    #             }
    #         }
    #     },
    #     'index_data_file': './_data/ingest.json'
    # }
}


class Command(BaseCommand):
    help = "Build ES mapping and ingest data"

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument(
            "-i", "--index", type=str, help="Index to be built and ingested"
        )

    def handle(self, *args, **kwargs):
        index = kwargs["index"]

        ES_CONNECTION = Elasticsearch(
            [ELASTICSEARCH_CONFIG["host"]],
            http_auth=(
                ELASTICSEARCH_CONFIG["username"],
                ELASTICSEARCH_CONFIG["password"],
            ),
            schema="http",
            port=ELASTICSEARCH_CONFIG["port"],
            timeout=60,
        )
        time = "111"
        self.stdout.write("It's now %s" % time)

        if index:
            index_config = ingest_config.get(index, None)

            if index_config is None:
                self.stderr.write("Index name not found in ingest_config!")
                return

            self.stdout.write("Ingesting %s data to ES..." % index)

            run_es_ingestion(
                ES_CONNECTION,
                index_name=index,
                index_mapping=index_config["index_mapping"],
                data_file=index_config["index_data_file"],
            )

            self.stdout.write("Done")

        else:
            for index_val in ingest_config:
                index_config = ingest_config.get(index_val, None)

                self.stdout.write("Ingesting %s data to ES..." % index_val)

                run_es_ingestion(
                    ES_CONNECTION,
                    index_name=index_val,
                    index_mapping=index_config["index_mapping"],
                    data_file=index_config["index_data_file"],
                )
