from django.urls import path
from . import views

urlpatterns = [
    path("posts/",view=views.post_list),
    path("posts/<str:pk>/",view=views.get_post),
]