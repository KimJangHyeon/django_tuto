from django.urls import path
from tokenApp.views import Auth


urlpatterns = [
    path('', Auth.as_view()),
]