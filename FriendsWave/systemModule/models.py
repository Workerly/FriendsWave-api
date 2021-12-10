from django.db import models
from django_extensions.db.models import TimeStampedModel

from social.models import Profil

import uuid

class Datation(TimeStampedModel):
    """
        This class content a timestamp reprensenting when the object was created and was last updated.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    h_objects = models.Manager()



class Notification(Datation):
    """ 
        This model content the notification created by the system
    """
    receiver = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_notification_related', 
        related_query_name='social_notifications')  # The profil can receive the notification
    title = models.CharField(max_length=50)     # the title about the notification
    message = models.TextField(max_length=100)  # the message about the notification
    
    class Meta:
        ordering =['created']
    

    def __str__(self) -> str:
        return self.title