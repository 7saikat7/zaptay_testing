from django.urls import path, include
from user_login import views

app_name = "user_login"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="user_login_page"),
    path('signup/', views.SignupView.as_view(), name="user_signup_page"),
]