from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/about/
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    # http://127.0.0.1:8000/cats/2/
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # http://127.0.0.1:8000/cats/2fevnejvbqeo/
    # re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive)
    # регулярка, четырехзначный год
    path("archive/<year4:year>/", views.archive, name='archive')
    # использование самодельного конвертера
]
