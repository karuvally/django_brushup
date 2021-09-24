from django.shortcuts import render
from .models import Sensors

# Create your views here.
def info_home_view(request):
    sensors = Sensors()
    sensors.update_sensor_data()
    return render(request, "info_home.html", {})
