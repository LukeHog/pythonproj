from rest_framework import serializers
from .models import TodoList, TodoListItem

class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = '__all__'

class TodoListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoListItem
        fields = ('id', 'content', 'status')
