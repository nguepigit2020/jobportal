from rest_framework import serializers
from .models import JobSeeker, AdminUser, Job


# JobSeekerSerializer class definition
class JobSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeeker
        fields = '__all__'


# AdminUserSerializer class definition
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


# JobSerializer class definition
class JobSerializer(serializers.ModelSerializer):
    # Meta class definition for JobSerializer
    class Meta:
        # Specify the model for the serializer
        model = Job
        # Specify the fields to be included in the serialized data
        fields = '__all__'
