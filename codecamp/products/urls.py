# URL module for products app
from django.urls import path
from products.views import (
    product_list_view,
    product_detail_view,
    product_model_form_view,
    product_html_form_view,
    product_raw_form_view,
    product_model_form_change_view,
    product_delete_view,
)

urlpatterns = [
    path('product_list/', product_list_view, name='product_list'),
    path('product/<int:id_lookup>/', product_detail_view, name='product_detail'),
    path('model_form/', product_model_form_view, name='model_form'),
    path('model_change_form/', product_model_form_change_view, name='model_change'),
    path('html_form/', product_html_form_view, name='html_form'),
    path('raw_form/', product_raw_form_view, name='raw_form'),
    path('delete_form/', product_delete_view, name='delete_form'),
]
