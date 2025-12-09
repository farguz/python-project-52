from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from task_manager.statuses.models import Status

from .forms import TaskCreationForm
from .models import Task

User = get_user_model()


# Create your views here.
class IndexTaskView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        template_name = 'tasks/index.html' 
        tasks = Task.objects.all()
        return render(
            request,
            template_name,
            context={
                'tasks': tasks,
            },
        )
    

class CreateTaskView(CreateView):
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
    
