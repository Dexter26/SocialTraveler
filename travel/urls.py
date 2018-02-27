'''
Created on Feb 11, 2018

@author: vp60132n
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:pk>/', views.TodoDetail.as_view()),
    path('addTodo/', views.AddTodo.as_view()),
]