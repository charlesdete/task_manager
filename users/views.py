from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .services.user_services import UserService
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView
from .models import User



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["signup", "signin"]:
            return [AllowAny()]
        return [IsAuthenticated()]


    @action(detail=False, methods=['post'])
    def signin(self, request):
            result = UserService.signin_user(request.data, request)  #  pass request too
            if result["success"]:
                return Response(result["data"], status=status.HTTP_200_OK)
            return Response(result["errors"], status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user =UserService.create(serializer)
            user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_406_NOT_ACCEPTABLE)


    class RefreshTokenView(APIView):
        def post(self, request, *args, **kwargs):
            refresh_token = request.data.get("refresh")
            result = UserService.token_refresh_logic(refresh_token)

            if result["success"]:
                return Response(result["data"], status=status.HTTP_200_OK)
            return Response(result["errors"], status=status.HTTP_401_UNAUTHORIZED)
