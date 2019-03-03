
from django.urls import path, include
from . import views

app_name= "LoginSignup"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='Login'),
    path('signup/', views.SignupView.as_view(), name='Signup'),
    path('logout/', views.LogoutView.as_view(), name='Logout'),
]