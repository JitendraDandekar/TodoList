from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    time = models.TimeField()

    def __str__(self):
        return self.title
