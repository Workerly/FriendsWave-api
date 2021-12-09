from django.db import models
from django_extensions.db.models import TimeStampedModel

from social.models import Profil

import uuid

class Datation(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    h_objects = models.Manager()



class Notification(Datation):
    """ 
    model Notification 
    """
    receiver = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_notification_related', 
        related_query_name='social_notifications')
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    
    class Meta:
        ordering =['created']
    

    def __str__(self) -> str:
        return self.title