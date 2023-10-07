from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify 


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):  # request это ссылка на класс HttpRequest
    # через request можно получать GET и POST коллекции
    #   t = render_to_string('women/index.html')
    # отрисовка шаблона на который ведет ссылка
    #   return HttpResponse(t)
    # Формирует загодовок и содержимое ответа
    data = {
        'title': 'главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 4, 5},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
        'url': slugify("The Main Page"),
            }
    return render(request, 'women/index.html', context=data)  # заменяет верхние две строки


def about(request):
    return render(request, "women/about.html", {'title': 'О сайте'})


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
