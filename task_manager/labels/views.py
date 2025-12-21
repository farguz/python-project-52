from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import LabelsCreationForm, LabelsUpdateForm
from .models import Label


class IndexLabelView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    context_object_name = 'labels'


class CreateLabelView(LoginRequiredMixin, CreateView):

    model = Label
    form_class = LabelsCreationForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('label_list')

    def get_success_url(self):
        messages.success(self.request, 'Метка успешно создана')
        return super().get_success_url()
    

class UpdateLabelView(LoginRequiredMixin, UpdateView):

    model = Label
    form_class = LabelsUpdateForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('label_list')
    context_object_name = 'label'
   
    def get_success_url(self):
        messages.success(self.request, 'Метка успешно обновлена')
        return super().get_success_url()
    
    
class DeleteLabelView(LoginRequiredMixin, DeleteView):

    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('label_list')
    context_object_name = 'label'

    def get_success_url(self):
        messages.success(self.request, 'Метка успешно удалена')
        return super().get_success_url()

    def form_valid(self, form):
        self.label = self.object
        if self.label.task_set.exists():
            messages.error(
                self.request,
                'Невозможно удалить метку, потому что она используется в задачах'
                )
            return redirect('label_list')
            
        response = super().form_valid(form)
        return response