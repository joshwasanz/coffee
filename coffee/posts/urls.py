from django.urls import path
from . import views

urlpatterns = [
    #for templates
    path("posts/",view=views.posts,name="posts"),
    path("post/<str:pk>/",view=views.post,name="post"),
    path("update-post/<str:pk>/",view=views.update_post,name="update-post"),
    path("delete-post/<str:pk>/",view=views.delete_post,name="delete-post"),


    #for api
]