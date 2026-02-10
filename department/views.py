from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import DepartmentSerializer
from .models import Department
from .services.department_services import Department_services



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all() 
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        result = Department_services.createDepartment(request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        result = Department_services.updateDepartment(pk, request.data)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, *args, **kwargs):
        result = Department_services.deleteDepartment(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_204_NO_CONTENT)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None, *args, **kwargs):
        result = Department_services.getDepartment(pk)
        if result["success"]:
            return Response(result, status=status.HTTP_200_OK)
        return Response(result, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        result = Department_services.filter_departments()
        return Response(result, status=status.HTTP_200_OK)