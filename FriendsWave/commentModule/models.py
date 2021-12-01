from django.db import models
from social.models import Profil
from postModule.models import Post
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
model Comment 
"""
class Comment(Content):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)