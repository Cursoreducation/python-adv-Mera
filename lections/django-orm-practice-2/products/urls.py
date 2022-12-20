from django.urls import path
from .views import add_product, product_details, edit_product, update_product, add_category

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/edit/<int:id>", edit_product, name="edit_product"),
    path("/update/<int:id>", update_product, name="update_product"),
    path("/category/add", add_category, name="add_category"),
    path("/<int:id>", product_details, name="product_details")
]