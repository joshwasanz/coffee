from django.urls import path
from . import views

urlpatterns = [
    path("register/",view=views.register_user),
    # path("login/"),
    # path("profile/"),
    # path("token/refresh/")
]