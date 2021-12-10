from django.db.models.query import QuerySet
from django.http import response
from rest_framework import permissions, generics, viewsets, status
from rest_framework import serializers
from rest_framework.parsers import JSONParser, FileUploadParser, FormParser, MultiPartParser
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action, permission_classes

from social.models import Profil, User
from social.serializers import LoginSerializer, RegisterSerializers, ProfilSerializers, LogoutSerializer

from rest_framework_simplejwt.tokens import RefreshToken

from social.utils import Util

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings
import jwt
from django.contrib import auth




"""
Authenticate Token 
"""
class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializers(user)
        return response.Response({'user': serializer.data})

        

"""
View registration user 
"""
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializers

    def post(self, request):
    
        serializer = RegisterSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            
            user = User.objects.get(email=user_data['email'])

            token = RefreshToken.for_user(user).access_token
        
            current_site = get_current_site(request)
            relativeLink = reverse('verify-email')
            
            #construct the email and send it
            absurl = 'http://'+str(current_site)+relativeLink+"?token"+str(token)
            email_body = 'Hi' + user.username+ 'Use the link below to vrify your email\n'+ absurl
            data = {'email_body':email_body, 
                    'to_email': user.email,
                    'email_subject': 'Verify your email'}
            Util.send_email(data) 

            return Response(user_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Verify email registration
"""
class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY) 
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfuly activated'}, status=status.HTTP_200_OK)
      
        except jwt.ExpiredSignatureError as identifier:
            return Response({'eroor': 'Activation expired'}, status= status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'email', 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)



class ProfilView(generics.ListCreateAPIView):
    Serializer_class = ProfilSerializers


    def get_queryset(self):
        
        return super().get_queryset()
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProfilSerializers(queryset, many=True)
        return Response(serializer.data)

"""
View registration user with profile use viewset
"""
class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializers
    parsers_classes = (JSONParser, FormParser, MultiPartParser)
    http_method_names =('post', 'get', 'put', 'patch', 'delete') 
    queryset = User.objects.all()
    lookup_field = 'id'

    def post(self, request):
    
        serializer = RegisterSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            
            user = User.objects.get(email=user_data['email'])

            token = RefreshToken.for_user(user).access_token
        
            current_site = get_current_site(request)
            relativeLink = reverse('verify-email')
            
            #construct the email and send it
            absurl = 'http://'+str(current_site)+relativeLink+"?token"+str(token)
            email_body = 'Hi' + user.username+ 'Use the link below to vrify your email\n'+ absurl
            data = {'email_body':email_body, 
                    'to_email': user.email,
                    'email_subject': 'Verify your email'}
            Util.send_email(data) 

            return Response(user_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    """@action(detail=True, methods=['GET'])
    def profiles(self, request, pk=None):
        user = self.get_object()
        profile = Profil.objects.filter(user=user)
        Serializer = ProfilSerializers(profile, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)
    """

    """@action(detail=True, methods=['post', 'patch'], name='profile')
    def profile(self, request, pk=None):
        user = self.get_object()
        data = request.data
        data['user'] = user.id
        serializer = ProfilSerializers(data, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400) 
    """


"""
View authenticate user 
"""
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


"""
view logout
"""
class LogoutView(APIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
        