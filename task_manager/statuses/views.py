from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import StatusesCreationForm, StatusesUpdateForm
from .models import Status


# Create your views here.
class IndexStatusView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'
   

class CreateStatusView(LoginRequiredMixin, CreateView):

    model = Status
    form_class = StatusesCreationForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('status_list')

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно создан')
        return super().get_success_url()
      

class UpdateStatusView(LoginRequiredMixin, UpdateView):

    model = Status
    form_class = StatusesUpdateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('status_list')
    context_object_name = 'status'
   
    def get_success_url(self):
        messages.success(self.request, 'Статус успешно обновлен')
        return super().get_success_url()
    
    
class DeleteStatusView(LoginRequiredMixin, DeleteView):

    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('status_list')
    context_object_name = 'status'

    def get_success_url(self):
        messages.success(self.request, 'Статус успешно удален')
        return super().get_success_url()
    
