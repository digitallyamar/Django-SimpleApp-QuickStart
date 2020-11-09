from django.db import models
from crum import get_current_user
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)

    def save(self, *args, **kwargs):
        created_by = get_current_user()
        super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title