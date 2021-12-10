from django.db import models
from django_extensions.db.models import TimeStampedModel

from social.models import Profil, Topic

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
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, related_name="social_content_related",
        related_query_name='social_contents') # Each profil can create the content 
    likes = models.ManyToManyField(Profil, through='postModule.Like', 
        related_name='social_likes_related', related_query_name='socials_likecontents')  # The profil can like content
    content = models.TextField(max_length=1000) # the object or message
    media = models.FileField(upload_to='static/content/%Y/%m/%d/', null=True, blank=True) # The media that illustrate the content
    numbers_likes = models.PositiveBigIntegerField()    # this field contains number of likes of a content
    numbers_dislikes = models.PositiveBigIntegerField()  # this field contains number of dislikes of a content

    class Meta:
        ordering = ['created']
        abstract = True
        verbose_name = 'content'
        verbose_name_plural = "contents"

    def __str__(self):
        return self.content



class Post(Content):
    """ 
        This model post concern all publication 
    """
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, 
        related_name='topicModule_post_related', related_query_name='topicModule_posts') # A post concern a topic
    shares = models.ManyToManyField(Profil, through='postModule.Share', 
        related_name='social_post_related', related_query_name='social_posts')  # The profil can share post
    number_shares = models.PositiveBigIntegerField()       # this field contains the number shares of a post


    class Meta(Content.Meta):
        verbose_name = 'post'
        verbose_name_plural = "posts"



class Like(Datation):
    """ 
        This mdel content all informations about likes of a content
    """
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_like_related', related_query_name='social_likes') # profil like post
    content = models.ForeignKey(Post, on_delete=models.PROTECT, 
        related_name='postModule_like_related', related_query_name='postModule_likes') # A content can be liking



class Share(Datation):
    """
        This model content all informations about shares of a post
    """
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_share_related', related_query_name='social_shares') # Profil can share post
    content = models.ForeignKey(Post, on_delete=models.PROTECT, 
        related_name='postModule_share_related', related_query_name='postModule_shares') # A content can be sharing with other