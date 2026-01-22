from django.urls import path
from obra.apps.catalog.controllers.admin.product_controller import all_products

app_name = "products"

urlpatterns = [
    path("products/", all_products , name="products"),
]
