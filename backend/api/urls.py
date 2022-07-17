from django.urls import URLPattern, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_home),
    path('auth/', obtain_auth_token),
]