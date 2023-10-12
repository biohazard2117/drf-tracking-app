from django.db import models

class Tracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
        abstract = True
        ordering = ('-created_at')