'''
Created on Feb 11, 2018

@author: vp60132n
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]