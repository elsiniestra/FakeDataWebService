from typing import List

from django.urls import path, include, URLPattern


urlpatterns: List[URLPattern] = [
    path('user/', include('src.apps.user.urls')),
    path('data/', include('src.apps.data_schemas.urls')),
]
