from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


class TaskCreationForm(ModelForm):

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        empty_label=_('(not set)'),
        widget=forms.Select(),
    )
    
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label=_('(not set)'),
        widget=forms.Select(),
    )

    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.SelectMultiple(),
    )

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]


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