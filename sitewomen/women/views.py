from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):  # request это ссылка на класс HttpRequest
    # через request можно получать GET и POST коллекции
    t = render_to_string('women/index.html')
    # отрисовка шаблона на который ведет ссылка
    return HttpResponse(t)
    # Формирует загодовок и содержимое ответа


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:  # Выделение спец параметров из GET-запроса.
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport', ))  # возвращает uri  c параметрами
        return HttpResponsePermanentRedirect(uri)
        # Перенаправление постоянное на главную стр
        # Можно использовать представления или имена
        # маршрутов в первом аргументе, вместо адреса
        # Возможно добавление аргументов
        # Возможно использование классов
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
