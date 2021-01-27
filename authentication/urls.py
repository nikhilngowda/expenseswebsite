from django.urls import path
from .views import RegistrationView, UsernameValidationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('validate-username', UsernameValidationView.as_view(), name="validate-username")
]