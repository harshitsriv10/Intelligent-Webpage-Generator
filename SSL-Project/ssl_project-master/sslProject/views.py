from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from details.models import *
from details.forms import *
@login_required
def TestPage(request):
    user1 = User.objects.get(username=username)
    notifs = NotificationDetails.objects.filter(username=user1)
    context={'notifs': notifs,}
    return render(request, 'test.html', context)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                try:
                    profile = ProfileDetails.objects.get(username__username=request.user.username)
                except ProfileDetails.DoesNotExist:
                    profile=None
                user1 = User.objects.get(username=request.user.username)
                notifs = NotificationDetails.objects.filter(username=user1)
                context={
                    'notifs': notifs,
                    'user':request.user,
                    'profile':profile,
                }
                return render(request , "test.html" , context)
            # else:
            #     return HttpResponseRedirect('');
        return super().get(request, *args, **kwargs)

def List(request):
    users = ProfileDetails.objects.order_by('name').order_by('department').all()
    context={
        'users': users
    }
    return render(request,'list.html', context)

def ProfilePage(request, username):
    users = ProfileDetails.objects.get(username__username=username)
    education = EducationDetails.objects.filter(username__username = username)
    work = WorkDetails.objects.filter(username__username = username)
    print(education)
    return render(request, 'profile.html',{'users':users, 'username':username, 'work':work, 'education':education})

def ProfileTeachingPage(request, username):
    users = TeachingDetails.objects.order_by('year').filter(username__username=username)
    return render(request, 'profile_teaching.html',{'users':users, 'username':username})

def ProfilePublicationPage(request, username):
    users = PublicationDetails.objects.filter(username__username=username)
    return render(request, 'profile_publication.html',{'users':users, 'username':username})

def ProfileStudentPage(request, username):
    users = StudentsDetails.objects.filter(username__username=username)
    btech = users.filter(degree='B-Tech')
    mtech = users.filter(degree='M-Tech')
    phd = users.filter(degree='PhD')
    btech1 = btech.filter(student_status='Continuing')
    mtech1 = mtech.filter(student_status='Continuing')
    phd1 = phd.filter(student_status='Continuing')
    btech2 = btech.filter(student_status='Completed')
    mtech2 = mtech.filter(student_status='Completed')
    phd2 = phd.filter(student_status='Completed')
    context={
        'username':username,
        'btech1': btech1,
        'mtech1': mtech1,
        'phd1': phd1,
        'btech2': btech2,
        'mtech2': mtech2,
        'phd2': phd2,
    }
    return render(request, 'profile_student.html',context)

def ProfileRecognitionPage(request, username):
    users = RecognitionDetails.objects.filter(username__username=username)
    return render(request, 'profile_recognition.html',{'users':users, 'username':username})

def ProfileProjectPage(request, username):
    users = ProjectDetails.objects.filter(username__username=username)
    return render(request, 'profile_project.html',{'users':users, 'username':username})

def Mail(request):
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            temp.save()
    else:
        form = MailForm()
    return render(request, 'mails.html', {
        'form': form,
    })
