from django.shortcuts import render
from .models import Product
from .forms import ProductModelForm

def product_model_form_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {
        "form": form
    }
    return render(request, "product/model_form.html", context)

def product_list_view(request):
    products_obj = Product.objects.all()
    context = {
        "products": [obj for obj in products_obj]
    }
    return render(request, "product/list.html", context)

def product_detail_view(request):
    context = {
        "product_obj": Product.objects.get(id=1)
    }
    return render(request, "product/detail.html", context)
