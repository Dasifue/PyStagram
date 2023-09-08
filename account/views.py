from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import (
    RegisterForm,
    LoginForm,
    UserBaseForm,
    UserInfoForm,
)

from .models import User, UserInfo


def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            info = UserInfo.objects.create(user=user)
            info.save()
            return redirect("account:login")
        else:
            return render(request, "sign-up.html", {"form": form})
    else:   
        return render(request, "sign-up.html", {"form": form})
    

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        user = authenticate(username=form.data["username"], password=form.data["password"])
        if user is not None:
            login(request, user)
            return redirect("blog:posts_list")
        else:
            return render(request, "sign-in.html", {"form": form, "error": "Неверное имя пользователя или пароль!"})
    else:
        return render(request, "sign-in.html", {"form": form})
    


def logout_view(request):
    logout(request)
    return redirect("account:login")
    

def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    info = user.info
    context = {
        "user": user,
        "universities": info.education.all(),
        "role": info.work,
        "address": info.address,
        "country": info.country,
    }
    return render(request, "profile.html", context)
    

# @login_required("login")
def update_profile_view(request):
    user = request.user

    base_form = UserBaseForm(instance=user)
    info_form = UserInfoForm(instance=user.info)

    if request.method == "POST":
        base_form = UserBaseForm(data=request.POST, instance=request.user, files=request.FILES)
        info_form = UserInfoForm(data=request.POST, instance=request.user.info)


        if base_form.is_valid() and info_form.is_valid():
            base_form.save()
            info_form.save()
            return redirect("account:profile", pk=user.pk)
        return render(request, "edit_profile.html", {"user": user, "base_form": base_form, "info_form": info_form})



    context = {
        "user": user,
        "base_form": base_form,
        "info_form": info_form,
    }

    return render(request, "edit_profile.html", context)
    