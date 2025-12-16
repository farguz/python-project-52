from django.forms import ModelForm

from .models import Task


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]


# delete, the same???
class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]