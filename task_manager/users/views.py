from django.contrib import messages
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from task_manager.mixins import BasePermissionMixin

from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class IndexUserView(ListView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'
    paginate_by = 10


class RegistrationView(CreateView):

    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request, _('User created successfully'))
        return super().get_success_url()


class UpdateUserView(BasePermissionMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('user_list')
    context_object_name = 'user'
    error_redirect_url = reverse_lazy('user_list')
    permission_denied_message = _('Forbidden. Not enough rights to edit this user')

    def test_func(self):    
        user = self.get_object()
        return self.request.user == user or self.request.user.is_superuser
    
    def get_success_url(self):
        messages.success(self.request, _('User updated successfully'))
        return super().get_success_url()
    
    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
        user.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)


class DeleteUserView(BasePermissionMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')
    context_object_name = 'user'
    error_redirect_url = reverse_lazy('user_list')
    permission_denied_message = _('Forbidden. Not enough rights to delete this user')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user or self.request.user.is_superuser

    def get_success_url(self):
        messages.success(self.request, _('User deleted successfully'))
        return super().get_success_url()

    def form_valid(self, form):
        self.user = self.object
        if self.user.task_creator.exists() or self.user.task_executor.exists():
            messages.error(
                self.request,
                _("The user cannot be deleted since he's tied with some tasks")
                )
            return redirect('user_list')
            
        response = super().form_valid(form)
        return response
    
