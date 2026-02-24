from base.services import ServiceBase
from ..models import Notification
from ..serializer import NotificationSerializer


class Notification_services(ServiceBase):
    
    manager = Notification.objects
    @staticmethod
    def createNotification(data):
        serializer = NotificationSerializer(data = data)
        if serializer.is_valid():
          new_created_notification = ServiceBase.create(**serializer)
          notification = new_created_notification.save()
          return{'success':True, 'notification':notification, 'error':None }
        return{'success':False, 'notification':None, 'error':serializer.errors}


    @staticmethod
    def updateNotification(notification_id,data):
        try:
          notification = ServiceBase.get(pk= notification_id)
        except Notification.DoesNotExist:
          return{'success': False, 'getData':None,'error':{'details': 'Notification not found'} }

        updateData = NotificationSerializer(notification, data = data, partial = True) #partial = True allows partial updates
        
        if updateData.is_valid():

          new_updated = ServiceBase.update(updateData)
          new_updated.save()
        
          return{'success': True, 'new_updated':NotificationSerializer(new_updated).data, 'error':None}
        return{'success':False, 'savedUpdate':None, 'error':updateData.errors}
    
    @staticmethod
    def deleteNotification(notification_id):
       try:  
             
            notification = ServiceBase.delete(pk= notification_id)
            serialized_notification = NotificationSerializer(notification).data
            return{'success':False, 'deleted_notification':serialized_notification,'error':{'details':'Notification does not exist'}}
       except Notification.DoesNotExist:
        
            return {
                "success": False,
                "deleted_notification": None,
                "errors": {"detail": "Notification does not exist"}
            }

    
    @staticmethod
    def getNotification(notification_id):
       try:
            notification = ServiceBase.get(pk =notification_id)
            serializer = NotificationSerializer(notification).data
            return{'success':True, 'serializer':serializer,'error':None}
       except Notification.DoesNotExist:
          return {'success':False,'serializer':None,'error': {'detail':'Notification not found'}}
       
    @staticmethod
    def get_all_notification():
       notifications =Notification.objects.all()
       serializer = NotificationSerializer(notifications, many=True).data
       return {'success':True,'notifications':serializer, 'errors':None}

    @staticmethod
    def filter_notifications(filters=None):
        if filters is None:
            filters = {}
        # apply filters or return all notifications
        return Notification.objects.filter(**filters)
