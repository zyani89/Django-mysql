from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    # call all the records of the database
    records = Record.objects.all()
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
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You habe been logged out ...')
    return redirect('website:home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate & login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully register')
            return redirect('website:home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # llok up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(
            request, 'You must be logged in to view this page....')
        return redirect('website:home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Record has been deleted successfully...')
        return redirect('website:home')
    else:
        messages.success(
            request, 'You must be logged in to delete this record....')
        return redirect("website:home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(
                    request, 'Record has been added successfully...')
                return redirect('website:home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, 'You should be Logged In ....')
        return redirect('website:home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Record has been updated successfully...')
            return redirect('website:home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You should be Logged In ....')
        return redirect('website:home')
