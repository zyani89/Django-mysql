from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    # check to see if logging in
    if request.method == "POST":
        # Getting the values sent by our form
        username = request.POST['username']
        pwd = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Logged In! ")
            return redirect('website:home')
        else:
            messages.success(request, "Invalid Username or Password")
            return redirect('website:home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You habe been logged out ...')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
