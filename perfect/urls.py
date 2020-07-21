from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet,SocialViewSet,MatchTokenViewSet
router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('social',SocialViewSet)
router.register('checkToken',MatchTokenViewSet)
urlpatterns = [
    path('',include(router.urls)),

]