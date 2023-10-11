from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify 


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie, при рождении Войт, ранее Джоли Питт; род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, 
     кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Роби', 'content': 'Биография Марго Роби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
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
    return render(request, "women/about.html", {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
