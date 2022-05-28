from django.urls import include, path
from rest_framework import routers

from intern_manager.views import UserProfileViewSet, TaskViewSet, AttendenceViewSet

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet)
router.register(r'task', TaskViewSet)
router.register(r'attendence', AttendenceViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
