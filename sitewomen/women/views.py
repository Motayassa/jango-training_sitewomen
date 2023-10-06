from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):  # request это ссылка на класс HttpRequest
    # через request можно получать GET и POST коллекции
    return HttpResponse("Страница приложения women.")
    # Формирует загодовок и содержимое ответа


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:  # Выделение спец параметров из GET-запроса.
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
