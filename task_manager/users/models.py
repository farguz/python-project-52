from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name=_('first name'), max_length=150, blank=False)
    last_name = models.CharField(verbose_name=_('last name'), max_length=150, blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
