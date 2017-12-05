from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from details.models import *
from details.forms import *
from django.core.exceptions import ObjectDoesNotExist
import requests
from bs4 import BeautifulSoup

@login_required
def About_Me(request):
    user_name = request.user.username
    try:
        users = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')
    context={
        'users':users,
        'profile':users,
    }
    return render(request, 'about_me.html', context)

@login_required
def About_Me_Edit(request):
    user_name = request.user.username
    try:
        instance = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/test/about_me')
    else:
        form = AboutForm(instance=instance)
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request, 'about_me_edit.html', {
        'form': form, 'profile':profile,
    })

@login_required
def About_Me_Edit2(request, pk):
    user_name = request.user.username
    try:
        instance = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')

    notif = NotificationDetails.objects.get(pk=pk)
    instance.designation = notif.arg1

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            notif.delete()
            return redirect('/test/about_me')
    else:
        form = AboutForm(instance=instance)
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request, 'about_me_edit.html', {
        'form': form, 'profile':profile,
    })

@login_required
def About_Me_Create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            temp = form.save(commit=False)
            temp.username = user
            temp.save()
            user = User.objects.get(username=request.user.username)
            return redirect('/test/about_me')
    else:
        form = AboutForm()
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request, 'about_me_edit.html', {
        'form': form, 'profile':profile,
    })

@login_required
def Education(request):
    user_name = request.user.username
    try:
        users = EducationDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/education/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'education.html', context)

@login_required
def Education_Edit(request, pk):
    instance = EducationDetails.objects.get(pk=pk)
    form = EducationForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/education')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'education_edit.html',{'form':form, 'profile':profile})

@login_required
def Education_Add(request):
    form = EducationForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/education')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'education_add.html',{'form':form, 'profile':profile})

@login_required
def Education_Link(request):
    user = User.objects.get(username=request.user.username)
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    if(profile.profile_page != ""):
        page = requests.get(profile.profile_page)
        soup = BeautifulSoup(page.content, 'html.parser')
        for item in soup.find_all('div', {'class':'fh5co-content-inner text-center'}):
    	    i = item('div', {'class':'fh5co-icon'})[0]
    	    for j in i('p'):
                 form = EducationForm(None)
                 temp = form.save(commit=False)
                 temp.username = user
                 x = j.text
                 x = x.split()
                 temp.degree = ""+x[0]+ " "+x[1]
                 temp.university = ""
                 for z in range(2,len(x)-1):
                     temp.university += "" + x[z] + " "
                 temp.year = x[len(x)-1]
                 temp.save()
        for item in soup.find_all('div', {'class':'fh5co-content-inner text-center'}):
    	    i = item('div', {'class':'fh5co-icon'})[1]
    	    for j in i('p'):
                 form = WorkForm(None)
                 temp = form.save(commit=False)
                 temp.username = user
                 x = j.text
                 x = x.split()
                 if j.find('strong'):
                     temp.experience = j.find('strong').text

                 for z in range(0,len(x)):
                     temp.description += "" + x[z] + " "
                 temp.save()

        x = soup.find_all('i', {'class':'icon-calendar-check-o'})
        if len(x) > 0:
            x = x[0]
        x = x.parent.parent
        for item in x('li'):
            string = item.text
            list = string.split('&diam;')
            list[0] = list[0].strip()
            form = TeachingForm(None)
            temp = form.save(commit=False)
            temp.username = user
            temp.year = list[0]
            temp.semester = list[1].strip()
            list2 = list[2].split(':')
            temp.course_name = list2[0].strip()
            temp.course_description = list2[1].strip()
            temp.save()

        x = soup.find_all('i', {'class':'icon-shield'})
        if len(x) > 0:
            x = x[0]

        x = x.parent.parent
        for item in x('li'):
            form = RecognitionForm(None)
            temp = form.save(commit=False)
            temp.username = user
            temp.description = item.text
            temp.save()
        return redirect('/test/education')
    else:
        return redirect('/test')

@login_required
def Education_Delete(request, pk):
    instance = EducationDetails.objects.get(pk=pk).delete()
    return redirect('/test/education')

@login_required
def Work(request):
    user_name = request.user.username
    try:
        users = WorkDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/work/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'work.html', context)

@login_required
def Work_Edit(request, pk):
    instance = WorkDetails.objects.get(pk=pk)
    form = WorkForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/work')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'work_edit.html',{'form':form, 'profile':profile})

@login_required
def Work_Add(request):
    form = WorkForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/work')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'work_add.html',{'form':form, 'profile':profile})

@login_required
def Work_Delete(request, pk):
    instance = WorkDetails.objects.get(pk=pk).delete()
    return redirect('/test/work')

@login_required
def Teaching(request):
    user_name = request.user.username
    try:
        users = TeachingDetails.objects.order_by('year').filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/teaching/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'teaching.html', context)

@login_required
def Teaching_Edit(request, pk):
    instance = TeachingDetails.objects.get(pk=pk)
    form = TeachingForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/teaching')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'teaching_edit.html',{'form':form, 'profile':profile})

@login_required
def Teaching_Add(request):
    form = TeachingForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/teaching')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'teaching_add.html',{'form':form, 'profile':profile})

@login_required
def Teaching_Add2(request):
    form = TeachingForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/teaching')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'teaching_add.html',{'form':form, 'profile':profile})

@login_required
def Teaching_Delete(request, pk):
    instance = TeachingDetails.objects.get(pk=pk).delete()
    return redirect('/test/teaching')

