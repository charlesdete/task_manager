from django.contrib import admin
from .models import User
from base.admin_site import admin_site  # your custom admin site instance

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "is_active", "is_staff", "is_superuser")
    search_fields = ("first_name", "last_name", "email_address")
    ordering = ("first_name",)

# Register User with the custom admin site
admin_site.register(User, UserAdmin)
