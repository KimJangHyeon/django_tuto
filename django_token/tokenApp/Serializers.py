from django.contrib.auth import authenticate
from rest_framework import exceptions
from tokenApp.models import MyUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def validate(self, data):
        name = data.get('name', '')
        pw = data.get('pw', '')

        if name and pw:
            user = authenticate(username=name, password=pw)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise exceptions.ValidationError('he')
                return data
            else:
                raise exceptions.ValidationError('no authenticate')

    class Meta:
        model = MyUser
        fields = ('uid', 'name', 'pw')
