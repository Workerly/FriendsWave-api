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



class Community(Datation):
    """ 
        This model have the information about a community (members, visibility)
    """

    VISIBILITY = (
        ('PUG', 'Public Group'),
        ('PRG', 'Private Group') 
    )
    
    members = models.ManyToManyField(Profil, through='Member', 
        related_name='social_group_related', 
        related_query_name='social_groups')   # Each profil can be belong a community
    name = models.CharField(max_length=100)  # designation of community
    description = models.TextField(max_length=100)  # His description
    visibilty = models.CharField(max_length=100, choices=VISIBILITY)  # A community can be public or private
    link = models.CharField(max_length=100, null=True)  # Link of community

    class Meta:
        ordering = ['created', 'name']
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.name




class Member(Datation):
    """ 
    This model have all the profil belong a community 
    """
    group = models.ForeignKey(Community, on_delete=models.PROTECT, 
        related_name='groupModule_member_related', 
        related_query_name='groupModule_members')  # community of member
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_member_related', 
        related_query_name='social_members') # profil of member
    is_admin = models.BooleanField(default=False)  # the profil can be admin or not
    is_owner = models.BooleanField(default=False)   # the profil can be owner of a community

    class Meta:
        ordering = ['created', 'is_admin', 'is_owner']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'