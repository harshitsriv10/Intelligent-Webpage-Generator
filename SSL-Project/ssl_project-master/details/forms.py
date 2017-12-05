from details.models import *
from django.forms import ModelForm
from django import forms

class AboutForm(ModelForm):
    class Meta:
        model = ProfileDetails
        fields = ("name","designation","department","institute",
        "office","email","phone", "date_of_birth", "research_interest", "profile_pic", "profile_page")

class TeachingForm(ModelForm):
    class Meta:
        model = TeachingDetails
        fields = ("year","semester","course_name","course_description")

class ProjectForm(ModelForm):
    class Meta:
        model = ProjectDetails
        fields = ("project_title", "project_description","pi","co_pi","funding_agency", "start_year", "end_year")

class RecognitionForm(ModelForm):
    class Meta:
        model = RecognitionDetails
        fields = ("description",)

class PublicationForm(ModelForm):
    class Meta:
        model = PublicationDetails
        fields = ("Authors", "title","journal","journal_volume","page_no", "publish_date")

class StudentsForm(ModelForm):
    class Meta:
        model = StudentsDetails
        fields = ("student_status", "degree","student_name","thesis_title","supervisor")

class EducationForm(ModelForm):
    class Meta:
        model = EducationDetails
        fields = ("degree", "university" ,"year")

class WorkForm(ModelForm):
    class Meta:
        model = WorkDetails
        fields = ("experience", "description")

class CourseForm(ModelForm):
    class Meta:
        model = CourseDetails
        fields = ("messages", "files")

class MailForm(ModelForm):
    class Meta:
        model = Mail
        fields = ("username", "mail_file")
