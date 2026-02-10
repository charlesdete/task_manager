from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "id",
            "name",          
            "description",   
            "department",
            "state",
            "file",
            "uploaded_by",
            "task",
            
        ]