from django.shortcuts import render, redirect

from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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
    post = get_object_or_404(Post, pk=pk)

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

  
  
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('blog:posts_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
  
  
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.owner.username != request.user.username:
        return redirect('blog:post_details', pk=post_id)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_details', pk=post_id)
    else:
        form = PostUpdateForm(instance=post)

    return render(request, 'update_post.html', {'form': form, 'post': post})


