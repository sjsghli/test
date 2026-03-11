from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser

from accounts.models import User



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
