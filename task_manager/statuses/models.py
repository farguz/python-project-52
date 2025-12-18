from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=80, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'