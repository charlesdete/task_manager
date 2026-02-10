from django.contrib.auth import authenticate
from ..serializer import UserSerializer   # adjust path if needed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from base.services import ServiceBase
from ..models import User
from rest_framework.response import Response


class UserService(ServiceBase):
    manager = User.objects

    @staticmethod
    def signup_user(data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return {"success": True, "user": user, "errors": None}
        return {"success": False, "user": None, "errors": serializer.errors}

    @staticmethod
    def signin_user(data, request):
        email = data.get("email_address")
        password = data.get("password")

        user = authenticate(request, username=email, password=password)  # works if USERNAME_FIELD = "email_address"

        if user is None:
            return {"success": False, "errors": {"error": "Invalid credentials"}}

        refresh = RefreshToken.for_user(user)
        serializer = UserSerializer(user)

        return {
            "success": True,
            "data": {
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        }
    
    @staticmethod
    def token_refresh_logic(refresh_token_str):
        try:
            refresh_token = RefreshToken(refresh_token_str)
            new_access = str(refresh_token.access_token)
            return {"success": True, "data": {"access": new_access}, "errors": None}
        except TokenError:
            return {"success": False, "data": None, "errors": {"detail": "Invalid or expired refresh token"}}
 

    @staticmethod
    def signout_user(refresh_token):
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return {"success": True, "errors": None}
        except TokenError:
            return {"success": False, "errors": {"detail": "Invalid or expired token"}}