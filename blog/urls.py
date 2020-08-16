"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.urls import path
from . views import ArticleList, ArticleDetail, CategoryList


app_name = "blog"
urlpatterns = [
       path('', ArticleList.as_view(), name="home"),
       path('page/<int:page>', ArticleList.as_view(), name="home"),
       path('post/<slug:slug>', ArticleDetail.as_view(), name="detail_article"),
       path('category/<slug:slug>', CategoryList.as_view(), name="category_list"),
       path('category/<slug:slug>/page/<int:page>', CategoryList.as_view(), name="category_list")
]