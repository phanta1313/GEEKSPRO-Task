from django.db import models
import uuid
class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    title = models.TextField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
