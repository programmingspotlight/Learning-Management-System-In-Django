from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Create your forms here
class SignupForm(UserCreationForm):
    email = forms.CharField(widget= forms.EmailInput())
    password1 = forms.CharField(widget= forms.PasswordInput())
    password2 = forms.CharField(widget= forms.PasswordInput())
    is_instructor = forms.BooleanField(widget= forms.CheckboxInput(), required=False)
    is_student = forms.BooleanField(widget= forms.CheckboxInput(), required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'is_instructor', 'is_student']


class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput())
    password = forms.CharField(widget= forms.PasswordInput())


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar', 'phone_number', 'bio']



