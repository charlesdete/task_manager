from django.contrib import admin
from .models import State

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # replace with actual fields in State
    search_fields = ("name",)      # fields you want searchable
    ordering = ("name",)           # default ordering 