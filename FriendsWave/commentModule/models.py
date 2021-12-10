from django.db import models
from django_extensions.db.models import TimeStampedModel

from social.models import Profil
from postModule.models import Post

import uuid



class Datation(TimeStampedModel):
    """
        This class content a timestamp reprensenting when the object was created and was last updated.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    h_objects = models.Manager()


class Content(Datation):

    """ 
         An abstract model that represent the content such as post or comment   
    """
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, 
        related_name="socials_content", 
        related_query_name='socials_contents')  # the profil can comment a content
    content = models.TextField(max_length=1000) # the content 
    media = models.FileField(upload_to='static/%Y/%m/%d/', null=True, blank=True)  # the media of the content

    class Meta:
        ordering = ['created']
        abstract = True
        verbose_name = 'content'
        verbose_name_plural = "contents"

    def __str__(self):
        return self.content


class Comment(Content):
    """ 
        This model have information about the comment of one profil 
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name='postModule_comment_related', 
    related_query_name='postModule_comments')  # the post concern
    class Meta(Content.Meta):
        verbose_name = 'comment'
        verbose_name_plural = "comments"