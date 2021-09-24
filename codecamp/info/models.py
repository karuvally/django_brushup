import subprocess
import json
from django.db import models

# Create your models here.
class Sensor(models.Model):
    cpu = models.DecimalField(decimal_places=1, max_digits=4)

    def _get_sensor_data(self):
        process = subprocess.Popen(
            ["sensors", "-j"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        process.wait()
        sensor_data = json.loads(process.communicate()[0].decode())
        return sensor_data
    
    def update_sensor_data(self):
        data = self._get_sensor_data()
        Sensor.objects.create(cpu=data["coretemp-isa-0000"]["Package id 0"]["temp1_input"])
