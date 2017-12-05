from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'details'

urlpatterns = [
    url(r"^about_me/$", views.About_Me,name='about_me'),
    url(r"^about_me/edit$", views.About_Me_Edit,name='about_me_edit'),
    url(r"^about_me/create$", views.About_Me_Create, name='about_me_create'),
    url(r'^about_me/(?P<pk>\d+)/edit$', views.About_Me_Edit2, name='about_me_edit2'),

    url(r"^education/$", views.Education,name='education'),
    url(r'^education/(?P<pk>\d+)/edit$', views.Education_Edit, name='education_edit'),
    url(r"^education/add$", views.Education_Add, name='education_add'),
    url(r'^education/(?P<pk>\d+)/delete$', views.Education_Delete, name='education_delete'),
    url(r"^link$", views.Education_Link, name='link'),

    url(r"^work/$", views.Work,name='work'),
    url(r'^work/(?P<pk>\d+)/edit$', views.Work_Edit, name='work_edit'),
    url(r"^work/add$", views.Work_Add, name='work_add'),
    url(r'^work/(?P<pk>\d+)/delete$', views.Work_Delete, name='work_delete'),

    url(r"^teaching/$", views.Teaching,name='teaching'),
    url(r'^teaching/(?P<pk>\d+)/edit$', views.Teaching_Edit, name='teaching_edit'),
    url(r"^teaching/add$", views.Teaching_Add, name='teaching_add'),
    url(r'^teaching/(?P<pk>\d+)/delete$', views.Teaching_Delete, name='teaching_delete'),

    url(r"^project/$", views.Project,name='project'),
    url(r'^project/(?P<pk>\d+)/edit$', views.Project_Edit, name='project_edit'),
    url(r"^project/edit$", views.Project_Edit,name='project_edit'),
    url(r"^project/add$", views.Project_Add, name='project_add'),
    url(r'^project/(?P<pk>\d+)/delete$', views.Project_Delete, name='project_delete'),

    url(r"^recognition/$", views.Recognition,name='recognition'),
    url(r'^recognition/(?P<pk>\d+)/edit$', views.Recognition_Edit, name='recognition_edit'),
    url(r"^recognition/add$", views.Recognition_Add, name='recognition_add'),
    url(r'^recognition/(?P<pk>\d+)/delete$', views.Recognition_Delete, name='recognition_delete'),

    url(r"^publication/$", views.Publication,name='publication'),
    url(r'^publication/(?P<pk>\d+)/edit$', views.Publication_Edit, name='publication_edit'),
    url(r"^publication/add$", views.Publication_Add, name='publication_add'),
    url(r'^publication/(?P<pk>\d+)/delete$', views.Publication_Delete, name='publication_delete'),
    url(r"^publication/add/(?P<pk>\d+)$", views.Publication_Add2, name='publication_add2'),

    url(r"^students/$", views.Students,name='students'),
    url(r'^students/(?P<pk>\d+)/edit$', views.Students_Edit, name='students_edit'),
    url(r"^students/add$", views.Students_Add, name='students_add'),
    url(r'^students/(?P<pk>\d+)/delete$', views.Students_Delete, name='students_delete'),

    url(r'^course/(?P<pk>\d+)/$', views.Course, name='course_'),
    url(r'^course/(?P<pk>\d+)/add$', views.Course_Add, name='course_'),
    url(r'^course/(?P<pk>\d+)/edit$', views.Course_Edit, name='course_'),
    url(r'^course/(?P<pk>\d+)/delete$', views.Course_Delete, name='course_'),

    url(r'^delete/(?P<pk>\d+)$', views.Notif_Delete, name='delete'),
]
