from django.db import models
from django.contrib.auth.models import AbstractUser

from topicModule.models import Topic
from social.utils import Datation

from rest_framework_simplejwt.tokens import RefreshToken



class User(AbstractUser, Datation):
    """
        model user extend default user django
    it content all informations about user of our system 
    that allow to represent each in the application
    """

    GENRE = (
        ('M', 'Masculin'),
        ('F', 'Feminin')
    )

    
    first_name = models.CharField(max_length=100) # Each User can have a first name This field content this data          
    last_npassame = models.CharField(max_length=100)  # Each User can have a last name Thisfield content this data       
    birth_date = models.DateField(null=True, blank=True) # Each User have a birth day This field content this data   
    genre = models.CharField(max_length=1, choices=GENRE) # Every human being is either male or female This field content this data   
    phone_number = models.CharField(max_length=200)  # This field content the phone number of a user
    address = models.CharField(max_length=200, blank=True)    # Every human lives in a locality this content this data
    email = models.EmailField(db_index=True, max_length=254, unique=True)  # We used an email address for contacting the user anyways and authenticate user
    username = models.CharField(db_index=True, max_length=200, unique=True)     # Each User needs a human-readable unique identifier that we can use to represent the `User` in the UI.
    is_active = models.BooleanField(default=True) # We will simply offer users a way to deactivate their account instead of letting them delete it
    is_verified = models.BooleanField(default=False)     # When a user has just created an account, he receives a confirmation email.

    class Meta:
        ordering = ['created_at', 'genre']
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):

        # This function return the full name of the User
        return  (self.first_name + ' '+self.last_name)


    def token(self):

        # This function create and return the access token and the refresh token after logging
        # This token allow to authenticate each request receive 
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Profil(Datation):

    """ 
    model Profil 
    """

    STATE_PROFIL = (
        ('A', 'Actif'),
        ('I', 'Inactive')
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT, 
        related_name='social_profil_related', 
        related_query_name='social_profils')  # 
    follow = models.ManyToManyField('self', through='social.Friend', 
        related_name = 'social_profil_related', 
        related_query_name='social_profils')
    topics_of_interest = models.ManyToManyField(Topic, through='topicModule.ProfilTopic', 
        related_name='topicModule_profil_related', 
        related_query_name='topicModule_profils')
    avatar = models.ImageField(upload_to='static/profile/%Y/%m/%d/', null=True, blank=True)  # Each profil can represent by his image
    pseudo = models.CharField(max_length=100, null=False)  # Each profile can represent by the pseudo
    state_profil = models.CharField(max_length=1, choices=STATE_PROFIL, default='A')  # Represent the state of profile 

    class Meta:
        ordering = ['created_at', 'is_active']
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

    def __str__(self):
        return self.pseudo



class Friend(Datation):
    STATUS = (
        ('A', 'ACCEPT'),
        ('D', 'DENIE')
    )

    follower = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_friend_related', related_query_name='social_friends')
    followed = models.ForeignKey(Profil, on_delete=models.PROTECT, 
        related_name='social_friend', related_query_name='socials_friends')
    status = models.CharField(max_length=1, choices=STATUS)

    class Meta:
        verbose_name = "friend"
        verbose_name_plural = "friends"

    def __str__(self):
        return self.STATUS
