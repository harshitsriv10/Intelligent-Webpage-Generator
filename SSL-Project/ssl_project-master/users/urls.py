from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    url(r"login/$", views.Login_User,name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(template_name="users/signup.html"), name="signup"),
]
