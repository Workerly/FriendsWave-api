from django.db import models, utils
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from topicModule.models import Topic


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
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=30, blank=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', 'genre']

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


""" 
model Profil 
"""
class Profil(models.Models):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="belong")
    follow = models.ManyToManyField('self', through='Friend', related_name="have")
    topics_of_interest = models.ManyToManyField(Topic, through='UserTopic')
    pseudo = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="static", null=True, blank=True)
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False) 
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = "Profil"
        verbose_plural_name = "Profils"

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

    follower = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="friends")
    followed = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="friend")
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name = "friend"
        verbose_plural_name = "friends"

    def __str__(self):
        return self.STATUS
