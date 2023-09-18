from django.urls import path

from .views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    update_profile_view,
    follow_unfollow_user_view,
)

app_name = "account"


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/<int:pk>", profile_view, name="profile"),
    path("profile/update/", update_profile_view, name="update"),
    path("user/fl_unfl/<int:user_pk>", follow_unfollow_user_view, name="fl_unfl")
]