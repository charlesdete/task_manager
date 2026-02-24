
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "priority", "state", "start_date", "due_date","assigned_to","created_by", "updated_by",
    "created_at","updated_at")
    search_fields = ("title", "state","assigned_to", "created_by")
    ordering = ("id","title")

