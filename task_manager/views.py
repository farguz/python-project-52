from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginForm


def index(request):
    return render(
        request,
        'index.html',
    )


class TaskManagerLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, 'Вы успешно вошли в систему!')
        return reverse_lazy('index_page')
         

class TaskManagerLogoutView(LoginRequiredMixin, LogoutView):

    next_page = reverse_lazy('index_page')

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Вы успешно вышли из профиля!')
        return super().post(request, *args, **kwargs)
