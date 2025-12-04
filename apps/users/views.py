from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from users.forms import CustomUserChangeForm, CustomUserCreationForm
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
            # prettify later
            errors = form.errors
            return render(
                request,
                'users/create.html',
                context={
                    'form': form,
                    'errors': errors,
                    }
                )


class UpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        form = CustomUserChangeForm(instance=user)
        return render(
            request,
            'users/update.html',
            context={
                'form': form,
                'user': user,
                },
            )
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            # prettify later
            errors = form.errors
            return render(
                request,
                'users/update.html',
                context={
                    'form': form,
                    'user': user,
                    'errors': errors,
                    }
                )
    

class DeleteView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = get_object_or_404(CustomUser, id=user_id)
        return render(
            request,
            'users/delete.html',
            context={
                'user': user,
                },
            )
    
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = CustomUser.objects.get(id=user_id)
        if user:
            user.delete()
        return redirect('user_list')
