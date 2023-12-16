from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.util import random_hex
from .forms import UserRegistrationForm, UserLoginForm  
from .models import LoginStats, LogoutStats, UserProfile
#from django_otp.plugins.otp_totp.views import VerifyTOTPView

def home(request):
    return render(request, 'authapp/home.html')

def auth(request):
    return render(request, 'authapp/auth.html')

def user_login(request):
    form = UserLoginForm()  # Instantiate the form
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                create_login_statistic(request.user, 'username/password', True)
                return redirect('dashboard')
            else:
                #create_login_statistic(None, 'username/password', False)
                #create_username_password_statistic(username, False)
                messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'authapp/login.html', {'form': form})

@login_required
def user_logout(request):
    create_logout_statistic(request.user, 'username/password', True)
    logout(request)
    return redirect('home')

def google_login(request):
    # Redirect to Google for authentication
    adapter = GoogleOAuth2Adapter()
    provider = adapter.get_provider()
    login_url = provider.get_login_url(request, OAuth2Client(request))
    create_login_statistic(request.user, 'google', True)
    return redirect(login_url)

def totp_login(request):
    # Generate or get TOTP device for the user
    if request.user.is_authenticated:
        totp_device, created = TOTPDevice.objects.get_or_create(user=request.user)

    # Pass the TOTP secret key to the template
    context = {
        'secret_key': totp_device.secret,
    }

    return render(request, 'authapp/totp_login.html', context)

@login_required
def register_totp(request):
    user = request.user

    # Check if the user already has a TOTP device
    if TOTPDevice.objects.filter(user=user).exists():
        # Redirect to a page indicating that the user already has a TOTP device
        return redirect('totp_already_registered')

    # Create a new TOTP device for the user
    totp_device = TOTPDevice.objects.create(user=user, confirmed=False)

    # Pass the provisioning URL to the template
    provisioning_url = totp_device.config_url()
    context = {'provisioning_url': provisioning_url}

    return render(request, 'authapp/register_totp.html', context)

@login_required
def confirm_totp_device(request):
    user = request.user
    totp_device = TOTPDevice.objects.get(user=user, confirmed=False)

    # Use the VerifyTOTPView provided by django-otp
    # verify_view = VerifyTOTPView.as_view()
    return verify_view(request, totp_device.id)

# Utility functions for creating login and logout statistics
def create_login_statistic(user, login_method, login_successful):
    # Check if the user is not None before creating the LoginStats object
    if user is not None:
        LoginStats.objects.create(
            user=user,
            login_method=login_method,
            login_successful=login_successful
        )
    else:
        # Handle the case where user is None (failed login attempt)
        LoginStats.objects.create(
            login_method=login_method,
            login_successful=login_successful
        )

def create_username_password_statistic(user, login_successful):
    LoginStats.objects.create(
        user=user,
        login_method='username/password',
        login_successful=login_successful
    )

def create_logout_statistic(user, logout_method, logout_successful):
    LogoutStats.objects.create(
        user=user,
        logout_method=logout_method,
        logout_successful=logout_successful
    )

@login_required
def dashboard(request):
    # Fetch Google login statistics
    google_account = SocialAccount.objects.filter(user=request.user, provider='google').first()

    # Fetch username/password login statistics
    username_password_stats = LoginStats.objects.filter(
        user=request.user,
        login_method='username/password'
    ).order_by('-login_time')[:10]

    # Fetch 2FA (TOTP) login statistics
    totp_devices = TOTPDevice.objects.filter(user=request.user)

    return render(request, 'authapp/dashboard.html', {
        'google_account': google_account,
        'username_password_stats': username_password_stats,
        'totp_devices': totp_devices,
    })

class UserRegistrationView(View):
    template_name = 'authapp/register_user.html'

    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Additional processing for the user profile can be added here if needed
            user.save()

            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration

        return render(request, self.template_name, {'form': form})

class UserLoginView(View):
    template_name = 'authapp/login.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                create_login_statistic(request.user, 'username/password', True)
                return redirect('dashboard')
            else:
                create_login_statistic(None, 'username/password', False)

        return render(request, self.template_name, {'form': form})