from django.contrib import admin
from django.urls import path,include
from .views import student_details

urlpatterns = [
    path('', student_details, name = 'student'),
]
