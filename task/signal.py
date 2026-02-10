from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMessage

from .models import Task
from notification.models import Notification

@receiver(post_save, sender=Task)
def task_assigned_handler(sender, instance, created, **kwargs):
    if not created:
        return

    # 1 Create in-app notification
    Notification.objects.create(
        user=instance.assigned_to,
        message=f"You have been assigned a task: {instance.title}"
    )

    # 2 Prepare email
    email = EmailMessage(
        subject=f"New Task Assigned: {instance.title}",
        body=f"""
Hello {instance.assigned_to.first_name},

You have been assigned a new task.

Title: {instance.title}
Description: {instance.description}

Please log in to the system to accept or reject the task.
""",
        to=[instance.assigned_to.email_address],
    )

    # 3 Attach files IF they exist
    for attachment in instance.attachments.all():
        email.attach_file(attachment.file.path)

    # 4 Send email
    email.send(fail_silently=False)
