from django import templatetags
import women.views as views

register = template.Library()

@register.simple_tag()  # создание простого тега
def get_categories():
    return views.cats_db
