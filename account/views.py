from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .forms import (
    RegisterForm,
    LoginForm
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
    