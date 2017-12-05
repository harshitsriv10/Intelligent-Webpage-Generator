from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from sslProject import settings
from . import forms
import urllib
import json
from details.models import NotificationDetails
from django.contrib.auth.models import User
from details.models import Mail
from django.core.exceptions import ObjectDoesNotExist

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"

def Login_User(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())

                if result['success']:
                    login(request, user)
                    users1 = User.objects.get(username=username)
                    try:
                        mail = Mail.objects.get(username=users1)
                    except ObjectDoesNotExist:
                        return(redirect('/test/about_me'))
                    print(mail.mail_file.url)
                    with open(mail.mail_file.path) as file:
                        email = ""
                        sender_name=[]
                        email_index = -1
                        type = -1
                        new_position = []
                        member_name= []
                        paper_name=""
                        volume = []
                        volume_number = 0
                        issue_number = 0
                        issue_name = []
                        page=[]
                        month = "month"
                        year = "year"
                        paper_name1 = ""
                        paper_name2 = ""
                        start_place = 0
                        end_place = 0
                        content = file.readlines()
                        for line in content:
                            words = line.split()
                            start_counter = 0
                            end_counter = 0
                            for word in words:
                                #print(word)
                                if "<" in word and ">" in word and ("@iitg" in word or "@gmail" in word or "@yahoo" in word):
                                    email = word
                                    email_index = words.index(email)
                                    for int in range(0,email_index):
                                        sender_name.append(words[int])
                                if "To" in word:
                                    print("word found as", word)
                                    found = word
                                    found_index = words.index(word)
                                    member_name.append(words[found_index + 2])
                                    member_name.append(words[found_index + 3])
                                if "promot" in word:#promoting, promoted for both of these
                                    #print("found promote")
                                    type = 1
                                if type == 1:
                                    #print(word)
                                    if "assistant" in word or "Assistant" in word or "Associate" in word or "associate" in word:
                                        new_position.append(word)
                                    if "professor" in word or "Professor" in word:
                                       new_position.append(word)
                                    if "HOD" in word or "hod" in word or "Head of Department" in word or "Head" in word or "head" in word or "Head" in word or "HoD" in word or "hOd" in word:
                                        new_position.append(word)
                                    if "Dean" in word or "dean" in word:
                                        new_position.append(word)
                                    if "Director" in word or "director" in word:
                                        new_position.append(word)
                                    if "To" in word:
                                        print("inside to search")
                                        index = words.index(word)
                                        print(words[index])
                                        member_name.append(words[index + 1])
                                        member_name.append(words[index + 2])
                                if "accept" in word:
                                    start_counter = words.index(word)
                                    print("start counter found as: ",words[start_counter])
                                    type = 2
                                    print("type found of :",type)
                                if type == 2 and (word == "by" or word == "in") and words.index(word) == start_counter + 1:
                                        start_counter = words.index(word)
                                        print("index found is :",words[start_counter])
                                if type == 2 and start_counter > 0 and "." in word:
                                    print("inside here")
                                    end_counter = words.index(word)
                                    for i in range(start_counter+1,end_counter+1):
                                        paper_name += words[i] + " "
                                if type == 2:
                                    if "volum" in word or "Volum" in word:
                                        volume_number = words[words.index(word)+1]
                                if type == 2 and word == "issue" or word == "Issue":
                                    word_temp1 = word
                                    issue_number = words.index(word_temp1)+1
                                    issue_name.append(words[issue_number])
                                if type == 2 and "page" in word or "Page" in word:
                                    index = words.index(word)+1
                                    page.append(words[index])
                                if type == 2 and "publish" in word:
                                    index = words.index(word)+2
                                    month = words[index]
                                    index = index + 1
                                    year = words[index]
                                if "paper" in word:
                                    place = words.index(word)
                                    if "on" in words[place + 1]:
                                        start_place = start_place + 2
                                if "has" in word:
                                    if start_place != 0:
                                        end_place = words.index(word)
                                    for int in range(start_place+1, end_place):
                                        paper_name2 = paper_name2 + " " + words[int]
                        print(paper_name2)
                        open(mail.mail_file.path, 'w').close()
                        if type == 1:
                            string = ""
                            for i in new_position:
                                string += i+" "
                            b = NotificationDetails(username=users1, type=1, message="Congrats! You have been promoted to "+string, arg1 = string)
                            b.save()

                        if type == 2:

                            b = NotificationDetails(username=users1, type=2, message="Your Paper on "+ paper_name2 +" has been accepted by "+ paper_name, arg1 = paper_name2, arg2 = paper_name)
                            b.save()
                    return redirect('/test/about_me')
                else:
                    return render(request, 'users/login.html', {'error_message': 'Invalid Captcha'})
            else:
                return render(request, 'users/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'users/login.html', {'error_message': 'Invalid Login'})
    return render(request, 'users/login.html')
