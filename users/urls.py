from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, password_recovery, generate_new_password, VerifyEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', password_recovery, name='password_recovery'),
    path('profile/generate_new_password/', generate_new_password, name='generate_new_password'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify_email'),
]
