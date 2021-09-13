from django.shortcuts import render
from .models import Product

def product_detail_view(request):
    products = Product.objects.all()
    context = {"products": []}
    for product in products:
        context["products"].append({
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "summary": product.summary,
            "featured": product.featured,
        })
    return render(request, "product/detail.html", context)
