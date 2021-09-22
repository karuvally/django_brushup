from django.urls import path
from .views import info_home_view

app_name = "info"
urlpatterns = [
    path("home_view/", info_home_view, name="home_view"),
]
