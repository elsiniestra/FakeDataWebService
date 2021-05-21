from typing import List

from django.urls import URLPattern, path

from src.apps.data_schemas import views


urlpatterns: List[URLPattern] = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('schema/new/', views.DataSchemaCreateView.as_view(), name='schema-new'),
    path('schema/delete/<int:schema_id>/', views.data_schema_delete_view,
         name='schema-delete'),
    path('schema/<int:schema_id>/sets/', views.DataSetListView.as_view(), name='schema-sets'),
    path('schema/<int:set_id>/sets/download/', views.data_set_download_view,
         name='schema-sets-download'),
    path('schema/<int:schema_id>/sets/create/', views.data_set_create_view,
         name='schema-sets-create'),
]
