from typing import Any, List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.conf import settings

from src.apps.data_schemas.forms import DataSchemaColumnFormset, DataSchemaForm, \
    DataSchemaColumnForm
from src.apps.data_schemas.models import DataSchema


class DataSchemaListView(LoginRequiredMixin, ListView):
    template_name = 'apps/dataSchemas/dataSchemaList.html'
    model = DataSchema


class DataSchemaCreateView(LoginRequiredMixin, FormView):
    template_name = 'apps/dataSchemas/dataSchemaCreate.html'
    form_class = DataSchemaForm
    success_url = settings.BASE_URL

    def dispatch(self, request, *args, **kwargs) -> HttpResponseRedirect:
        form: DataSchemaForm = DataSchemaForm(request.POST or None)
        column_formset: DataSchemaColumnFormset = DataSchemaColumnFormset(request.POST or None)

        if form.is_valid() and column_formset.is_valid():
            schema: DataSchema = form.create_model_instance()

            schema_column_form: DataSchemaColumnForm
            for schema_column_form in column_formset:
                schema_column_form.create_model_instance(schema=schema)

            return HttpResponseRedirect(redirect_to=self.get_success_url())

        return self.render_to_response(self.get_context_data(**{'formset': column_formset}))


def data_schema_delete_view(request: Any, schema_id: int) -> HttpResponseRedirect:
    DataSchema.objects.get(id=schema_id).delete()
    return redirect(to=settings.BASE_URL)


class HomeView(DataSchemaListView):
    pass
