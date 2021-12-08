from django.db import models
from django.db.models.base import Model
from django.db.models.fields import related
from django.db.models.fields.related import OneToOneField, RelatedField


class Profil(models.Models):
    pseudo = models.CharField(max_length=100) #pseudo of profile
    profil_image = models.ImageField() #image of profile
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='profils') #profile user
    friends = models.ManyToManyField('self', through='Friend', related_name="freinds_set") #profile friends
    topics = models.ManyToManyField('Topic', through='UserTopic', related_name='followers')
    email = models.EmailField()
    is_active = models.BooleanField(default=False) #allows you to know if the profile is in use

class Friend(models.Model):
    follower = models.ForeignKey(Profil, on_delete = models.CASCADE, related_name="followers") #following profile
    followed = models.ForeignKey(Profil, on_delete = models.CASCADE, related_name="followeds")#profile that is followed
    status = models.BooleanField() #determine if the profile is blod

class Topic(models.Model):
    subject = models.TextField(max_length=100) #text describing the theme to which the topic relates
    description = models.TextField(max_length=100) #topic description
    creator = models.ForeignKey(Profil, on_delete=models.SET_NULL, related_name="topics") #profile having created the topic

class ProfilTopic(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="profilTopics")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="profilTopics") #topic followed by the profile 
    reason = models.TextField(max_length=100) #reason why the profile follows the topic
    start_date = models.DateField(auto_now_add=True) #starting date of the connection to the topic
    end_date = models.DateField(null=True) #topic monitoring stop date
    last_opened = models.DateField()

class Group(models.Model):
    nom = models.TextField(max_length=100) #group title
    description = models.TextField(max_length=100) #textual description of the reason for the creation of the group
    is_public = models.BooleanField() #allows you to know if the group is private or public
    created_at = models.DateField(auto_now_add=True) #date of creation of the group
    members = models.ManyToManyField(Profil, through='Member',related_name="group_set") #list of group members
    private_key = models.TextField(max_length=150, null=True)#private key to the group

class Invitation(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="invitations_received") #profile invite
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invitations") #group concerned by the invitation
    sujbject = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="invitations_send") #profile that issued the invitation
    created_at = models.DateField(auto_now_add=True) #date of creation of the invitation
    etat = models.BooleanField(default=False) #allows you to know if the profile accepts the invitation

class Member(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE) #designates the group concerned by the relation
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="members_set") #represents the member profile of the group
    is_admin = models.BooleanField(default=False) #desinge if the profile is administrator
    is_owner = models.BooleanField(default=False) #designates whether to create the group
    start_date = models.DateField() #subscription date
    end_date = models.DateField(null=True) #date of group dissolution

class Content(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="%(class)ss_create") #designates the profile having created the content
    title = models.TextField(max_length=255) #designates the title of the content
    content = models.TextField(max_length=255)#represents the content of the content

    class Meta:
        abstract = True #allows to make the class abstract

class Post(Content):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts") #designates the topic concerned by the content
    
class Comment(Content):
    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True) #represents the content of the comment
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True) #represents the content of the comment

class Like(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="likes") #profile having liker
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "likes") #post liker
    created_at = models.DateField(auto_now_add=True) #date of creation of the like

class Share(models.Model):
    sender = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="sender_sets") #profile at the origin of the sharing
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="share_set") #profile recipient of the share
    content = models.URLField(max_length=200) #designates the link to the post or comment

class Notification(models.Model):
    sender = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="nofitications_sender") #profile at the origin of the notification
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="notifications_recipient") #profile recipient of the notification
    created_at = models.DateField(auto_now_add=True)
    title = models.TextField(max_length=100) #notification title
    message = models.TextField(max_length=255) #notification message
    



