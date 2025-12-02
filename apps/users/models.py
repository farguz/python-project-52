from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=150)
    password = models.CharField(max_length=255, validators=[MinLengthValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)