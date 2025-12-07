from django.shortcuts import redirect, render
from django.views import View
from statuses.forms import StatusesCreationForm
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