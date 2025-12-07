from django.forms import ModelForm
from statuses.models import Status


class StatusesCreationForm(ModelForm):
    class Meta:
        model = Status
        fields = [
            'name',
        ]


class StatusesUpdateForm(ModelForm):
    class Meta:
        model = Status
        fields = [
            'name',
        ]
