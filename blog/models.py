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


    @property
    def short_content(self):
        return f"{self.content[:20]}..."
    
    
    @property
    def rating(self) -> int:
        likes = self.favorites.all().count() 
        comments = self.comments.all().count() * 3
        return likes + comments
    
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Комментарии")
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Публикация")
    text = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата обновления", auto_now=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Ответ комментарию", related_name="answers", null=True, blank=True)

    def __str__(self):
        return f"{self.owner.username} {self.text[:20]}"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        
        
