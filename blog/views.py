from django.shortcuts import render, redirect

from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Category
from .forms import  PostForm, PostUpdateForm, ComentCreationForm


def posts_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        "posts": posts,
        "categories": categories,
    }
    return render(request, "samples.html", context)


def post_details(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    form = ComentCreationForm()

    context = {
        "post": post,
        "form": form,
    }
    return render(request, "post_details.html", context)
    
    

def get_posts_by_category(request, category_pk):
    posts = Post.objects.filter(category_id=category_pk)

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
def update_post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.owner.username != request.user.username:
        return redirect('blog:post_details', pk=post_pk)

    if request.method == 'POST':
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_details', pk=post_pk)
    else:
        form = PostUpdateForm(instance=post)

    return render(request, 'update_post.html', {'form': form, 'post': post})



@login_required  
def like_unlike_post_view(request, post_pk):
    user = request.user
    post: Post = get_object_or_404(Post, pk=post_pk)

    if post not in user.favorites.all():
        user.favorites.add(post)
    else:
        user.favorites.remove(post)
    
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def write_comments(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method =="POST":
        form=ComentCreationForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner=request.user
            comment.post_id = post
            comment.save()
    return redirect("blog:post_details", post_pk=post.pk)







