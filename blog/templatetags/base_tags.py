from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "رتو|Reto"

@register.inclusion_tag("blog/partials/category_navbar.html")
def cate():
    return {
         'category': Category.objects.filter(status=True)
    }