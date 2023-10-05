from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000/
    path('cats/<int:cat_id>/', views.categories),
    # http://127.0.0.1:8000/cats/
]
