from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products_obj = Product.objects.all()
    context = {
        "products": [obj for obj in products_obj]
    }
    return render(request, "product/list.html", context)

def product_detail_view(request):
    product_obj = Product.objects.get(id=1)
    context = {
        "title": product_obj.title,
        "description": product_obj.description,
        "featured": product_obj.featured,
    }
    return render(request, "product/detail.html", context)
