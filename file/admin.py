from django.contrib import admin
from .models import File
from base.admin_site import admin_site  # your custom admin site instance

class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description', 'state', 'file','uploaded_by','task',)
    list_filter = ('state','file','uploaded_by')
    search_fields = ('name','state','uploaded_by')

# Register User with the custom admin site
admin_site.register(File, FileAdmin)
