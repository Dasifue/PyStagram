from django.shortcuts import render, redirect

from django.shortcuts import  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, Category,Comment
from .forms import  PostForm, PostUpdateForm, ComentCreationForm, AnswerCommentForm, ComentUpdateForm

from .utils import find_recomendations

from .models import User

@login_required
def posts_list(request):
    
    posts = Post.objects.filter(owner__in=request.user.followings.all()).order_by("-published")
    categories = Category.objects.all()
    paginator = Paginator(posts, 10)

    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    recomendations = find_recomendations(request.user)

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "recomendations": recomendations
    }
    return render(request, "index.html", context)


def post_details(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    user = post.owner
    info = user.info
      
    form = ComentCreationForm()
    comments = Comment.objects.filter(post_id=post_pk, parent=None)
      
    context = {
        "user": user,
        "universities": info.education.all(),
        "role": info.work,
        "address": info.address,
        "country": info.country,
        "post": post,
        "form": form,
        "comments": comments,
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
def delete_post(request, post_pk):
    post=get_object_or_404(Post, pk=post_pk)
    if post.owner.username != request.user.username:
        return redirect('blog:post_details', post_pk=post_pk)
    
    post.delete()
    return redirect('account:profile', pk=request.user.pk)



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
def delete_post(request, post_pk):
    post=get_object_or_404(Post, pk=post_pk)
    if post.owner.username != request.user.username:
        return redirect('blog:post_details', post_pk=post_pk)
    
    post.delete()
    return redirect('account:profile', pk=request.user.pk)

  
  
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


@login_required
def answer_comment(request, comment_id):
    parent_comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.method == "POST":
        form = AnswerCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = request.user
            comment.parent = parent_comment
            comment.post_id = parent_comment.post_id
            comment.save()
            return redirect(request.META.get('HTTP_REFERER'))
    
    form = AnswerCommentForm()
    return render(request, "post_details.html", {"form": form, "parent_comment": parent_comment})


@login_required
def delete_comment(request, comment_pk):
    comment= Comment.objects.get(pk=comment_pk)
    
    if comment not in request.user.comments.all():
        return redirect("blog:post_details", post_pk=comment.post_id.pk)
    
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def update_comment(request, comment_id):
    template_name = 'update_comment.html'
    comment = get_object_or_404(Comment, id=comment_id)

    
    if request.method == "POST":
        form = ComentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('blog:post_details', post_pk=comment.post_id.id)
        
             
    else:
        form = ComentUpdateForm(instance=comment)
    
    return render(request, template_name, {'form': form, 'comment': comment})



def popular_posts_view(request):

    category = request.GET.get("category")
    search = request.GET.get("search")

    if category and search:
        posts = Post.objects.filter(category_id=category, title__icontains=search)
    elif category:
        posts = Post.objects.filter(category_id=category)
    elif search:
        posts = Post.objects.filter(title__icontains=search)
    else:
        posts = Post.objects.all()

    
    posts = sorted(posts, key=lambda post: post.rating, reverse=True)

    paginator = Paginator(posts, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    categories = Category.objects.all()
    return render(request,"popular.html", {"page_obj":page_obj, "categories": categories})

@login_required
def favorites_view(request):
    favorites=request.user.favorites.all()

    paginator = Paginator(favorites, 10)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)

    return render (request, "favorites.html", {"page_obj":page_obj})

