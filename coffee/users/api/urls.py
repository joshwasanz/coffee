from django.urls import path

from .views import get_users

urlpatterns = [
    path("users/",view=get_users)
]