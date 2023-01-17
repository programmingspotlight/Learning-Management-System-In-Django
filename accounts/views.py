from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm, UserForm, ProfileForm

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect("login")

    else:
        signup_form = SignupForm()

    context = {
        'signup_form': signup_form,
    }

    return render(
        request= request,
        template_name= "accounts/signup.html",
        context= context
    )


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username= username, password= password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged successfully.')
                return redirect("profile")
    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form,
    }

    return render(
        request= request,
        template_name= "accounts/login.html",
        context= context
    )


def user_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance= request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been created successfully.')
            return redirect("home")

    else:
        user_form = UserForm(instance= request.user)
        profile_form = ProfileForm(instance= request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(
        request= request,
        template_name= "accounts/profile.html",
        context= context
    )


def user_logout(request):
    logout(request)
    return redirect("home")