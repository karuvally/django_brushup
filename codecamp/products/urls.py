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


