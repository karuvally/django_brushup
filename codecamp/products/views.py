from django.shortcuts import render
from .models import Product
from .forms import ProductModelForm, ProductRawForm

def product_model_form_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductModelForm()
    
    context = {
        "form": form,
    }
    return render(request, "product/model_form.html", context)

def product_raw_form_view(request):
    raw_form = ProductRawForm()
    if request.method == "POST":
        raw_form = ProductRawForm(request.POST)
        if raw_form.is_valid():
            print(raw_form.cleaned_data)
            Product.objects.create(**raw_form.cleaned_data)
        raw_form = ProductRawForm()
    context = {
        "raw_form": raw_form,
    }
    return render(request, "product/raw_form.html", context)

def product_html_form_view(request):
    if request.method == "POST":
        Product.objects.create(
            title=request.POST.get("title"),
            price=request.POST.get("price"),
        )
    return render(request, "product/html_form.html", {})

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
