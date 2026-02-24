from base.services import ServiceBase
from ..models import Task
from ..serializer import TaskSerializer

class Task_services(ServiceBase):

    manager = Task.objects

    @staticmethod
    def createTask(data):
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            task = serializer.save()
            return {"success": True, "task": TaskSerializer(task).data}
        return {"success": False, "errors": serializer.errors}

    @staticmethod
    def updateTask(task_id, data):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return {"success": False, "task": None, "errors": {"detail": "Task not found"}}

        serializer = TaskSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            updated_task = serializer.save()
            return {"success": True, "task": TaskSerializer(updated_task).data}
        return {"success": False, "task": None, "errors": serializer.errors}

    @staticmethod
    def deleteTask(task_id):
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            return {"success": True, "task_id": str(task_id)}
        except Task.DoesNotExist:
            return {"success": False, "task_id": None, "errors": {"detail": "Task does not exist"}}

    @staticmethod
    def getTask(task_id):
        try:
            task = Task.objects.get(pk=task_id)
            serializer = TaskSerializer(task).data
            return {"success": True, "task": serializer}
        except Task.DoesNotExist:
            return {"success": False, "task": None, "errors": {"detail": "Task not found"}}

    @staticmethod
    def get_all_task():
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True).data
        return {"success": True, "tasks": serializer}

    @staticmethod
    def filter_tasks(filters=None):
        if filters is None:
            filters = {}
        tasks = Task.objects.filter(**filters)
        serializer = TaskSerializer(tasks, many=True).data
        return {"success": True, "tasks": serializer}
