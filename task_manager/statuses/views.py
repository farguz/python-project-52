from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import StatusesCreationForm, StatusesUpdateForm
from .models import Status


# Create your views here.
class IndexStatusView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            'statuses/index.html',
            context={
                'statuses': statuses,
            },
        )
    

class CreateStatusView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = StatusesCreationForm()
        return render(
            request,
            'statuses/create.html',
            context={
                "form": form,
                },
            )

    def post(self, request, *args, **kwargs):
        form = StatusesCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('status_list')
        else:
            # prettify later
            errors = form.errors
            return render(
                request,
                'statuses/create.html',
                context={
                    'form': form,
                    'errors': errors,
                    }
                )
        

class UpdateStatusView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = StatusesUpdateForm(instance=status)
        return render(
            request,
            'statuses/update.html',
            context={
                'form': form,
                'status': status,
                },
            )
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        form = StatusesUpdateForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно изменен')
            return redirect('status_list')
        else:
            # prettify later
            errors = form.errors
            return render(
                request,
                'statuses/update.html',
                context={
                    'form': form,
                    'status': status,
                    'errors': errors,
                }
            )


class DeleteStatusView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        return render(
            request,
            'statuses/delete.html',
            context={
                'status': status,
                },
            )
    
    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = get_object_or_404(Status, id=status_id)
        if status:
            status.delete()
            messages.success(request, 'Статус успешно удален')
        return redirect('status_list')