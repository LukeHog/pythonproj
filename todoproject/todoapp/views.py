from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem, TodoList

def todoappView(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})

def todolistpage(request, i):
    todo = TodoList.objects.get(id=i)
    todo_items = TodoListItem.objects.filter(todo=todo)
    return render(request, 'todolist.html', {'todo_items': todo_items, 'todo':todo})

def addtodolist(request):
    new = request.POST['todoname']
    new_todo = TodoList(name = new)
    new_todo.save()
    return HttpResponseRedirect('/todoapp/')

def deletetodolist(request, i):
    item = TodoList.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/')


def addTodoView(request, i):
    x = request.POST['content']
    new_item = TodoListItem(content = x, todo=TodoList.objects.get(id=i))
    new_item.save()
    return HttpResponseRedirect(f'/todolistpage/{i}')

def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect(f'/todolistpage/{i}')

def updateTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.status = True
    item.save()
    return  HttpResponseRedirect(f'/todolistpage/{i}')