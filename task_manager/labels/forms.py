from django.forms import ModelForm

from .models import Label


class LabelsCreationForm(ModelForm):
    class Meta:
        model = Label
        fields = [
            'name',
        ]


class LabelsUpdateForm(ModelForm):
    class Meta:
        model = Label
        fields = [
            'name',
        ]
