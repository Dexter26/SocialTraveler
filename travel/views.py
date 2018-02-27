from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from . import serializers

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from travel.models import Todo
from travel.serializers import TodoSerializer

# For /todo/ --> Kind of URL
# Post Request
class TodoList(APIView):
    '''
        If the below post method changed to get it will become get request (just change the keyword post-->get)
    '''
    def post(self, request, format=None):
        todos = Todo.objects.all()
        serializer = serializers.TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
# For /todo/addTodo/ --> Kind of URL
# Post Request
class AddTodo(APIView):
    
    def post(self, request, format=None):
        serializer = serializers.TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# For /todo/1/ --> Kind of URL
# Change the various HTTP methods Get-->Retrive, Put-->Update, Delete-->Delete records
class TodoDetail(APIView):
    """
    Retrieve, update or delete a single todo instance.
    """

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo = TodoSerializer(todo)
        return Response(todo.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

