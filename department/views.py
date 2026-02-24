from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .serializer import DepartmentSerializer
from users.serializer import UserSerializer

from .models import Department
from .services.department_services import Department_services



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all() 
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


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
        filters = request.query_params.dict()
        departments = Department_services.filter_departments(filters)
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


    def members(self, request, pk=None):
        department = self.get_object()
        users = department.members.all()  # assuming FK from User → Department
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)