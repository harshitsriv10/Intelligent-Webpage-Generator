from django.db import models
from django.contrib.auth.models import User
from sslProject import settings

class ProfileDetails(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    department = models.CharField(max_length=128)
    institute = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    research_interest = models.TextField()
    profile_pic = models.ImageField(upload_to='photos/', blank=True, null=True)
    profile_page = models.CharField(blank=True, max_length=1000)
    def __str__(self):
        return self.name


class EducationDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

class WorkDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

import datetime
YEAR_CHOICES = []
SEM_CHOICES = [('Odd Semester', 'Odd Semester'), ('Even Semester', 'Even Semester')]
for r in range(1993, (datetime.datetime.now().year+1)):
    s = str(r)+"-"+str(r+1)
    YEAR_CHOICES.append((s,s))

class TeachingDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    year=models.CharField(max_length=255, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=255, choices=SEM_CHOICES)
    course_name = models.CharField(max_length=255)
    course_description = models.TextField(max_length=255)

class ProjectDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=255)
    project_description=models.TextField(max_length=255)
    pi = models.CharField(max_length=255, blank=True)
    co_pi = models.CharField(max_length=255, blank=True)
    funding_agency = models.CharField(max_length=255)
    start_year = models.CharField(max_length=255)
    end_year = models.CharField(max_length=255)

class RecognitionDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)

class PublicationDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    Authors = models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    journal = models.CharField(max_length=255)
    journal_volume = models.CharField(max_length=255)
    page_no = models.CharField(max_length=255)
    publish_date = models.CharField(max_length=255)

STATUS_CHOICES=[('Continuing', 'Continuing'),('Completed', 'Completed')]
STUDENT_DEGREE=[('B-Tech','B-Tech'),('M-Tech','M-Tech'),('PhD','PhD')]

class StudentsDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    student_status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    degree=models.CharField(max_length=255, choices=STUDENT_DEGREE)
    student_name = models.CharField(max_length=255)
    thesis_title = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)

class CourseDetails(models.Model):
    course = models.ForeignKey(TeachingDetails, on_delete=models.CASCADE)
    messages = models.TextField(max_length=255)
    files = models.FileField(blank=True)

class NotificationDetails(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(blank=True)
    message = models.CharField(max_length=255)
    arg1 = models.CharField(max_length=255, blank=True)
    arg2 = models.CharField(max_length=255, blank=True)

class Mail(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    mail_file = models.FileField(blank=True)
