from base.services import ServiceBase
from ..models import Department
 

class DepartmentService(ServiceBase):
   
   manager = Department.objects