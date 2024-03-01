from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, LogoutView, ChangePasswordView, ForgotPasswordView, ForgotPasswordCompleteView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('activate/', ActivationView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot-password-complete/', ForgotPasswordCompleteView.as_view(), name='forgot_password_complete')
]
