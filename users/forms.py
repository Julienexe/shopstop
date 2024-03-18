from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('image','contact','name')

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)