from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import View

from blog.models import Event as mEvent

from blog.serializers import EventSerializer
# Create your views here.
class Event(APIView):

	def get(self, request):
		events = mEvent.objects.all()
		serializer = EventSerializer(events, many=True)
#if not serializer.is_valid():
#			return ErrorResponse.error_response(-300, serializer.errors)
#		else:
		return Response(serializer.data)
		
	def post(self, request):
		serializer = EventSerializer(data=request.data, many=True)
		if not serializer.is_valid():
			return ErrorResponse.error_response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
			

class ErrorResponse:
	@staticmethod
	def error_response(error_code, message):
		data = {"message": message, "ErrorCode": error_code}
		return Response(data)

