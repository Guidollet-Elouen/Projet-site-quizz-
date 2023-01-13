
from django.contrib import admin
from django.urls import include, path
from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
]
