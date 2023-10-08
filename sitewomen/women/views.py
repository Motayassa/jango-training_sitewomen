from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify 


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'Биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


def index(request):  # request это ссылка на класс HttpRequest
    # через request можно получать GET и POST коллекции
    #   t = render_to_string('women/index.html')
    # отрисовка шаблона на который ведет ссылка
    #   return HttpResponse(t)
    # Формирует загодовок и содержимое ответа
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
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
