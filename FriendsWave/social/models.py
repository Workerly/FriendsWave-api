from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from topicModule.models import Topic
from rest_framework_simplejwt.tokens import RefreshToken


"""
  model user extend default user django
"""
class User(AbstractUser):
    GENRE = (
        ('M', 'Masculin'),
        ('F', 'Feminin')
    )

    first_name = models.CharField(max_length=100)
    last_npassame = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=1, choices=GENRE)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at', 'genre']
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return  (self.first_name + ' '+self.last_name)


    def token(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


""" 
model Profil 
"""
class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_profil_related', related_query_name='social_profils')
    follow = models.ManyToManyField('self', through='social.Friend', symmetrical = False, related_name = 'social_profil_related', related_query_name='social_profils')
    topics_of_interest = models.ManyToManyField(Topic, through='topicModule.UserTopic', related_name='topicModule_profil_related', related_query_name='topicModule_profils')
    pseudo = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="static", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'is_active']
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return self.pseudo



""" 
model Friend 
"""
class Friend(models.Model):
    STATUS = (
        ('A', 'ACCEPT'),
        ('D', 'DENIE')
    )

    follower = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_friend_related', related_query_name='social_friends')
    followed = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='social_friend', related_query_name='socials_friends')
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name = "friend"
        verbose_name_plural = "friends"

    def __str__(self):
        return self.STATUS
