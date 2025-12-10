from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.statuses.models import Status

from .forms import TaskCreationForm, TaskUpdateForm
from .models import Task

User = get_user_model()


# Create your views here.
class IndexTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    

class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['users'] = User.objects.all()
        context['statuses'] = Status.objects.all()
        return context
    
    def form_valid(self, form):
        task = form.save(commit=False)
        task.creator = self.request.user
        task.save()
        return super().form_valid(form)
    

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        context['users'] = User.objects.all()
        context['statuses'] = Status.objects.all()
        return context
    

class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('task_list')
    
    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator or self.request.user.is_superuser
    

class DetailTaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'