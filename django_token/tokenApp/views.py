from django.shortcuts import render
from rest_framework.views import APIView
from tokenApp.models import Users

# Create your views here.
class SignUp(APIView):
    def post(self, request, format=None):
        data = request.data
        exist_uid = Users.objects.filter()


