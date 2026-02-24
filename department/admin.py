from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name','description','member_list')
    list_filter = ('id','name')
    search_fields = ('id','name')

    def member_list(self, obj):
        return ", ".join([user.username for user in obj.department_members.all()])
    member_list.short_description = "Members"

