'''
Created on Feb 11, 2018

@author: vp60132n
'''
from rest_framework import serializers

from .UserModel import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo