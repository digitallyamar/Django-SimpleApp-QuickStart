from django.contrib import admin
from .models import Todo

# Register your models here.

# We need to create custom Admin form to be able to show items from list_display in the panel.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_by', 'created_at')

admin.site.register(Todo, TodoAdmin)