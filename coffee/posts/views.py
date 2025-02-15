from django.shortcuts import render

from .models import Post

# Create your views here.


def posts(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,"posts/posts.html",context)


def post(request,pk):
    post = Post.objects.get(id=pk)
    context = {"post":post}

    return render(request,"posts/post.html",context)


def create_post(request):
    pass 

def update_post(request,pk):
    pass

def delete_post(request,pk):
    pass