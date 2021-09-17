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
    title       = forms.CharField(label="സാധനത്തിന്റെ പേര്")
    price       = forms.DecimalField(label="പരമാവധി റീറ്റെയ്ൽ തുക", initial=99.99)
    description = forms.CharField(label="വിശദീകരണം", widget=forms.Textarea)
    summary     = forms.CharField(
        label="അധിക വിവരം",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "വെറുതെ ഒരു പ്ലേസ്‌ഹോൾഡർ",
                "cols": 50,
                "rows": 5,
                "class": "my_bootstrap_class",
                "id": "adhika_vivaram_id",
            }
        )
    )
