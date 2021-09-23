from django.db import models

# Create your models here.
class Sensors(models.Model):
    cpu = models.DecimalField(decimal_places=1, max_digits=4)