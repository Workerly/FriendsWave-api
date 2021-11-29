from functools import _Descriptor
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import OneToOneField

class Profil(models.Models):
    pseudo = models.CharField(max_length=100)
    image = models.ImageField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', through='Friend')
    topics = models.ManyToManyField('Topic', through='UserTopic')
    etat = models.BooleanField(default=False)

class Friend(models.Model):
    follower = models.ForeignKey(Profil, OneToOneField = models.CASCADE)
    followed = models.ForeignKey(Profil, OneToOneField = models.CASCADE)
    status = models.BooleanField()

class Topic(models.Model):
    subject = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    creator = models.ForeignKey(Profil, on_delete=models.SET_NULL)

class UserTopic(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    choice_date = models.DateField()
    raison = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    

class Group(models.Model):
    designation = models.TextField(max_length=100)
    _description = models.TextField(max_length=100)
    type = models.BooleanField()
    created_at = models.DateField() 
    members = models.ManyToManyField(Profil, through='Member')
    private_key = models.TextField(max_length=100, null=True)

class Invitation(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sujbject = models.ForeignKey(Profil, on_delete=models.CASCADE)
    created_at = models.DateField()
    etat = models.BooleanField(default=False)
    
class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

class Content(models.Model):
    Profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()

    class Meta:
        abstract = True

class Post(Content):
    pass

class Comment(Content):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Like(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    Content = models.ForeignKey(Profil, on_delete=models.CASCADE)
    created_at = models.DateField()

class share(models.Model):
    sender = models.ForeignKey(Profil, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Notification(models.Model):
    sender = models.ForeignKey(Profil, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE)
    created_at = models.DateField()
    title = models.TextField(max_length=50)
    message = models.TextField(max_length=100)
    



