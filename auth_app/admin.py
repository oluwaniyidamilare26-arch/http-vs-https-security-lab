from django.contrib import admin

# Register your models here.
from .models import LoginAttempt

admin.site.register(LoginAttempt)
