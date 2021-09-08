from django.db import models

class TodoList(models.Model):
    """
    Class Name: TodoList
    Derived Class Name : models.Model

    Description: It represents the db model of the table TodoList with two fields id and name.
    Fields: id(integer, primary key, serialize), name(Charfield, max_length=110, unique)
    """
    name = models.CharField(max_length=110, unique=True)

class TodoListItem(models.Model):
    """
    Class Name : TodoListItem
    Derived Class Name: models.Model

    Descriprtion: It represents the db model of the table TodoListItem with four fields.
    Fields: id(integer, primary key, serialize), content(TextField), status(BooleanField, default=False),
            todo (TodoList)
    """
    content = models.TextField()
    status = models.BooleanField(default=False)
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
