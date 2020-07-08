"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article, Category

# Views
def home(request):
    context = {
        'articles': Article.objects.filter(status="p"),
    }
    return render(request, "blog/home.html", context)

def detail_article(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status="p")
    }
    return render(request, 'blog/single-post.html', context)

def category_list(request, slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, 'blog/category.html', context)
