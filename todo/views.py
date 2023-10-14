from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from authentication.jwt import JWTAuthentication
from todo.models import Todo
from django_filters.rest_framework import DjangoFilterBackend


class TodoListAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['id', 'title', 'is_complete']
    search_fields = ['title', 'description']
    ordering_fields = ['id','created_at','title', 'description']

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
