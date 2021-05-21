from typing import List

from django.contrib.auth.views import LogoutView
from django.urls import URLPattern, path

from src.apps.user.views import LoginView

urlpatterns: List[URLPattern] = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
