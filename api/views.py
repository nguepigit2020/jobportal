from .models import JobSeeker, AdminUser, Job
from .serializers import JobSeekerSerializer, AdminUserSerializer, JobSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class JobSeekerViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows job seekers to be viewed or edited.
    """
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

    def update(self, request, *args, **kwargs):
        """
            Updates a job seeker instance.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """
            Deletes a job seeker instance.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminUserViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows admin users to be viewed or edited.
    """
    queryset = AdminUser.objects.all()
    serializer_class = AdminUserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows jobs to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

