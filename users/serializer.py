from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
      
   

    class Meta:
        model = User
        fields = [
            "id", "first_name", "last_name", "email_address",
            "password", "is_staff", "is_superuser","department" , "phone_number",
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
            department = validated_data.get("department", "")
        )

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email_address"

    def validate(self, attrs):
        email = attrs.get("email_address")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,   # IMPORTANT
            password=password
        )

        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        return super().validate(attrs)


