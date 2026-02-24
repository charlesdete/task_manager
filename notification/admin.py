
from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ( 'id','title','message','user','notification_type',
            'is_read', 'state',"created_at","updated_at")
    search_fields = ("title", "state")
    ordering = ("id","title", "created_at")

# Register User with the custom admin site

