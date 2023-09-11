from django.urls import path

from .views import (
    posts_list,
    post_details,
    get_posts_by_category,
    create_post

)

app_name = "blog"

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("post/details/<int:pk>", post_details,name="post_details"),
    path("create/", create_post, name="create_post"),
]

