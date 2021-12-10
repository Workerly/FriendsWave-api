from rest_framework import serializers

from .models import Profil, Friend, User
from topicModule.models import Topic

from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.exceptions import AuthenticationFailed


from drf_writable_nested.serializers import WritableNestedModelSerializer
import datetime


class FriendSerializers(serializers.ModelSerializer):
    """
    Serialiazer friend 
    """    
    class Meta:
        model = Friend
        fields = []


class ProfilSerializers(serializers.ModelSerializer):
    
    """
    Serializer Profil
    """
    class Meta:
        model = Profil
        fields = ['id', 'pseudo', 'avatar']
        read_only_fields = ['user']


    def validate(self, attrs):
        return super().validate(attrs)

class RegisterSerializers(serializers.ModelSerializer):
    """
    Serializer User Registration with profil
    """
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, max_length=68, min_length=6)

    class Meta:
        model = User
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'birth_date', 
            'genre',
            'phone_number', 
            'address', 
            'is_active',
            'email', 
            'username', 
            'password',
        ]
    
    def validate(self, attrs):
        if attrs['birth_date'] > datetime.date.today():
            raise serializers.ValidationError("Your birth date is not correct, please review this date")
        return super().validate(attrs)


    def create(self, validated_data):
        return User.objects.create(**validated_data)

        
    """
    methode create user with profil
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profil.objects.create(user=user, **profile_data)
        return user
    
    
    methode to update user with profil
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')

        profile = instance.profile

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()

        profile.pseudo = profile_data.get(
            'pseudo',
            profile.pseudo
        )
        profile.avatar = profile_data.get(
            'avatar',
            profile.avatar
         )
        profile.save()

        return instance
        """

class LoginSerializer(serializers.ModelSerializer):    

    username = serializers.CharField(max_length=255, min_length=5)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=68, min_length=6, write_only=True)
    
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        
        user = auth.authenticate(username=username, password=password)

        if not user:
            raise AuthenticationFailed('Invalide crusedentials, try again')

        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {
        'bad_token' : 'Token is invalid'
    }
    
    def validate(self, attrs):
        self.validate(attrs)

        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')