from django.db import models
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Yazar", related_name="user")
    title = models.CharField(max_length=150, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(blank=True, null=True, verbose_name="Fotoğraf Ekle", upload_to="images/")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_date"]

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    comment_user = models.CharField(max_length=100, verbose_name="isim")
    comment_content = models.TextField(max_length=500, verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_user
    
    class Meta:
        ordering = ["-comment_date"]

    