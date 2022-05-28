from django.shortcuts import render
from django.conf.urls import url
from rest_framework import viewsets
from rest_framework_swagger.views import get_swagger_view


# Create your views here.
from intern_manager.serializers import UserProfileSerializer, TaskSerializer, AttendenceSerializer 
from intern_manager.models import UserProfile, Task, Attendence 

class UserProfileViewSet(viewsets.ModelViewSet):
   queryset = UserProfile.objects.all()
   serializer_class = UserProfileSerializer

class TaskViewSet(viewsets.ModelViewSet):
   queryset = Task.objects.all()
   serializer_class = TaskSerializer

class AttendenceViewSet(viewsets.ModelViewSet):
   queryset = Attendence.objects.all()
   serializer_class = AttendenceSerializer
