from django.db import models
from social.models import Profil, Topic
from django.utils import timezone

# Create your models here.

""" 
model Content   
"""
class Content(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="social_content_related", related_query_name='social_contents')
    content = models.TextField(max_length=1000)
    media = models.FileField(upload_to='static/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        abstract = True
        verbose_name = 'content'
        verbose_name_plural = "contents"

    def __str__(self):
        return self.content


""" 
model Post 
"""
class Post(Content):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topicModule_post_related', related_query_name='topicModule_posts')
    shares = models.ManyToManyField(Profil, through='postModule.Share', related_name='social_post_related', related_query_name='social_posts')
    likes = models.ManyToManyField(Profil, through='postModule.Like', related_name='social_likes_related', related_query_name='socials_likecontents')


    class Meta(Content.Meta):
        verbose_name = 'post'
        verbose_name_plural = "posts"


""" 
model Like 
"""
class Like(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_like_related', related_query_name='social_likes')
    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postModule_like_related', related_query_name='postModule_likes')
    like_date= models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)


"""
model share
"""
class Share(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_share_related', related_query_name='social_shares')
    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postModule_share_related', related_query_name='postModule_shares')
    share_date = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)