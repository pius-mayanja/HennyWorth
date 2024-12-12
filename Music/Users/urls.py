from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'Users'

urlpatterns = [
    path('signup/', ClientSignUpView.as_view(), name='signup'),
    path("artist/",ArtistSignUpView.as_view(), name="reg"),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', Logout_view , name='logout'),
]

   

