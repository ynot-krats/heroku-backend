from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class SocialAccounts(models.Model):
    name = models.CharField(max_length=50,blank=False)
    email = models.EmailField(primary_key=True,blank=False)
    platform = models.CharField(max_length=50,blank=False)
    token = models.CharField(max_length=500,blank=False)

    def __str__(self):
        return self.platform


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True,blank=False)
    mobile = models.CharField(max_length=10,blank=False)
    course = models.CharField(max_length=10,blank=True)
    def __str__(self):
        return self.user.email

