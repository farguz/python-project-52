from django.shortcuts import redirect, render
from django.views import View
from users.forms import CustomUserCreationForm
from users.models import CustomUser


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        return render(
            request,
            'users/index.html',
            context={
                'users': users,
            },
        )
    

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        return render(
            request,
            'users/create.html',
            context={
                "form": form,
                },
            )

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            errors = form.errors
            return render(
                request,
                'users/create.html',
                context={
                    'form': form,
                    'errors': errors,
                    })


class LoginView(View):
    pass


class UpdateView(View):
    pass
    

class DeleteView(View):
    pass