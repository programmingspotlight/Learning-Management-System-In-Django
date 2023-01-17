from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create your forms here.
class SignupForm(UserCreationForm):
    email = forms.CharField(widget= forms.EmailInput())
    password1 = forms.CharField(widget= forms.PasswordInput())
    password2 = forms.CharField(widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput())
    password = forms.CharField(widget= forms.PasswordInput())


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'phone_number', 'bio', 'student_college']
