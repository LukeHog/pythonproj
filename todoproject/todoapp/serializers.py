from rest_framework import serializers
from .models import TodoList, TodoListItem

class TodoListSerializer(serializers.ModelSerializer):
    """
    Class Name: TodoListSerializer
    Derived Class: serializers.ModelSerializer

    Description: This class is serializer for the model TodoList
    and it define the fields which are to be sent in JSON format
    """
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoListItemSerializer(serializers.ModelSerializer):
    """
    Class Name: TodoListSerializer
    Derived Class: serializers.ModelSerializer

    Description: This class is serializer for the model TodoListItem
    and it define the fields which are to be sent in JSON format
    """
    class Meta:
        model = TodoListItem
        fields = ('id', 'content', 'status')
