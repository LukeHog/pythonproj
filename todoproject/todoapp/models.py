from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=False)

class TodoList(models.Model):
    child_item = models.ForeignKey(TodoListItem, on_delete=models.CASCADE)