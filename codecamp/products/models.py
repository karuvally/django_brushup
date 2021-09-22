from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(blank=True)
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id_lookup": self.id})
        