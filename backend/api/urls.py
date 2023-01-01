from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views


app_name = "api"


urlpatterns = [
    path("", views.api_home, name="api"),
    path("auth/", obtain_auth_token, name="auth"),
]
