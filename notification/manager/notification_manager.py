from  base.services import ServiceBase
from ..models import Notification

class  NotificationManager(ServiceBase):
    manager = Notification.objects