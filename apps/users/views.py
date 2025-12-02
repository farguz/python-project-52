from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'users/index.html',
        )
    

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'users/create.html',
        )
    

class UpdateView(View):
    pass
    

class DeleteView(View):
    pass