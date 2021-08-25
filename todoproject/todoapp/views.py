from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'index.html', {'all_items': all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    item = TodoListItem.objects.get(id=i)
    item.delete()
    return HttpResponseRedirect('/todoapp/')