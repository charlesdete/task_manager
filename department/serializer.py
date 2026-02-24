from rest_framework import serializers
from .models import Department
from users.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    department_members = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all(), required=False
    )

    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'department_members']