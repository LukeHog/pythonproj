from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoListItem, TodoList

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
