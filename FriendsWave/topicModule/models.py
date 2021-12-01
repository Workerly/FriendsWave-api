from django.db import models
from social.models import Profil
from django.utils import timezone

# Create your models here.

""" 
model Topic 
"""
class Topic(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    profil = models.ForeignKey(Profil, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'title']
        verbose_name = "topic"
        verbose_plural_name = "topics"

    def __str__(self):
        return self.title



""" 
model User_Topic 
"""
class UserTopic(models.Model):
    suscribers = models.ForeignKey(Profil, on_delete=models.CASCADE)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    raison = models.TextField(max_length=500)
    last_opened = models.DateTimeField(null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    end= models.DateField(null=True)