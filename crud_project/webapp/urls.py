from django.contrib import admin
from django.urls import path
from . import views  # import all the views

# from django import views home ---> for importing single view

urlpatterns = [
    path('', views.home, name=''),

    path('register/', views.register, name="register"),

    path('login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    # Crud

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name="update-record"),
    # <int:pk> means that the dynamic value on the link if we type 2 then it will update record

    path('record/<int:pk>', views.single_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

]



