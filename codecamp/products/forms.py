from products.views import product_list_view
from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "price",
            "description",
            
        ]

class ProductRawForm(forms.Form):
    title   = forms.CharField()
    price   = forms.DecimalField()
