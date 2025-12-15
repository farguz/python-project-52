from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class IndexUserView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'


class RegistrationView(CreateView):

    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно создан')
        return super().get_success_url()


class UpdateUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')
    context_object_name = 'user'

    def test_func(self):    
        user = self.get_object()
        return self.request.user == user or self.request.user.is_superuser
    
    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно обновлен')
        return super().get_success_url()


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')
    context_object_name = 'user'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user or self.request.user.is_superuser

    def get_success_url(self):
        messages.success(self.request, 'Пользователь успешно удален')
        return super().get_success_url()
    