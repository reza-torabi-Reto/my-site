"""
this script is used to create the models for the projects app.

Author: reza
date: 6/28/2020
"""
from django.urls import path
from . views import home, detail_article, category_list


app_name = "blog"
urlpatterns = [
       path('' ,home, name="home"),
       path('page/<int:page>' ,home, name="home"),
       path('post/<slug:slug>', detail_article, name="detail_article"),
       path('category/<slug:slug>', category_list, name="category_list"),
]