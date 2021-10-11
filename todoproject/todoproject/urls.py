"""todoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from todoapp.views import todoappview, addtodoview, deletetodoview, updatetodoview, addtodolist, deletetodolist, todolistpage, TLList, TLIList, TodoListItemAPI, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', register, name="register"),
    path('todoapp/', todoappview, name='home'),
    path('addTodoItem/<int:i>', addtodoview, name='additem'),
    path('deleteTodoItem/<int:i>', deletetodoview, name='deleteitem'),
    path('updateTodoItem/<int:i>', updatetodoview, name='updateitem'),
    path('addtodolist/', addtodolist, name='addtodo'),
    path('deletetodolist/<int:i>', deletetodolist, name='deletetodo'),
    path('todolistpage/<int:i>', todolistpage, name='todolistpage'),
    path('todoapi/', TLList.as_view(), name='todoapi'),
    path('todolistapi/<int:id>', TLIList.as_view(), name='todolistapi'),
    path('todolistitemapi/<int:id>', TodoListItemAPI.as_view(), name='todolistitemapi'),
]
