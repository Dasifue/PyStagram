from django.urls import path

from .views import (
    posts_list,
    post_details
)

app_name = "blog"

urlpatterns = [
    path("", posts_list, name="posts_list"),
    path("post/details/<int:pk>", post_details,name="post_details"  ),
]
