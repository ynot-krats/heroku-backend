
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from perfect.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfect/', include('perfect.urls')),
    path('auth/',CustomAuthToken.as_view())
]
