"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article, Category

# Views
def home(request, page=1):
    articles_list = Article.objects.published()
    _paginator = Paginator(articles_list, 2)
    articles = _paginator.get_page(page)
    context = {
        'articles': articles,
    }
    return render(request, "blog/home.html", context)

def detail_article(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status="p")
    }
    return render(request, 'blog/single-post.html', context)

def category_list(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    article_list = category.articles.published()
    _paginator = Paginator(article_list, 2)
    articles = _paginator.get_page(page)
    context = {
        'category':category,
        'articles':articles
    }
    return render(request, 'blog/category.html', context)
