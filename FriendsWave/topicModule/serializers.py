from django.db.models import fields
from rest_framework import serializers
from .models import Topic, UserTopic
from social.serializers import ProfilSerializers


"""
Serializer topic
"""
class TopicSerializer(serializers.ModelSerializer):
    profil =  ProfilSerializers(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = [
            'id', 
            'title', 
            'designation', 
            'created_at', 
            'profil'
        ]



"""
Serializer user topic
"""
class UserTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserTopic
        fields = []