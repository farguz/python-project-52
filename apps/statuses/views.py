from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from statuses.forms import StatusesCreationForm, StatusesUpdateForm
from statuses.models import Status


# Create your views here.
class IndexStatusView(View):
    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(
            request,
            'statuses/index.html',
            context={
                'statuses': statuses,
            },
        )
    

class CreateStatusView(View):
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
        

class UpdateStatusView(View):
    """def test_func(self):
        user_id = self.kwargs.get('id')
        return self.request.user.id == user_id or self.request.user.is_superuser"""
    
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
