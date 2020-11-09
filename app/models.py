from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, editable=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        try:
            # Check to see if this field is filled in or left empty
            # In case of empty, an exception is raised!
            # As a result, it will be set to value of get_current_user() in the exception block.
            if (self.created_by):
                pass
        except:
            self.created_by = get_current_user()
        super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)