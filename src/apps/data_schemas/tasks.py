from typing import NoReturn

from src.apps.data_schemas.services import CSVDataSet
from src.apps.data_schemas.models import DataSet
from src.config.core.celery import celery_app


@celery_app.task
def generate_csv_data_set_file(data_set_id: int) -> NoReturn:
    data_set: DataSet = DataSet.objects.get(id=data_set_id)
    csv_generator: CSVDataSet = CSVDataSet(data_set=data_set)
    csv_generator.generate()
