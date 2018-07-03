from django.shortcuts import render
from django.http import HttpResponse

#for class view
from django.views.generic import View
# Create your views here.
class MyView(View):
	def get(self, request):
		return HttpResponse("class get")

