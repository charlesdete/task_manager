from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .serializer import TaskSerializer
from .models import Task
from .services.task_service import Task_services


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all() 
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        result = Task_services.createTask(request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        result = Task_services.updateTask(pk, request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        result = Task_services.deleteTask(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_204_NO_CONTENT)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None, *args, **kwargs):
        result = Task_services.getTask(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        filters = request.query_params.dict()  # convert query params to dict
        result = Task_services.filter_tasks(filters)
        return Response(result)
