from django.db import models

from social.models import Profil
from FriendsWave.utils import Datation

# Create your models here.


class Group(Datation):
    """ 
    model Group 
    """

    VISIBILITY = (
        ('PUG', 'Public Group'),
        ('PRG', 'Private Group') 
    )
    
    members = models.ManyToManyField(Profil, through='Member', 
        related_name='social_group_related', 
        related_query_name='social_groups')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    visibilty = models.CharField(max_length=100, choices=VISIBILITY)
    link = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['created', 'name']
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name




class Member(Datation):
    """ 
    model Member 
    """
    group = models.ForeignKey(Group, on_delete=models.PROTECT, 
        related_name='groupModule_member_related', 
        related_query_name='groupModule_members')
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_member_related', 
        related_query_name='social_members')
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    class Meta:
        ordering = ['create', 'is_admin', 'is_owner']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'