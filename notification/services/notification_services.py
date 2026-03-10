from base.services import ServiceBase
from ..models import Notification
from ..serializer import NotificationSerializer
from django.core.mail import send_mail
from django.conf import settings
from users.models import User



class Notification_services(ServiceBase):
    manager = Notification.objects

    @staticmethod
    def createNotification(data):
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            notification = serializer.save()

             #  Send email to the assigned user
            try:
                user = User.objects.get(pk=notification.user_id)
                send_mail(
                    subject=notification.title,
                    message=notification.message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email_address],
                    fail_silently=False,
                )

                print(f"Email sent to {user.email_address} for notification {notification.id}")
            except User.DoesNotExist:
                pass
            except Exception as e:
                print(f"Email sending failed: {e}")


            return {"success": True, "notification": NotificationSerializer(notification).data, "error": None}
        return {"success": False, "notification": None, "error": serializer.errors}

    @staticmethod
    def updateNotification(notification_id, data):
        try:
            notification = Notification.objects.get(pk=notification_id)
        except Notification.DoesNotExist:
            return {"success": False, "notification": None, "error": {"detail": "Notification not found"}}

        serializer = NotificationSerializer(notification, data=data, partial=True)
        if serializer.is_valid():
            updated = serializer.save()
            return {"success": True, "notification": NotificationSerializer(updated).data, "error": None}
        return {"success": False, "notification": None, "error": serializer.errors}

    @staticmethod
    def deleteNotification(notification_id):
        try:
            notification = Notification.objects.get(pk=notification_id)
            notification.delete()
            return {"success": True, "notification_id": str(notification_id), "error": None}
        except Notification.DoesNotExist:
            return {"success": False, "notification_id": None, "error": {"detail": "Notification does not exist"}}

    @staticmethod
    def getNotification(notification_id):
        try:
            notification = Notification.objects.get(pk=notification_id)
            return {"success": True, "notification": NotificationSerializer(notification).data, "error": None}
        except Notification.DoesNotExist:
            return {"success": False, "notification": None, "error": {"detail": "Notification not found"}}

    @staticmethod
    def get_all_notifications():
        notifications = Notification.objects.all()
        return {"success": True, "notifications": NotificationSerializer(notifications, many=True).data, "error": None}

    @staticmethod
    def filter_notifications(filters=None):
        if filters is None:
            filters = {}
        notifications = Notification.objects.filter(**filters)
        return {"success": True, "notifications": NotificationSerializer(notifications, many=True).data, "error": None}