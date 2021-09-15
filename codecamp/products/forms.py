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
    # Here, we do not have a TextField, so we stick with CharField
    title   = forms.CharField()
    price   = forms.DecimalField()
