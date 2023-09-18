from django.shortcuts import render

from .models import Post, Category

def posts_list(request):
    search_query = request.GET.get('search' , '')
    
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.all()
    
    categories = Category.objects.all()
    
    

    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "base.html", context)


def post_details(request, pk):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post
    }
    return render(request, "post_details.html", context)
    

def get_posts_by_category(request, pk):
    posts = Post.objects.filter(category_id=pk)

    context = {
        "posts": posts
    }
    return render(request, "categoty_posts.html", context)


