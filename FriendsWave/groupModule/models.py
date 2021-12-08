from django.db import models
from social.models import Profil
from django.utils import timezone

# Create your models here.


""" 
model Group 
"""
class Group(models.Model):
    VISIBILITY = (
        ('PUG', 'Public Group'),
        ('PRG', 'Private Group') 
    )
    
    members = models.ManyToManyField(Profil, through='Member', related_name='social_group_related', related_query_name='social_groups')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    visibilty = models.CharField(max_length=100, choices=VISIBILITY)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'name']
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name



""" 
model Member 
"""
class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groupModule_member_related', related_query_name='groupModule_members')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_member_related', related_query_name='social_members')
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now, editable=False) 
    end= models.DateTimeField(null=True)