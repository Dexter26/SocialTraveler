'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers
from . import models
from travel.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo