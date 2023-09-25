from django.urls import path

from .views import (
    posts_list,
    post_details,
    update_post,
    get_posts_by_category,
    create_post,
    like_unlike_post_view,
    write_comments,
    delete_comment,
    update_comment,
)

app_name = "blog"

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("post/details/<int:post_pk>", post_details,name="post_details"),
    path("post/create/", create_post, name="create_post"),
    path("post/update/<int:post_pk>",update_post,name="update"),
    path("post/lk_unlk/<int:post_pk>", like_unlike_post_view, name="lk_unlk"),
    path("post/comments/create/<int:post_pk>",write_comments,name="create_comment"),
    path("post/comments/delete/<int:comment_pk>", delete_comment, name="delete_comment"),
    path("post/comments/update/<int:comment_id>", update_comment, name="update_comment"),
]

