"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Article, Category

# Views
class ArticleList(ListView):
    """Demonstrates docstrings and does nothing really."""
    queryset = Article.objects.published()
    paginate_by = 5


class ArticleDetail(DetailView):
    """Demonstrates docstrings and does nothing really."""
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


class CategoryList(ListView):
    """Demonstrates docstrings and does nothing really."""
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category 
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


























