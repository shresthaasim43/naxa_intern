from rest_framework import serializers

from intern_manager.models import UserProfile, Task,Attendence

class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
       model = UserProfile
       fields = ('id', 'name', 'role', 'username','password','is_logged_id')

class TaskSerializer(serializers.ModelSerializer):
   class Meta:
       model = Task
       fields = ('id', 'name', 'is_completed', 'assignee_id', 'supervisor_id')

class AttendenceSerializer(serializers.ModelSerializer):
   class Meta:
       model = Attendence
       fields = ('id', 'attendence_time', 'user_id')