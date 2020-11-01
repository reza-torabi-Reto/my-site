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

@register.inclusion_tag("registration/partials/link.html")
def link(request, link_name, icn , content):
    return{
        "request": request,
        "link_name": link_name,
        "link": "account:{}".format(link_name),
        "icn": icn,
        "content": content,
    }