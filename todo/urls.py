from django.urls import path
from todo.views import TodoListAPIView, TodoDetailAPIView


urlpatterns = [
    path("", TodoListAPIView.as_view(), name='todo'),
    path("<int:id>", TodoDetailAPIView.as_view(), name='todo-detail'),
]
