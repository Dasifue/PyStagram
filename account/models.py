from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField("Почта", unique=True)
    image = models.ImageField("Аватар", upload_to="account/", default="account/default_avatar.png")
    date_of_birth = models.DateField("Дата рождения", null=True)
    about = models.TextField("О себе")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()



