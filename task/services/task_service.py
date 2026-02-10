from base.services import ServiceBase
from ..models import Task
from ..serializer import TaskSerializer


class Task_services(ServiceBase):
    
    manager = Task.objects
    @staticmethod
    def createTask(data):
        serializer = TaskSerializer(data = data)
        if serializer.is_valid():
          new_created_task = ServiceBase.create(**serializer)
          task = new_created_task.save()
          return{'success':True, 'task':task, 'error':None }
        return{'success':False, 'task':None, 'error':serializer.errors}


    @staticmethod
    def updateTask(task_id,data):
        try:
          task = ServiceBase.get(pk= task_id)
        except Task.DoesNotExist:
          return{'success': False, 'getData':None,'error':{'details': 'Task not found'} }

        updateData = TaskSerializer(task, data = data, partial = True) #partial = True allows partial updates
        
        if updateData.is_valid():

          new_updated = ServiceBase.update(updateData)
          new_updated.save()
        
          return{'success': True, 'new_updated':TaskSerializer(new_updated).data, 'error':None}
        return{'success':False, 'savedUpdate':None, 'error':updateData.errors}
    
    @staticmethod
    def deleteTask(task_id):
       try:  
             
            task = ServiceBase.delete(pk= task_id)
            serialized_task = TaskSerializer(task).data
            return{'success':False, 'deleted_task':serialized_task,'error':{'details':'Task does not exist'}}
       except Task.DoesNotExist:
        
            return {
                "success": False,
                "deleted_task": None,
                "errors": {"detail": "Task does not exist"}
            }

    
    @staticmethod
    def getTask(task_id):
       try:
            task = ServiceBase.get(pk =task_id)
            serializer = TaskSerializer(task).data
            return{'success':True, 'serializer':serializer,'error':None}
       except Task.DoesNotExist:
          return {'success':False,'serializer':None,'error': {'detail':'Task not found'}}
       
    @staticmethod
    def get_all_task():
       tasks =Task.objects.all()
       serializer = TaskSerializer(tasks, many=True).data
       return {'success':True,'tasks':serializer, 'errors':None}

    @staticmethod
    def filter_tasks(filters):
       """
        filters: dict of field lookups, e.g. {"status": "open"} or {"title__icontains": "API"}
        """

       tasks = ServiceBase.filter(**filters)
       serializer = TaskSerializer(tasks, many= True).data
       return {'success':True,'tasks':serializer, 'errors':None}