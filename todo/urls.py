from django.urls import path
from todo.views import TodoListAPIView


urlpatterns = [
    path("", TodoListAPIView.as_view(), name='todo'),
]
