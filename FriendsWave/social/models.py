from django.db import models 
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This class allows to extend the fields of the default user of django """

    GENRES = (
        ('F', 'Feminin'),
        ('M', 'Masculin')
    )

    birth_date = models.DateField() # user's date of birth
    sex = models.CharField(max_length=1, choices=GENRES) # user's sex
    address = models.CharField(max_length=30, blank=True) # user's geographic address
    phone = models.CharField(max_length=20) # user's phone number
    
class Profil(models.Model):
    """allows you to store the various user profiles"""

    def __str__(self):
        return "{}".format(self.pseudo)

    pseudo = models.CharField(max_length=100) # pseudo of profile
    profil_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True) # image of profile
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='profils') # profile user
    friends = models.ManyToManyField('self', through='Friend', related_name="have") # profile friends
    topics_followed = models.ManyToManyField('Topic', through='ProfilTopic', related_name='followers') # list of categories followed by user
    email = models.EmailField()
    is_active = models.BooleanField(default=False) # allows you to know if the profile is in use


class Friend(models.Model):
    """this class represents the friendships between the different profiles of the social network """

    STATUS = (
        ('A', 'ACCEPT'),
        ('D', 'DENIED')
    )
    follower = models.ForeignKey(Profil, on_delete = models.CASCADE, related_name="freinds") # following profile
    followed = models.ForeignKey(Profil, on_delete = models.CASCADE, related_name="freind")# profile that is followed
    status = models.CharField(max_length=1, choices=STATUS) # determine if the profile is blod
    
class Topic(models.Model):
    """this class preserves the categories which are the different themes followed """

    def __str__(self):
        return self.title

    subject = models.TextField(max_length=100) # text describing the theme to which the topic relates
    description = models.TextField(max_length=100) # topic description
    creator = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="createTopics") # profile having created the topic
    
class ProfilTopic(models.Model):
    """ this class represents the relation between a profile and a category """

    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="profilTopics")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="profilTopics") # topic followed by the profile 
    reason = models.TextField(max_length=100) # reason why the profile follows the topic
    start_date = models.DateField(auto_now_add=True) # starting date of the connection to the topic
    end_date = models.DateField(null=True) # topic monitoring stop date 
    last_opened = models.DateField()

class Group(models.Model): 
    """this class represented the profile groupings in order to exchange"""

    # each group has a name allowing it to be recognized
    nom = models.TextField(max_length=100) 

    # each group has a description that allows you to know why it was
    # as well as its objective
    description = models.TextField(max_length=100) 

    # each group has a scope that can be private or public. if it is public its contents
    # are accessible by everyone if their name is only seen by its members
    is_public = models.BooleanField() 

    # the creation date allows you to know when the group was created
    created_at = models.DateField(auto_now_add=True)

    # a group has a list of members. the information related to this relationship is recorded
    # in the Member table
    members = models.ManyToManyField(Profil, through='Member')

class Invitation(models.Model):
    """ the purpose of the class is to manage group membership invitations from one user to another """
    
    STATUS = (
        ('A', 'ACCEPT'),
        ('D', 'DENIED')
    )

    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="invitations") # profile invite
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invitations") # group concerned by the invitation
    sujbject = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="invitations_send") # profile that issued the invitation
    created_at = models.DateField(auto_now_add=True) # date of creation of the invitation
    status = models.CharField(max_length=1, choices=STATUS) # allows you to know if the profile accepts the invitation

class Member(models.Model):
    """ users can be members of different groups. 
        several information are stored in this relations which are managed in this class
    """

    group = models.ForeignKey(Group, on_delete=models.CASCADE) # designates the group concerned by the relation
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="members_set") # represents the member profile of the group
    is_admin = models.BooleanField(default=False) # desinge if the profile is administrator
    is_owner = models.BooleanField(default=False) # designates whether to create the group
    start_date = models.DateField() # subscription date
    end_date = models.DateField(null=True) # date of group dissolution

class Content(models.Model):
    """ this class allows you to keep information shared between a publication
        and a comment to simplify the work
    """

    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="%(class)ss_create") # designates the profile having created the content
    title = models.TextField(max_length=255) # designates the title of the content
    content = models.TextField(max_length=255)#r epresents the content of the content
    media = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True) # date of creation of the content

    class Meta:
        abstract = True # allows to make the class abstract 

class Post(Content):
    """ extends content and contains publications referring to a same category"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts") # designates the topic concerned by the content
    
class Comment(Content):
    """ the comment table extends from content and contains messages made on other publications
        or other comments
    """

    content = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True) # null if the comment concerns a comment
    comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='comments', null=True) # null if the comment concerns a post
    content = models.TextField(max_length=255) #the content of the comment

class Like(models.Model):
    """represents the sign of appreciation of a profile for a content"""

    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="likes") # profile having liker
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name= "likes") # post liker
    created_at = models.DateField(auto_now_add=True) # date of creation of the like

class Share(models.Model):
    """records content sharing between different profiles"""

    sender = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="emitShare") # profile at the origin of the sharing
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="receiveShare") # profile recipient of the share
    content = models.URLField(max_length=200) # designates the link to the post or comment

class Notification(models.Model):
    """this class is used by the system to inform users about actions concerning them"""

    sender = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="nofitications_sender") # profile at the origin of the notification
    recipient = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name="notifications_recipient") # profile recipient of the notification
    created_at = models.DateField(auto_now_add=True) # date of creation of the notification
    title = models.TextField(max_length=100) # notification title
    message = models.TextField(max_length=255) # notification message
    



