from django.urls import path
from blog.views import Event
urlpatterns = [
	path('', Event.as_view()),
]
