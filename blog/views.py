from django.shortcuts import render

from .models import Post, Category

def main_page(request):
    posts = Post.objects.all()

    context = {
        "posts": posts,
        "key": "My name is Emir",
    }
    return render(request, "index.html", context)


def post_details(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post
    }
    return render(request, "post_details.html", context)
    