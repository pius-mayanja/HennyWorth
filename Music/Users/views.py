from django.shortcuts import render
from .forms import ClientSignUpForm, ArtistSignUpForm, LoginForm
from django.views.generic import CreateView
from .models import User
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
import django.contrib.auth.views as auth_views
from django.contrib.auth import login



class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'user/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('Users:login')

class ArtistSignUpView(CreateView):
    model = User
    form_class = ArtistSignUpForm
    template_name = 'user/art_reg.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'artist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('Users:login')

def Logout_view(request):
    logout(request)
    return redirect('Dashboard:homepage')

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            user = self.request.user
            if user.is_authenticated:
                if user.is_client:
                    return reverse('Dashboard:homepage')
                elif user.is_artist:
                    return reverse('Artist:home')
        return reverse('User:login')