from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = AbstractUser
        fields = ("username", "email", "first_name", "last_name")
