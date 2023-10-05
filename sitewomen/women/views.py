from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # request это ссылка на класс HttpRequest
    return HttpResponse("Страница приложения women.")
    # Формирует загодовок и содержимое ответа
