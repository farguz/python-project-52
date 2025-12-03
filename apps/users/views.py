from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from users.forms import CreateUserForm
from users.models import User


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(
            request,
            'users/index.html',
            context={
                'users': users,
            }
        )
    

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'users/create.html',
        )

    def post(self, request, *args, **kwargs):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

        # no matter what, fix according to check results
        return redirect(reverse('user_list'))



class LoginView(View):
    pass

class UpdateView(View):
    pass
    

class DeleteView(View):
    pass