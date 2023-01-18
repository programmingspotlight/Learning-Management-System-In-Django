from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser

# Create your models here.
class Articles(models.Model):
    article_author = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    article_title = models.CharField(max_length= 150)
    article_image = models.ImageField(upload_to= 'article/%Y/%m/%d')
    article_snippet = models.TextField()
    article_body = models.TextField()
    article_category = models.ForeignKey('ArticleCategory', on_delete= models.CASCADE)
    article_tags = models.ManyToManyField('ArticleTags')
    posted_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    article_slug = models.SlugField(max_length= 150, unique= True, null= True, blank= True)

    class Meta:
        verbose_name = 'Articles'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        return reverse("article_details", kwargs={"article_slug": self.article_slug})

    def save(self, *args, **kwargs):
        if not self.article_slug:
            self.article_slug = slugify(self.article_title)
        return super().save(*args, **kwargs)


class ArticleCategory(models.Model):
    category_title = models.CharField(max_length= 50)
    category_slug = models.SlugField(max_length= 50, unique= True, null= True, blank= True)

    class Meta:
        verbose_name = 'Article Categories'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.category_title

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_title)
        return super().save(*args, **kwargs)


class ArticleTags(models.Model):
    tag_title = models.CharField(max_length= 50)
    tag_slug = models.SlugField(max_length= 50, unique= True, null= True, blank= True)

    class Meta:
        verbose_name = 'Article Tags'
        verbose_name_plural = 'Article Tags'

    def __str__(self):
        return self.tag_title

    def save(self, *args, **kwargs):
        if not self.tag_slug:
            self.tag_slug = slugify(self.tag_title)
        return super().save(*args, **kwargs)


