from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import BasePermissionMixin

from .filters import TaskFilter
from .forms import TaskCreationForm, TaskUpdateForm
from .models import Task

User = get_user_model()


class IndexTaskView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    
    def get_queryset(self):
        return Task.objects.select_related(
            'creator', 
            'executor', 
            'status'
            ).prefetch_related(
            'labels'
            ).all()


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(self.request, _('Task created successfully'))
        response = super().form_valid(form)
        return response
    

class UpdateTaskView(BasePermissionMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('task_list')
    error_redirect_url = reverse_lazy('task_list')
    permission_denied_message = _('Forbidden. Not enough rights to edit this task')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator or self.request.user.is_superuser
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Task updated successfully'))
        return response
    

class DeleteTaskView(BasePermissionMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('task_list')
    error_redirect_url = reverse_lazy('task_list')
    permission_denied_message = _('Forbidden. Not enough rights to delete this task')
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator or self.request.user.is_superuser

    def get_success_url(self):
        messages.success(self.request, _('Task deleted successfully'))
        return super().get_success_url()
    

class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'