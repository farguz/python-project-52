import django_filters
from django import forms
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


class TaskFilter(django_filters.FilterSet):
    User = get_user_model()
    users = User.objects.all()
    statuses = Status.objects.all()
    labels_list = Label.objects.all()

    executor = django_filters.ModelChoiceFilter(
        queryset=users,
        empty_label='Все исполнители',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    status = django_filters.ModelChoiceFilter(
        queryset=statuses,
        empty_label='Все статусы',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    labels = django_filters.ModelChoiceFilter(
        queryset=labels_list,
        empty_label='Все метки',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    tasks_by_me = django_filters.BooleanFilter(
        method='filter_tasks_by_me',
        label='Я постановщик задачи',
        widget=forms.CheckboxInput()
    )

    tasks_for_me = django_filters.BooleanFilter(
        method='filter_tasks_for_me',
        label='Я исполнитель задачи',
        widget=forms.CheckboxInput()
    )
    
    def filter_tasks_by_me(self, queryset, name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset
    
    def filter_tasks_for_me(self, queryset, name, value):
        if value:
            return queryset.filter(executor=self.request.user)
        return queryset
    
    class Meta:
        model = Task
        fields = [
            'status',
            'executor',
            'labels',
            'creator',
        ]
