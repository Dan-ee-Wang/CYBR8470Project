from django.db import models
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import AbstractUser

#class CustomUser(AbstractUser):
    # Create a TOTPDevice relationship
#CustomUser.add_to_class('totp_device', TOTPDevice)

class UserProfile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)  # Add email field
    first_name = models.CharField(max_length=30, blank=True, null=True)  # Add first name field
    last_name = models.CharField(max_length=30, blank=True, null=True)  # Add last name field
    # Add any additional fields you want for your user profile
    USERNAME_FIELD = 'user'

    def __str__(self):
        return self.user.username

class LoginStats(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    login_method = models.CharField(max_length=255)
    login_successful = models.BooleanField(default=False)
    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_method} - {'Successful' if self.login_successful else 'Failed'}"
        #return f'{self.user} - {self.login_method} - {self.login_successful}'


class LogoutStats(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    logout_method = models.CharField(max_length=255)
    logout_successful = models.BooleanField(default=False)
    logout_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.login_method} - {'Successful' if self.login_successful else 'Failed'}"

class TOTPDeviceStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(TOTPDevice, on_delete=models.CASCADE)
    confirmation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - TOTP Device - {'Confirmed' if self.device.confirmed else 'Not Confirmed'}"
