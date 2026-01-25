from django.forms import ModelForm

from .models import Label


class LabelsForm(ModelForm):
    class Meta:
        model = Label
        fields = [
            'name',
        ]
