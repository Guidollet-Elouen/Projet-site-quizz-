from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
    path('find_numberchoice/', views.find_numberchoice, name='find_numberchoice'),
]

