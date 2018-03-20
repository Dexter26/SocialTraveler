'''
Created on Feb 11, 2018

@author: vp60132n
'''
from django.urls import path
from travel.user import UserViews

urlpatterns = [
    path('', UserViews.TodoList.as_view()),
    path('<int:pk>/', UserViews.TodoDetail.as_view()),
    path('addTodo/', UserViews.AddTodo.as_view()),
]