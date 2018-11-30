from swapp.models import TodoList
from swapp.models import Memo
from swapp.models import Time
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoList
		fields = ('lid', 'date', 'title', 'context')

class MemoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Memo
    fields = ('mid', 'context')

class TimeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Time
    fields = ('time_zone')
