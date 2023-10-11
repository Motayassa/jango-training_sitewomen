from django import template
import women.views as views

register = template.Library()


@register.simple_tag(name='getcats')  # создание простого тега
def get_categories():
    return views.cats_db


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = views.cats_db
    return {'cats': cats}
# в women/list_categories.html будет доступна переменная cats
