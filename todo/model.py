from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.title
