from django.db import models
from accounts.models import CustomUser
# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, default=2)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']