import django_filters
from django import forms
from django.contrib.auth import get_user_model

from task_manager.statuses.models import Status

from .models import Task


class TaskFilter(django_filters.FilterSet):
    User = get_user_model()
    users = User.objects.all()
    statuses = Status.objects.all()

    status = django_filters.ModelChoiceFilter(
        queryset=statuses.values_list('name', flat=True),
        empty_label='Все статусы',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.filter(is_active=True).values_list('first_name', 'last_name'),
        empty_label='Все исполнители',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    tasks_by_myself = django_filters.ModelChoiceFilter(
        queryset=users.filter(is_active=True),
        label='Только свои задачи',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    class Meta:
        model = Task
        fields = [
            'status',
            'executor',
            # 'labels',
            'creator',
        ]
