from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=110, primary_key=True)

class TodoListItem(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=False)
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
