from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from authentication.jwt import JWTAuthentication
from todo.models import Todo
from rest_framework.response import Response
from rest_framework import status


class TodoListAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        print(self.request.user)
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    lookup_field = "id"

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
