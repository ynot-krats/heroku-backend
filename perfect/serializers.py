from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SocialAccounts,UserDetails
from rest_framework.authtoken.models import Token
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['username','id','first_name','email','password']

class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= SocialAccounts
        fields=['name','email','token','platform']


class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= UserDetails
        fields=['user','mobile','course']


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Token
        fields=['user','key']