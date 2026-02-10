from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model




User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
      
    def get_queryset(self):
        # drf-yasg sets swagger_fake_view=True when generating docs
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()
        # normal runtime queryset
        return User.objects.all()


    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "email_address",
            "password", "is_staff", "is_superuser", "phone_number",
        ]
        extra_kwargs = {"password": {"write_only": True}} #do not expose the password 

    def create(self, validated_data):
        return User.objects.create_user(
            email_address=validated_data["email_address"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            phone_number=validated_data.get("phone_number", ""),
            is_staff=validated_data.get("is_staff", False),
            is_superuser=validated_data.get("is_superuser", False),
        )

