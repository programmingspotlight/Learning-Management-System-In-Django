from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm, UserForm, ProfileForm

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        # Submit The Form.
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            # If The Form Data is Valid, Save The Form and Display a Success Message and Then Redirect to The Login Page.
            signup_form.save()
            messages.success(request, 'Your account has been created successfully.')
            return redirect("login")

    else:
        # Display The Blank Form.
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
        # Submit The Form.        
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # If The Form Data is Valid, Get The Data From The Database.
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            # Check The User Credentials (username and password) and Return The Correct User Object From The DataBase
            user = authenticate(username= username, password= password)

            # If The User Credentials are Correct, Log in The User and Display a Success Message.
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged successfully.')
                return redirect("profile")
            
            # If The User Credentials aren't Correct, Back to The Login Page and Display an Error Message.
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect("login")
    else:
        # Display The Blank Form.
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
        # If The User Submit The Form, Display The Stored Data Previously and store the user image in request.FILES.
        user_form = UserForm(request.POST, instance= request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            # If The Forms are All Valid, Save Their Data and Display a Success Message Then Redirect to The Home Page.
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been created successfully.')
            return redirect("home")

    else:
        # Display The Form With The Stored Data.
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
    # When The User Clicks on The Logout URL, Logout and Redirect to The Home Page.
    logout(request)
    return redirect("home")