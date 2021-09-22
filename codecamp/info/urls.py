from django.urls import path
from .views import info_home_view


urlpatterns = [
    path("", info_home_view, name="home_view"),
]
