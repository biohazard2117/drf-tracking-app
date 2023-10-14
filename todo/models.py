from helpers.models import Tracking
from authentication.models import User
from django.db import models

class Todo(Tracking):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

