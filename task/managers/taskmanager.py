from base.services import ServiceBase
from ..models import Task
 

class taskService(ServiceBase):
   
   manager = Task.objects