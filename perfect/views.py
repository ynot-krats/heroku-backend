from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.exceptions import APIException
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .models import SocialAccounts,UserDetails
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer,SocialSerializer,TokenSerializer
from rest_framework.views import exception_handler
# Create your views here.


class MatchTokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class =TokenSerializer
    @action(detail=False,methods=['GET','POST'])
    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.data['user'])
            token=self.queryset.get(user=user)
            if(token.key==request.data['key']):
                return Response(True)
        except :
            user = SocialAccounts.objects.get(email=request.data['user'])
            if(user.token==request.data['key']):
                return Response(True)
        return Response(False)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=False)
        try:
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'user_id':user.pk,
                'email': user.email})
        except :
            raise APIException('user doesnt exist')



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    def create(self, request, *args, **kwargs):
        data = self.serializer_class(data=request.data,context={'request': request})
        try:
            if(data.is_valid(raise_exception=True)):
                register =data.validated_data
                print(register)
                user = User.objects.create_user(first_name=register['first_name'],username=register['username'],
                                             email=register['email'],password=register['password'])
                Token.objects.get_or_create(user=user)
                print(request.data)
                UserDetails(user=user,mobile=request.data['mobile'],course=request.data['course']).save()
                return Response('user created')
        except :
            raise Exception('user already exists')

class SocialViewSet(viewsets.ModelViewSet):
    queryset = SocialAccounts.objects.all()
    serializer_class = SocialSerializer
    def create(self, request, *args, **kwargs):
        print(request.data)
        data = self.serializer_class(data=request.data,context={'request':request})
        try:
            if(data.is_valid(raise_exception=True)):
                data.save()
                return Response(True)
        except :
            if(self.queryset.filter(email__iexact=request.data['email']).exists()):
                self.queryset.update(token=request.data['token'])
                return Response(True)
        raise APIException(False)




