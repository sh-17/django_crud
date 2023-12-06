"""

In django UserCreationForm is a built-in-form provide by 'django.contrib.auth.forms' module
that creates the process of new user account.. used when we are developing authentication system ..
which required to to handle user registration..designed to create new user instances in the database by handling the
necessary input fields such as username, password, and password confirmation.

- When we import UserCreationForm from django.contrib.auth.forms, we can use this form in our
  Django views or templates to render a form for user registration

"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# ---> Register / Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# ---> Login a User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# ---> Add Record of User

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# ---> Update Record of User

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
