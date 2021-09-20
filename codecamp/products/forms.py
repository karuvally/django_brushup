from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    # Overriding default implementation of title field
    title = forms.CharField(label="സാധനത്തിന്റെ പേര്")
    class Meta:
        model = Product
        fields = [
            "title",
            "price",
            "description",
        ]

    # def clean_<field_name>(self, *args, **kwargs):
    #     pass
    # Ensure pricing is not too high
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price > 999:
            raise forms.ValidationError("Price too high!")
        return price

class ProductRawForm(forms.Form):
    # Here, we do not have a TextField, so we stick with CharField
    # Make sure the var names match that of model,
    # This makes it possible to pass data as a dict (**raw_form.cleaned_data)
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

class ProductDeleteForm(forms.Form):
    product_tuple = [
        (product.id, product.title)
        for product in Product.objects.all()
    ]
    title = forms.ChoiceField(choices=product_tuple)

