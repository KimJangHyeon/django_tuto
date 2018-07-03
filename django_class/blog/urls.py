from django.urls import path
from blog.views import MyView


urlpatterns = [
	path('', MyView.as_view()),
]

