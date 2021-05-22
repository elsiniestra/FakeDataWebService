from typing import AnyStr, NoReturn
from dataclasses import dataclass
import csv
import io

from django.core.files.base import ContentFile
from django.db.models import QuerySet
from django.http import HttpResponse
from faker import Faker

from src.apps.data_schemas.models import DataSet, DataSchemaColumn


@dataclass
class CSVDataSet:
    data_set: DataSet

    def generate(self) -> NoReturn:
        file_content: str = self._generate()
        self._set_data_set_file(file_content=file_content)
        self._check_data_set_ready_status()

    def _generate(self) -> str:
        faker: Faker = Faker()
        csv_buffer: io.StringIO = io.StringIO()

        csv_writer: csv.writer = csv.writer(
            csv_buffer,
            delimiter=self.data_set.schema.preferences.column_separator,
            quotechar=self.data_set.schema.preferences.string_character,
            quoting=csv.QUOTE_NONNUMERIC
        )
        set_columns: QuerySet[DataSchemaColumn] = self.data_set.schema.columns.order_by('order')
        csv_writer.writerow([column.title for column in set_columns])
        csv_writer.writerows([
            [getattr(faker, column.type)() for column in set_columns]
            for _ in range(self.data_set.rows)
        ])

        return csv_buffer.getvalue()

    @property
    def file_name(self) -> str:
        return (f'{self.data_set.schema.title}_'
                f'{self.data_set.created_at.strftime("%d-%m-%y-%H:%M")}.csv')

    def download_trigger(self) -> HttpResponse:
        data: AnyStr = self.data_set.file.open()
        response: HttpResponse = HttpResponse(data, content_type='application/x-download')
        response['Content-Disposition'] = f'attachment;filename={self.data_set.file.name}'
        return response

    def _set_data_set_file(self, file_content: str) -> NoReturn:
        self.data_set.file.save(name=self.file_name, content=ContentFile(file_content))

    def _check_data_set_ready_status(self) -> NoReturn:
        self.data_set.status = DataSet.Statuses.READY
        self.data_set.save()
