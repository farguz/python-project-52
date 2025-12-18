from django.contrib.auth import get_user_model
from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

User = get_user_model()


class Task(models.Model):
    name = models.CharField(max_length=80, unique=True, blank=False)
    description = models.TextField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False)
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=False,
        related_name="task_creator")
    executor = models.ForeignKey(User,
        on_delete=models.PROTECT,
        blank=True,
        related_name="task_executor")
    labels = models.ManyToManyField(Label)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'



