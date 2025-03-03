﻿from django.urls import path
from .views import index, list_books, aboutus

app_name = 'books' 

urlpatterns = [
    path('', index, name='index'),   
    path('list/', list_books, name='list_books'),
    path('about/', aboutus, name='aboutus'),
]