from . import views
from django.urls import path

urlpatterns = [
  path('todoall', views.todo_all, name='todoall'),
  path('todocreate', views.todo_create, name='todocreate'),
  path('todoupdate', views.todo_update, name='todoupdate'),
  path('tododelete', views.todo_delete, name='tododelete'),
]
