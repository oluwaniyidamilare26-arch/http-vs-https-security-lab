from django.db import models

# Create your models here.

class LoginAttempt(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {'Success' if self.success else 'Failed'}"
