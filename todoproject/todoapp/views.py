from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoListItem, TodoList
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoListSerializer, TodoListItemSerializer

def todoappview(request):
    """
    The todoappview renders the main page

    :param request: this the default parameter of view
    :return: render function returns the index.html
    """
    all_todo_items = TodoList.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})

def todolistpage(request, i):
    """
    The todolistpage renders the todolist.html for the selected TodoList with the corresponding TodoListItem

    :param request: this the default parameter of view
    :param i: is the id of the TodoList for which the TodoListItems are to be displayed
    :return: render function returns the todolist.html
    """
    todo = TodoList.objects.get(id=i)
    todo_items = TodoListItem.objects.filter(todo=todo)
    return render(request, 'todolist.html', {'todo_items': todo_items, 'todo':todo})

def addtodolist(request):
    """
    The addtodolist view adds new TodoList passed through the form

    :param request: this the default parameter of view
    :return: redirects to 'home' path after adding the new TodoList
    """
    new = request.POST['todoname']
    new_todo = TodoList(name=new)
    new_todo.save()
    return redirect('home')

def deletetodolist(request, i):
    """
    The deletetodolist view deletes the selected TodoList with id = i

    :param request: this the default parameter of view
    :param i: is an integer. It is the id of TodoList to be deleted
    :return: redirects to 'home' path after deleting the TodoList
    """
    item = TodoList.objects.get(id=i)
    item.delete()
    return redirect('home')

def addtodoview(request, i):
    """
    The addtodoview view adds a TodoListItem

    :param request: this the default parameter of view
    :param i: is an integer. It is the id of TodoList to which the new TodoListItem is referred.
    :return: redirects to 'todolistpage' with the parameter i = TodoList.id
    """
    x = request.POST['content']
    new_item = TodoListItem(content=x, todo=TodoList.objects.get(id=i))
    new_item.save()
    return redirect('todolistpage', i=i)

def deletetodoview(request, i):
    """
    The deletetodoview view deletes the selected TodoListItem with id = i

    :param request: this the default parameter of view
    :param i: is an integer. It is the id of TodoListItem to be deleted
    :return: redirects to 'todolistpage' with the parameter i = TodoList.id
    """
    item = TodoListItem.objects.get(id=i)
    todo_id = item.todo.id
    item.delete()
    return redirect('todolistpage', i=todo_id)

def updatetodoview(request, i):
    """
    The updatetodoview view updates the completion status of the TodoListItem to True

    :param request: this the default parameter of view
    :param i: is an integer. It is the id of the TodoListItem to be updated
    :return: redirects to 'todolistpage' with the parameter i = TodoList.id
    """
    item = TodoListItem.objects.get(id=i)
    item.status = True
    todo_id = item.todo.id
    item.save()
    return redirect('todolistpage',i=todo_id)

class TLList(APIView):
    """
    Class Name: TLList
    Derived Class: rest_framework.view.APIView

    Description: This view is called when the url for api is accessed
    """

    def get(self, request):
        """
        The get method returns a json format data as response for a get request
        :param request: this the default parameter of view
        :return: JSON format of data in TodoList data
        """
        todos = TodoList.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        The post method gets the json format data and adds a record in the TodoList
        :param request:
        :return:
        """
        todo = request.data.get('todo')
        serializer = TodoListSerializer(data=todo)
        if serializer.is_valid(raise_exception=True):
            saved_todo = serializer.save()
        return Response({"success": "Todo '{}' created successfully".format(saved_todo.name)})

class TLIList(APIView):
    """
    Class name: TLIList
    Derived Class: rest_framework.view.APIView

    Description: This class view is called when the url '/todolistapi' is called
    """

    def get(self, request, id):
        """
        The get method returns a json format data as response for a get request

        :param request: this the default parameter of view
        :param id: id of the TodoList
        :return: JSON format of data in TodoListItem table
        """
        todo = TodoList.objects.get(id=id)
        todolists = TodoListItem.objects.filter(todo=todo)
        serializer = TodoListItemSerializer(todolists, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        """
        The post method gets data from request in json format and adds a record in TodoLisItem
        :param request: this the default parameter of view
        :param id: id of the TodoList
        :return: Response with success message
        """
        todolist = request.data.get('todolist')
        serializer = TodoListItemSerializer(data=todolist)
        if serializer.is_valid(raise_exception=True):
            saved_todolist = serializer.save()
        return Response({"success": "TodoItem '{}' created successfully".format(saved_todolist.content)})

    def delete(self, request, id):
        todo = get_object_or_404(TodoList.objects.all(), id=id)
        todo.delete()
        return Response({"message": "Todolist with id {} has been deleted.".format(id)}, status=204)

class TodoListItemAPI(APIView):
    def get(self, request, id):
        todolistitem = TodoListItem.objects.get(id=id)
        serializer = TodoListItemSerializer(todolistitem)
        return Response(serializer.data)

    def delete(self, request, id):
        todo = TodoListItem.objects.get(id=id)
        todo.delete()
        return Response({"message": "TodolistItem with id {} has been deleted.".format(id)}, status=204)