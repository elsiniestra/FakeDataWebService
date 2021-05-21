from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.utils import timezone

from src.apps.data_schemas.tasks import generate_csv_data_set_file
from src.apps.data_schemas.models import DataSchema, DataSet
from src.apps.data_schemas.services import CSVDataSet


class DataSetListView(LoginRequiredMixin, ListView):
    template_name = 'apps/dataSchemas/dataSetList.html'

    def get_queryset(self) -> QuerySet[DataSet]:
        return DataSchema.objects.get(id=self.kwargs.get('schema_id')).sets.all()

    def get_context_data(self, **kwargs) -> dict:
        context_data: dict = super().get_context_data(**kwargs)
        context_data.update(self.kwargs)
        return context_data


def data_set_create_view(request: Any, schema_id: int) -> HttpResponseRedirect:
    data_set: DataSet = DataSet.objects.create(
        schema_id=schema_id,
        rows=int(request.POST.get('rows')),
        created_at=timezone.now(),
    )
    generate_csv_data_set_file.delay(data_set)
    return redirect(to=f'/data/schema/{schema_id}/sets/')  # TODO:


def data_set_download_view(request: Any, set_id: int) -> HttpResponse:
    data_set: DataSet = DataSet.objects.get(id=set_id)
    csv_generator: CSVDataSet = CSVDataSet(data_set=data_set)
    return csv_generator.download_trigger()
