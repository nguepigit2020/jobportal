from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobSeekerViewSet, AdminUserViewSet, JobViewSet

# Create a default router object.
router = DefaultRouter()

# Register the JobSeekerViewSet for the 'jobseekers','adminusers' and 'jobs' URLS.
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'adminusers', AdminUserViewSet)
router.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
