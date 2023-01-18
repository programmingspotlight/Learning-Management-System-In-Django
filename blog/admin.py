from django.contrib import admin
from .models import Articles, ArticleCategory, ArticleTags

# Register your models here.
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    ordering = ('-posted_at',)
    list_display = ['article_title', 'article_author', 'article_category', 'posted_at']
    list_display_links = ['article_title',]
    list_filter = ['article_category', 'article_author',]
    search_fields = ['article_title', 'article_category__category_title',]
    list_per_page = 15

admin.site.register(ArticleCategory)
admin.site.register(ArticleTags)


