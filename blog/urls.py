from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name="articles"),
    path('<slug:article_slug>/', views.article_details, name="article_details"),
    path('tag/<slug:tag_slug>/', views.tag_articles, name="tag_articles"),
    path('category/<slug:category_slug>/', views.category_articles, name="category_articles"),
    path('archive/<int:year>/<int:month>/', views.archive_articles, name='archive'),
    path('search/', views.articles_search, name="articles_search"),
]

