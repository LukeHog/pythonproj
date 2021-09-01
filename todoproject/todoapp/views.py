from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem, TodoList

def todoappView(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})

def addtodolist(request):
    new = request.POST['todoname']
    new_todo = TodoList(name = new)
    new_todo.save()
    return HttpResponseRedirect('/todoapp/')

def deletetodolist(request):
    pass


def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/')

def updateTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.status = True
    item.save()
    return  HttpResponseRedirect('/todoapp/')