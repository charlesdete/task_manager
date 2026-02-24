from base.services import ServiceBase
from ..models import Department
from ..serializer import DepartmentSerializer


class Department_services(ServiceBase):
    
    manager = Department.objects
    
    @staticmethod
    def createDepartment(data):
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid():
            dept = serializer.save()
            return {
                'success': True,
                'department': DepartmentSerializer(dept).data,
                'error': None
            }
        return {
            'success': False,
            'department': None,
            'error': serializer.errors
        }

    @staticmethod
    def updateDepartment(department_id,data):
        try:
          department = ServiceBase.get(pk= department_id)
        except Department.DoesNotExist:
          return{'success': False, 'getData':None,'error':{'details': 'Department not found'} }

        updateData =DepartmentSerializer(department, data = data, partial = True) #partial = True allows partial updates
        
        if updateData.is_valid():

          new_updated = ServiceBase.update(updateData)
          new_updated.save()
        
          return{'success': True, 'new_updated':DepartmentSerializer(new_updated).data, 'error':None}
        return{'success':False, 'savedUpdate':None, 'error':updateData.errors}
    
    @staticmethod
    def deleteDepartment(department_id):
       try:  
             
            department= ServiceBase.delete(pk= department_id)
            serialized_department = DepartmentSerializer(department).data
            return{'success':False, 'deleted_department':serialized_department,'error':{'details':'Department does not exist'}}
       except Department.DoesNotExist:
        
            return {
                "success": False,
                "deleted_department": None,
                "errors": {"detail": "Department does not exist"}
            }

    
    @staticmethod
    def getDepartment(department_id):
       try:
            department = ServiceBase.get(pk =department_id)
            serializer = DepartmentSerializer(department).data
            return{'success':True, 'serializer':serializer,'error':None}
       except Department.DoesNotExist:
          return {'success':False,'serializer':None,'error': {'detail':'Department not found'}}
       
    @staticmethod
    def get_all_department():
       departments =Department.objects.all()
       serializer = DepartmentSerializer(departments, many=True).data
       return {'success':True,'departments':serializer, 'errors':None}

    @staticmethod
    def filter_departments(filters=None):
        if filters is None:
            filters = {}
        return Department.objects.filter(**filters)
