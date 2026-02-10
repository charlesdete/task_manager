
from django.contrib import admin
from .models import Task
from base.admin_site import admin_site  # your custom admin site instance

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "priority", "state", "start_date", "due_date","assigned_to","created_by", "updated_by",
    "created_at","updated_at")
    search_fields = ("title", "state","assigned_to", "created_by")
    ordering = ("id","title")

# Register User with the custom admin site
admin_site.register(Task, TaskAdmin)
