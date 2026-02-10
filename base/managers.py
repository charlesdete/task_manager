from .services import ServiceBase
from .models import User

class UserService(ServiceBase):
    manager = User.objects




# class TaskService(ServiceBase):
#     manager = Task.objects
# class  NotificationService(ServiceBase):
#     manager = Notification.objects

