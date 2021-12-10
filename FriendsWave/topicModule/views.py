from django import http
from rest_framework import serializers
from models import Topic, ProfilTopic
from rest_framework.serializers import Serializer

from rest_framework import viewsets
from rest_framework.generics import GenericAPIView

from serializers import UserTopicSerializer, TopicSerializer

# Create your views here.


class Topic(viewsets.ModelViewSet):
    Serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    http_method_names = ('get', 'post', 'update', 'patch', 'delete')
    lookup_field = 'id'



class ProfilTopic(viewsets.ModelViewSet):
    serializer_class = UserTopicSerializer
    queryset = ProfilTopic.objects.all()
    http_method_names = ('get', 'post', 'update', 'patch', 'delete')
    lookup_field = 'id'
