from django.db import models

from social.models import Profil, Topic
from social.utils import Datation

# Create your models here.

class Content(Datation):

    """ 
    model Content   
    """
    profil = models.ForeignKey(Profil, on_delete=models.PROTECT, related_name="social_content_related",
        related_query_name='social_contents')
    content = models.TextField(max_length=1000)
    media = models.FileField(upload_to='static/content/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        ordering = ['created']
        abstract = True
        verbose_name = 'content'
        verbose_name_plural = "contents"

    def __str__(self):
        return self.content



class Post(Content):
    """ 
    model Post 
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, 
        related_name='topicModule_post_related', related_query_name='topicModule_posts')
    shares = models.ManyToManyField(Profil, through='postModule.Share', 
        related_name='social_post_related', related_query_name='social_posts')
    likes = models.ManyToManyField(Profil, through='postModule.Like', 
        related_name='social_likes_related', related_query_name='socials_likecontents')


    class Meta(Content.Meta):
        verbose_name = 'post'
        verbose_name_plural = "posts"



class Like(Datation):
    """ 
    model Like 
    """
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, 
        related_name='social_like_related', related_query_name='social_likes')
    content = models.ForeignKey(Post, on_delete=models.CASCADE, 
        related_name='postModule_like_related', related_query_name='postModule_likes')



class Share(Datation):
    """
    model share
    """
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, 
        related_name='social_share_related', related_query_name='social_shares')
    content = models.ForeignKey(Post, on_delete=models.CASCADE, 
        related_name='postModule_share_related', related_query_name='postModule_shares')