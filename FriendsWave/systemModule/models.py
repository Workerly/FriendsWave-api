from django.db import models
from social.models import Profil
from django.utils import timezone
# Create your models here.

""" 
model Notification 
"""
class Notification(models.Model):
    receiver = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_notification_related', related_query_name='social_notifications')
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['created_at']
    

    def __str__(self) -> str:
        return self.title