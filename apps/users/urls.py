from django.urls import path
from users.views import RegistrationView, DeleteView, IndexView, UpdateView

# ../users/
urlpatterns = [
    path('', IndexView.as_view()),
    path('create/', RegistrationView.as_view()),
    path('<int:user_id>/update/', UpdateView.as_view()),
    path('<int:user_id>/delete/', DeleteView.as_view()),
]
