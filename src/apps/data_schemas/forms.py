from typing import NoReturn, List

from django.forms import formset_factory, BaseFormSet
from django import forms

from src.apps.data_schemas.models import DataSchema, DataSchemaColumn, DataSchemaPreferences
from src.apps.data_schemas.utils import is_valid_data_schema_columns_ordering


class DataSchemaForm(forms.Form):
    title = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'w-1/2 border-gray-light rounded'})
    )
    column_separator = forms.CharField(
        max_length=128,
        widget=forms.Select(choices=DataSchemaPreferences.ColumnSeparator.choices,
                            attrs={'class': 'w-1/2 border-gray-light rounded'}),
    )
    string_character = forms.CharField(
        max_length=128,
        widget=forms.Select(choices=DataSchemaPreferences.StringCharacter.choices,
                            attrs={'class': 'w-1/2 border-gray-light rounded'}),
    )

    def create_model_instance(self) -> DataSchema:
        schema_preferences: DataSchemaPreferences = DataSchemaPreferences.objects.create(
                column_separator=self.cleaned_data.get('column_separator'),
                string_character=self.cleaned_data.get('string_character'),
            )
        return DataSchema.objects.create(
            title=self.cleaned_data.get('title'),
            preferences=schema_preferences
        )

    def update_model_instance(self, schema_id: int) -> DataSchema:
        schema: DataSchema = DataSchema.objects.get(id=schema_id)

        schema.title = self.cleaned_data.get('title')
        schema.preferences.column_separator = self.cleaned_data.get('column_separator')
        schema.preferences.string_character = self.cleaned_data.get('string_character')
        schema.save()

        return schema


class DataSchemaColumnForm(forms.Form):
    title = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'border-gray-light rounded',
                                      'required': ''}),
    )
    type = forms.CharField(
        max_length=128,
        widget=forms.Select(choices=DataSchemaColumn.Types.choices,
                            attrs={'class': 'border-gray-light rounded'}),
    )
    order = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'border-gray-light rounded',
                                        'required': ''}),
    )

    def create_model_instance(self, schema: DataSchema) -> DataSchemaColumn:
        self.is_valid()
        return DataSchemaColumn.objects.create(
            title=self.cleaned_data.get('title'),
            type=self.cleaned_data.get('type'),
            order=self.cleaned_data.get('order'),
            schema=schema,
        )


class BaseDataSchemaColumnFormset(BaseFormSet):
    def clean(self) -> NoReturn:
        orders: List[int] = list(map(lambda x: x.cleaned_data.get('order'),
                                     self.forms))
        if not is_valid_data_schema_columns_ordering(orders):
            raise forms.ValidationError('Please, fix your columns ordering.'
                                        'Be sure, all numbers are positive and consecutive.')
        super().clean()


DataSchemaColumnFormset: type = formset_factory(form=DataSchemaColumnForm,
                                                formset=BaseDataSchemaColumnFormset,
                                                can_delete=True,
                                                can_delete_extra=False)
