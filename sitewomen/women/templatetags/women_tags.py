from django import templatetags
import women.views as views

register = template.Library()


def get_categories():
    return views.cats_db
