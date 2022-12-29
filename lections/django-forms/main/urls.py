from django.urls import path
from .views import home, sign_up, sign_in, logout_view, add_to_cart, show_cart, delete_cart

urlpatterns = [
    path("", home, name="home"),
    path("sign-up", sign_up, name="sign-up"),
    path("sign-in", sign_in, name="sign-in"),
    path("logout", logout_view, name="logout"),
    path("cart/<int:id>", add_to_cart, name="add_to_cart"),
    path("cart", show_cart, name="show_cart"),
    path("cart/delete/<int:id>", delete_cart, name="delete_cart"),
]