from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm


def index(request):
    return render(
        request,
        'index.html',
    )


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(
            request,
            'login.html',
            context={
                'form': form,
                },
            )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_page')
        else:
            # prettify later
            errors = form.errors
            return render(
            request,
            'login.html',
            context={
                'form': form,
                'errors': errors,
                },
            )