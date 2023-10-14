from rest_framework.serializers import ModelSerializer
from todo.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','description','is_complete']