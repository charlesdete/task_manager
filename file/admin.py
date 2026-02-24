from django.contrib import admin
from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description', 'state', 'file','uploaded_by','task',)
    list_filter = ('state','file','uploaded_by')
    search_fields = ('name','state','uploaded_by')


