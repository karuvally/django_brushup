from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    context = {"products": []}
    for product in products:
        context["products"].append({
            "title": product.title,
            "price": product.price,
        })
    return render(request, "product/list.html", context)
