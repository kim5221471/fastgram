import os
import uuid

from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Content(BaseModel):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(default='')

def image_upload_to(instance,filename):
    ext=filename.split('.')[-1]
    return os.path.join(instance.UPLOAD_PATH,"%s.%s" % (uuid.uuid4(),ext))

class Image(BaseModel):
    UPLOAD_PATH='user-upload'

    content=models.ForeignKey(Content,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=image_upload_to)
    order=models.SmallIntegerField()

    class Meta:
        ordering=['order']