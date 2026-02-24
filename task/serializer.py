from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id','title','description','priority' ,'state','start_date','due_date','assigned_to', 'created_by','updated_by','created_at','updated_at'
        ]