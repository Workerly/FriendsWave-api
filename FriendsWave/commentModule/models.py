from django.db import models

from social.models import Profil
from postModule.models import Post
from social.utils import Datation

# Create your models here.


class Content(Datation):

    """ 
    model Content   
    """
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, 
        related_name="socials_content", 
        related_query_name='socials_contents')
    content = models.TextField(max_length=1000)
    media = models.FileField(upload_to='static/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        ordering = ['created']
        abstract = True
        verbose_name = 'content'
        verbose_name_plural = "contents"

    def __str__(self):
        return self.content


class Comment(Content):
    """ 
    model Comment 
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, 
    related_name='postModule_comment_related', 
    related_query_name='postModule_comments')


    class Meta(Content.Meta):
        verbose_name = 'comment'
        verbose_name_plural = "comments"