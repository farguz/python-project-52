from django.forms import ModelForm

from .models import Status


class StatusesForm(ModelForm):
    class Meta:
        model = Status
        fields = [
            'name',
        ]
