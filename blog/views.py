from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Articles, ArticleCategory, ArticleTags

# Create your views here.
def articles(request):
    articles_list = Articles.objects.all().order_by('-posted_at')

    page_num = request.GET.get('page', 1)
    paginator = Paginator(articles_list, 2) # 15 articles per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        # 'articles': articles_list,
        'articles': page_obj,
    }

    return render(
        request= request,
        template_name= "blog/articles.html",
        context= context
    )


def article_details(request, article_slug):
    article = get_object_or_404(Articles, article_slug= article_slug)
    
    context = {
        'article': article,
    }

    return render(
        request= request,
        template_name= "blog/article.html",
        context= context
    )


def category_articles(request, category_slug):
    category = get_object_or_404(ArticleCategory, category_slug= category_slug)
    category_articles = Articles.objects.filter(article_category= category)
    
    context = {
        'category': category,
        'category_articles': category_articles,
    }

    return render(
        request= request,
        template_name= "blog/category_articles.html",
        context= context
    )


def tag_articles(request, tag_slug):
    tag = get_object_or_404(ArticleTags, tag_slug= tag_slug)
    tag_articles = Articles.objects.filter(article_tags= tag)
    
    context = {
        'tag': tag,
        'tag_articles': tag_articles,
    }

    return render(
        request= request,
        template_name= "blog/tag_articles.html",
        context= context
    )


def archive_articles(request, year, month):
    archive_articles = Articles.objects.filter(posted_at__year=year, posted_at__month=month)
    
    context = {
        'archive_articles': archive_articles,
    }

    return render(
        request= request,
        template_name= "blog/archive_articles.html",
        context= context
    )


def articles_search(request):
    if request.method == 'GET':
        query = request.GET.get("q")
        if query:
            object_list = Articles.objects.filter(Q(article_title__icontains=query))
        else:
            object_list = Articles.objects.all()
    
    context = {
        'articles': object_list,
    }

    return render(
        request= request,
        template_name= "blog/search.html",
        context= context
    )



