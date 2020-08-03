"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.urls import path
from . views import ArticleList, detail_article, category_list


app_name = "blog"
urlpatterns = [
       path('', ArticleList.as_view(), name="home"),
       path('page/<int:page>', ArticleList.as_view(), name="home"),
       path('post/<slug:slug>', detail_article, name="detail_article"),
       path('category/<slug:slug>', category_list, name="category_list"),
       path('category/<slug:slug>/page/<int:page>', category_list, name="category_list")
]