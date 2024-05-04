from django.contrib import admin
from .models import Article,Comment

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created_date"]
    list_display_links = ["title", "created_date"]
    list_filter = ["created_date"]
    search_fields = ["title"]
    class Meta:
        model = Article

admin.site.register(Comment)
