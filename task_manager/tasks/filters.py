import django_filters
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

from .models import Task


class TaskFilter(django_filters.FilterSet):

    executor = django_filters.ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        empty_label=_('Any executor'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        empty_label=_('Any status'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        empty_label=_('Any label'),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    tasks_by_me = django_filters.BooleanFilter(
        method='filter_tasks_by_me',
        widget=forms.CheckboxInput()
    )

    tasks_for_me = django_filters.BooleanFilter(
        method='filter_tasks_for_me',
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