@login_required
def Project(request):
    user_name = request.user.username
    try:
        users = ProjectDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/project/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'project.html', context)

@login_required
def Project_Edit(request, pk):
    instance = ProjectDetails.objects.get(pk=pk)
    form = ProjectForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/project')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'project_edit.html',{'form':form, 'profile':profile})

@login_required
def Project_Add(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/project')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'project_add.html',{'form':form, 'profile':profile})

@login_required
def Project_Delete(request, pk):
    instance = ProjectDetails.objects.get(pk=pk).delete()
    return redirect('/test/project')

@login_required
def Recognition(request):
    user_name = request.user.username
    try:
        users = RecognitionDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/recognition/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'recognition.html', context)

@login_required
def Recognition_Edit(request, pk):
    instance = RecognitionDetails.objects.get(pk=pk)
    form = RecognitionForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/recognition')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'recognition_edit.html',{'form':form, 'profile':profile})

@login_required
def Recognition_Add(request):
    form = RecognitionForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/recognition')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'recognition_add.html',{'form':form, 'profile':profile})

@login_required
def Recognition_Delete(request, pk):
    instance = RecognitionDetails.objects.get(pk=pk).delete()
    return redirect('/test/recognition')

@login_required
def Publication(request):
    user_name = request.user.username
    try:
        users = PublicationDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/publication/create')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'users':users,
        'profile':profile,
    }
    return render(request, 'publication.html', context)

@login_required
def Publication_Edit(request, pk):
    instance = PublicationDetails.objects.get(pk=pk)
    form = PublicationForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/publication')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'publication_edit.html',{'form':form, 'profile':profile})

@login_required
def Publication_Add(request):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/publication')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'publication_add.html',{'form':form , 'profile':profile})

@login_required
def Publication_Delete(request, pk):
    instance = PublicationDetails.objects.get(pk=pk).delete()
    return redirect('/test/publication')

@login_required
def Publication_Add2(request, pk):
    user_name = request.user.username
    try:
        instance = ProfileDetails.objects.get(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/about_me/create')

    notif = NotificationDetails.objects.get(pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            notif.delete()
            return redirect('/test/about_me')
    else:
        form = PublicationForm(initial={'Authors': instance.name, 'title': notif.arg1, 'journal': notif.arg2})
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request, 'publication_add.html', {
        'form': form, 'profile':profile,
    })

@login_required
def Students(request):
    user_name = request.user.username
    try:
        users = StudentsDetails.objects.filter(username__username=user_name)
    except ObjectDoesNotExist:
        return redirect('/test/students/create')
    btech = users.filter(degree='B-Tech')
    mtech = users.filter(degree='M-Tech')
    phd = users.filter(degree='PhD')
    btech1 = btech.filter(student_status='Continuing')
    mtech1 = mtech.filter(student_status='Continuing')
    phd1 = phd.filter(student_status='Continuing')
    btech2 = btech.filter(student_status='Completed')
    mtech2 = mtech.filter(student_status='Completed')
    phd2 = phd.filter(student_status='Completed')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    context={
        'btech1': btech1,
        'mtech1': mtech1,
        'phd1': phd1,
        'btech2': btech2,
        'mtech2': mtech2,
        'phd2': phd2,
        'profile':profile,
    }
    return render(request, 'students.html', context)

@login_required
def Students_Edit(request, pk):
    instance = StudentsDetails.objects.get(pk=pk)
    form = StudentsForm(request.POST or None, instance=instance)
    if form.is_valid():
          form.save()
          return redirect('/test/students')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'students_edit.html',{'form':form, 'profile':profile})

@login_required
def Students_Add(request):
    form = StudentsForm(request.POST or None)
    if form.is_valid():
        user = User.objects.get(username=request.user.username)
        temp = form.save(commit=False)
        temp.username = user
        temp.save()
        return redirect('/test/students')
    try:
        profile = ProfileDetails.objects.get(username__username=request.user.username)
    except ProfileDetails.DoesNotExist:
        profile=None
    return render(request,'students_add.html',{'form':form, 'profile':profile})

@login_required
def Students_Delete(request, pk):
    instance = StudentsDetails.objects.get(pk=pk).delete()
    return redirect('/test/students')

def Course(request, pk):
    user_name = request.user.username
    try:
        courses = TeachingDetails.objects.get(pk=pk)
        users = CourseDetails.objects.filter(course=courses)
    except ObjectDoesNotExist:
        return redirect('/courses/create')
    print(users)
    context={
        'users':users,
        'pk':pk,
    }
    return render(request, 'course.html', context)

@login_required
def Course_Add(request, pk):
    instance = TeachingDetails.objects.get(pk=pk)
    form = CourseForm(request.POST or None)
    if form.is_valid():
          form.save(commit=False)
          form.course = instance
          form.save()
          return redirect('/test/teaching/')
    return render(request,'course_edit.html',{'form':form, 'pk':pk})

@login_required
def Course_Edit(request, pk):
    instance = CourseDetails.objects.get(pk=pk)
    form = CourseForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/test/teaching')
    return render(request,'course_edit.html',{'form':form, 'pk':pk})

@login_required
def Course_Delete(request, pk):
    instance = CourseDetails.objects.get(pk=pk).delete()
    return redirect('/test/teaching')

@login_required
def Notif_Delete(request, pk):
    instance = NotificationDetails.objects.get(pk=pk).delete()
    return redirect('/test')
