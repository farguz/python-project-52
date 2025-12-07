from django.shortcuts import render
from django.views import View
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