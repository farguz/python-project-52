from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)