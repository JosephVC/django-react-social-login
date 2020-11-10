from django.contrib import admin
from django.urls import path

from social_login.views import FacebookLogin, GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
