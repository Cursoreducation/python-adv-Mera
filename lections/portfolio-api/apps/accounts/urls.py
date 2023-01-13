from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from .views import register, change_password, update_profile, logout, delete_profile


namespace = "accounts"

urlpatterns = [
    path("login/", token_obtain_pair, name="token-obtain-pair"),
    path("login/refresh/", token_refresh, name="token-refresh"),
    path("register/", register, name="register"),
    path("change_password/", change_password, name="change_password"),
    path("update_profile/", update_profile, name="update_profile"),
    path("destroy/", delete_profile, name="delete"),
    path("logout/", logout, name="logout"),
]
