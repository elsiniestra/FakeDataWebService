from typing import NoReturn

from src.apps.data_schemas.services import CSVDataSet
from src.apps.data_schemas.models import DataSet
from src.config.core.celery import celery_app


@celery_app.task
def generate_csv_data_set_file(data_set: DataSet) -> NoReturn:
    print(1)
    csv_generator: CSVDataSet = CSVDataSet(data_set=data_set)
    print(2)
    csv_generator.generate()
