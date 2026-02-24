from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import User
from .serializer import UserSerializer, EmailTokenObtainPairSerializer
from .services.user_services import UserService



class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action in ["signup", "signin","list"]:
            return [AllowAny()]
        return [IsAuthenticated()]


    

    def get_queryset(self):
        queryset = super().get_queryset()
        is_staff = self.request.query_params.get("is_staff")
        if is_staff in ["true", "True", "1"]:
            queryset = queryset.filter(is_staff=True)
        elif is_staff in ["false", "False", "0"]:
            queryset = queryset.filter(is_staff=False)
        return queryset


    @action(detail=False, methods=['post'])
    def signup(self, request):
        
        result = UserService.signup_user(request.data)

        if result["success"]:
            user_data = UserSerializer(result["user"]).data
            return Response(
                {"message": "Account created successfully", "user": user_data},
                status=status.HTTP_201_CREATED
            )

        return Response(result["errors"], status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=False, methods=['post'])
    def signin(self, request):
       
        result = UserService.signin_user(request.data, request)
        if result["success"]:
            return Response(result["data"], status=status.HTTP_200_OK)

        return Response(result["errors"], status=status.HTTP_401_UNAUTHORIZED)



class RefreshTokenView(APIView):
   
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        result = UserService.token_refresh_logic(refresh_token)

        if result["success"]:
            return Response(result["data"], status=status.HTTP_200_OK)
        return Response(result["errors"], status=status.HTTP_401_UNAUTHORIZED)



class CookieTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data
        access = data.get("access")
        refresh = data.get("refresh")

        payload = {
            "message": "Login success",
            "access": access,
            "refresh": refresh,
        }

        resp = Response(payload)
        # Set cookies
        resp.set_cookie("access_token", access, httponly=True, samesite="None", secure=False, path="/")
        resp.set_cookie("refresh_token", refresh, httponly=True, samesite="None", secure=False, path="/")
        return resp



class CookieTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        refresh = request.COOKIES.get("refresh_token")
        if not refresh:
            return Response({"detail": "No refresh token cookie"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={"refresh": refresh})
        serializer.is_valid(raise_exception=True)
        access = serializer.validated_data["access"]

        resp = Response({"access": access})
        resp.set_cookie("access_token", access, httponly=True, samesite="None", secure=False, path="/")
        return resp



class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = Response({"message": "Logout success"}, status=status.HTTP_200_OK)
        response.delete_cookie("access_token", path="/")
        response.delete_cookie("refresh_token", path="/")
        return response
