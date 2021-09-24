from django.urls import path
from .views import(
    info_home_view,
    InfoListView,
)

app_name = "info"
urlpatterns = [
    path("home_view/", info_home_view, name="home_view"),
    path("list_view/", InfoListView.as_view(), name="list_view"),
]
