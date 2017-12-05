"""sslProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r"^test/$", views.HomePage.as_view(), name="test"),
    url(r'^admin/', admin.site.urls),
    url(r"^users/", include("users.urls")),
    url(r"^users/", include("django.contrib.auth.urls")),
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"),
    url(r"^list/$", views.List ,name='list'),
    url(r"^test/", include("details.urls")),
    url(r"^profile/(?P<username>\w+)/$", views.ProfilePage, name="profile_page"),
    url(r"^profile/(?P<username>\w+)/teaching$", views.ProfileTeachingPage, name="profile_teaching"),
    url(r"^profile/(?P<username>\w+)/student$", views.ProfileStudentPage, name="profile_student"),
    url(r"^profile/(?P<username>\w+)/project$", views.ProfileProjectPage, name="profile_project"),
    url(r"^profile/(?P<username>\w+)/publication$", views.ProfilePublicationPage, name="profile_publication"),
    url(r"^profile/(?P<username>\w+)/recognition$", views.ProfileRecognitionPage, name="profile_recognition"),
    url(r"^mail/$", views.Mail, name="mail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
