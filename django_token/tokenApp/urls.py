from django.urls import path
from tokenApp.views import SignUp, SignIn

urlpatterns = [
    path('SignUp', SignUp.as_view()),
    path('SignIn', SignIn.as_view()),
]