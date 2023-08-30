from django.db import models
from account.models import User

class Category(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание")

    def __str__(self):
        return f"{self.name} - {self.description[:20]}"

    class Meta:
        verbose_name_plural = "Категории"


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец", related_name="posts")
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Картинка", upload_to="posts/", null=True, blank=True)
    content = models.TextField("Контент", null=True, blank=True)
    published = models.DateField("Дата публикации", auto_now_add=True)
    updated = models.DateField("Дата обновления", auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"