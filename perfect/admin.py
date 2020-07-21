from django.contrib import admin
from .models import SocialAccounts,UserDetails
# Register your models here.
admin.site.register(SocialAccounts)
admin.site.register(UserDetails)