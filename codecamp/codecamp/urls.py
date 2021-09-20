"""codecamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view
from products.views import product_list_view, product_detail_view
from products.views import product_model_form_view, product_html_form_view
from products.views import product_raw_form_view, product_model_form_change_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('product_list/', product_list_view, name='product_list'),
    path('product/<int:id_lookup>/', product_detail_view, name='product_detail'),
    path('model_form/', product_model_form_view, name='model_form'),
    path('model_change_form/', product_model_form_change_view, name='model_change'),
    path('html_form/', product_html_form_view, name='html_form'),
    path('raw_form/', product_raw_form_view, name='raw_form'),
    path('admin/', admin.site.urls),
]
