from django.db import models

from social.models import Profil
from social.utils import Datation

# Create your models here.


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