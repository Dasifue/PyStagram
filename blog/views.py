from django.shortcuts import render, redirect

from django.shortcuts import  get_object_or_404, redirect

from .models import Post, Category
from .forms import  PostForm, PostUpdateForm


def posts_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "samples.html", context)


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

  
  

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_post.html')  
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
  
  

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = PostUpdateForm(instance=post)

    return render(request, 'update_post.html', {'form': form, 'post': post})


