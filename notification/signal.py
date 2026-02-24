from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Notification


@receiver(post_save, sender=Notification)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        user = instance.user

        send_mail(
            subject=instance.title,
            message=instance.message,
            from_email=None,
            recipient_list=[user.email_address],
            fail_silently=False,
        )