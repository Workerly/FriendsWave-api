from django.db import models

from social.utils import Datation

class Topic(Datation):
    """ 
    model Topic 
    """
    profil = models.ForeignKey('social.Profil', on_delete=models.PROTECT, 
        related_name='social_topic_related', related_query_name='social_topics')
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['created', 'title']
        verbose_name = "topic"
        verbose_name_plural = "topics"

    def __str__(self):
        return self.title




class ProfilTopic(Datation):
    """ 
    model User_Topic 
    """
    suscriber = models.ForeignKey('social.Profil', on_delete=models.PROTECT, 
        related_name='social_usertopic_related', related_query_name='social_usertopics')
    topics = models.ForeignKey(Topic, on_delete=models.PROTECT, 
        related_name='topicModule_usertopic_related', related_query_name='topicModule_usertopics')
    reason = models.TextField(max_length=500)
    last_opened = models.DateTimeField(null=True)