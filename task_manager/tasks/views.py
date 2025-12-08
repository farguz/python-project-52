from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from .models import Task


# Create your views here.
class IndexTaskView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        template_name = 'tasks/index.html'

        tasks = Task.objects.all()
        
        return render(
            request,
            template_name,
            context={
                'tasks': tasks,
            },
        )