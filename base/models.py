from django.db import models
import uuid


# Create your models here.
 
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)



    class Meta:
        abstract = True

class GenericBaseModel(BaseModel):

    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True, null=True)

    class Meta(object):
        abstract = True

class State(GenericBaseModel):

    def __str__(self):
        return '%s' % self.name
    
    class Meta(object):
        verbose_name= 'State'
        verbose_name_plural = 'States'

class task_identity_type(GenericBaseModel):
    
    def __str__(self):
        return self.name