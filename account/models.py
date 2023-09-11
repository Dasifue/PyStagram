from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField("Почта", unique=True)
    image = models.ImageField("Аватар", upload_to="account/", default="account/default_avatar.png")
    date_of_birth = models.DateField("Дата рождения", null=True)
    about = models.TextField("О себе")
    favorites = models.ManyToManyField("blog.Post", related_name="favorites", verbose_name="Лайки")
    followings = models.ManyToManyField("self", related_name="followers", verbose_name="Подписки")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()



class University(models.Model):
    name = models.CharField("Name", max_length=155)
    
    class Meta:
        verbose_name = "Университет"
        verbose_name_plural = "Университеты"

    def __str__(self):
        return self.name
    

class Country(models.Model):
    name = models.CharField("Name", max_length=100)
    flag = models.ImageField("Флаг", upload_to="flags/")

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="info", verbose_name="Пользователь")
    education = models.ManyToManyField(University, related_name="info", verbose_name="Образование")
    work = models.CharField("Должность", max_length=100)
    address = models.CharField("Адрес", max_length=255)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name="info", verbose_name="Страна")

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self):
        return self.user.username