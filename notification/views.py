from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .serializer import NotificationSerializer
from .models import Notification
from .services.notification_services import Notification_services


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all() 
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        result = Notification_services.createNotification(request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        result = Notification_services.updateNotification(pk, request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        result = Notification_services.deleteNotification(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_204_NO_CONTENT)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None, *args, **kwargs):
        result = Notification_services.getNotification(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        filters = request.query_params.dict()  # convert query params to dict
        result = Notification_services.filter_notifications(filters)
        return Response(result)
