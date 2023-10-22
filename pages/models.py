from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(600)
    priority = models.IntegerField()
    created_at = models.DateTimeField(null=True)

    # def __str__(self):
    #     return self.title 