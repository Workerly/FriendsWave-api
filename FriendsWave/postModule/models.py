from django.db import models
from social.models import Profil, Topic
from django.utils import timezone

# Create your models here.

""" 
model Content  
"""
class Content(models.Model):
    Profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="creator")
    shares = models.ManyToManyField(Profil, through='Share')
    likes = models.ManyToManyField(Profil, through='Like')
    content = models.TextField(max_length=1000)
    media = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        abstract = True
        verbose_name = 'content'
        verbose_plural_name = "contents"

    def __str__(self):
        return self.content


""" 
model Post 
"""
class Post(Content):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)



""" 
model Like 
"""
class Like(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)