from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from tokenApp.Serializers import UserSerializer
from tokenApp.models import MyUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password

class ErrorResponse:
    @staticmethod
    def error_response(error_code, message):
        data = {"message": message, "ErrorCode": error_code}
        return Response(data)

# Create your views here.
class SignUp(APIView):
    def post(self, request, format=None):
        data = request.data
        exist_uid = MyUser.objects.filter(name=data['name'])

        if exist_uid.count() != 0:
            return ErrorResponse.error_response(-200, 'same name exist')


        #password = make_password(password=data['pw'], salt=None, hasher='default')

        user = dict()
        user['name'] = data['name']
        user['pw'] = make_password(password=data['pw'], salt=None, hasher='default')
        user_serializer = UserSerializer(data=user)

        if user_serializer.is_valid():
            user_serializer.save()
            return_data = {'message': 'Success', 'ErrorCode': 0}
            return Response(return_data)
        return ErrorResponse().error_response(-1, 'Error at the end')

class SignIn(APIView):
    def post(self, request, format=None):
        # data = request.data
        # userId = MyUser.objects.filter(name=data['name'])
        # user = authenticate(name=data['name'], pw=make_password(password=data['pw'], salt=None, hasher='default'))
        # print(userId.get(name=data['name']).uid)
        # print(user)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)