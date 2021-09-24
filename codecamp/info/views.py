from django.shortcuts import render
from .models import Sensor

# Create your views here.
def info_home_view(request):
    sensors = Sensor()
    sensors.update_sensor_data()
    return render(request, "info_home.html", {})
