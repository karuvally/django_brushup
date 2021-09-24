from django.shortcuts import render
from .models import Sensor
from django.views.generic import(
    ListView,
)

def info_home_view(request):
    """Insert sensor data into DB"""
    sensors = Sensor()
    sensors.update_sensor_data()
    return render(request, "info_home.html", {})

def info_list_view(ListView):
    """Show stored temp values as a list"""
    queryset = Sensor.objects.all()
