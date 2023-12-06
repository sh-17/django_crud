from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

# use of this is that before we redirect any of page like ( register, signout...) it can just show some messages
from django.contrib import messages

""" 
    RENDER : The render shortcut will take a template name as an argument, and then render this 
    template with the given parameters and then return an HttpResponse with the rendered body

    HTTP-RESPONSE : HttpResponse returns only what the name we have indicates, dealing with HTTP responses
"""


#  Home Page

def home(request):
    return render(request, 'webapp/index.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("my-login")

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)


# - Login a user

def my_login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/my-login.html', context=context)


# Dashboard

@login_required(login_url='my-login')  # using decorators it says that login required  and it will pass to login url
def dashboard(request):
    # passing all the records from our database
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


# Create a Record

@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your Record Created!")

            return redirect("dashboard")
    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


# Update Record

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(
        instance=record)  # instance means i want to get particular user record, preload the form based on the instance

    if request.method == "POST":

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request, "Your Record is Updated!")

            return redirect("dashboard")
    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)


# Read/ View a single data/Record

@login_required(login_url='my-login')
def single_record(request, pk):
    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'webapp/view-record.html', context=context)


# Delete a Record

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    messages.success(request, "Your Record was Deleted!")

    record.delete()

    return redirect("dashboard")


# User Logout

def user_logout(request):
    auth.logout(request)

    messages.success(request, "Logout successful!")

    return redirect("my-login")
