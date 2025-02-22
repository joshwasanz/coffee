from django.urls import path
from . import views

urlpatterns = [
    path("posts/",view=views.post_list),
]