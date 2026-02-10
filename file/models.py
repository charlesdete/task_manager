from django.db import models
from  django.conf import settings
from base.models import GenericBaseModel, State
from task.models import Task
from department.models import Department
# Create your models here.
class File(GenericBaseModel):

    file = models.FileField(upload_to="department_files/")
    state = models.ForeignKey(State, max_length=20,on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="files"
    )
    

    def __str__(self):
        return self.name