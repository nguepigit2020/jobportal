from django.db import models

# Create your models here.


class JobSeeker(models.Model):
    """
        Model representing a job seeker.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)


class AdminUser(models.Model):
    """
        Model representing an admin user.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()


class Job(models.Model):
    """
        Model representing a job.
    """
    id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField()



