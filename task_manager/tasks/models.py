from django.contrib.auth import get_user_model
from django.db import models

from task_manager.statuses.models import Status

# from task_manager.users.models import CustomUser

# Create your models here.
User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=80, unique=True, blank=False)
    description = models.TextField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)  # AUTOSET LOGGED USER! do here or at View?
    executor = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    # labels = FOREIGN KEY ADD LATER
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



