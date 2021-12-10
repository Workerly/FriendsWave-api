from django.db import models
from django_extensions.db.models import TimeStampedModel

import uuid

class Datation(TimeStampedModel):
    """
        This class content a timestamp reprensenting when the object was created and was last updated.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    h_objects = models.Manager()

class Topic(Datation):
    """ 
        This have the information about a topic 
    """
    profil = models.ForeignKey('social.Profil', on_delete=models.PROTECT, 
        related_name='social_topic_related', related_query_name='social_topics')   # the profil can suscribe to topic
    title = models.TextField(max_length=100)    # the title of topic
    description = models.TextField(max_length=100) # his description

    class Meta:
        ordering = ['created', 'title']
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.title




class ProfilTopic(Datation):
    """ 
        This model have all informations about the suscriber to a topic
    """
    suscriber = models.ForeignKey('social.Profil', on_delete=models.PROTECT, 
        related_name='social_usertopic_related', related_query_name='social_usertopics')  # the suscriber 
    topics = models.ForeignKey(Topic, on_delete=models.PROTECT, 
        related_name='topicModule_usertopic_related', related_query_name='topicModule_usertopics')  # topic suscribe
    reason = models.TextField(max_length=500) # if the profil stop to follow a topic
