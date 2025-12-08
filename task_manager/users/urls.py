from django.urls import path

from .views import (
    DeleteView,
    IndexView,
    RegistrationView,
    UpdateView,
)

# ../users/
urlpatterns = [
    path('<int:id>/update/', UpdateView.as_view(), name='user_update'),
    path('<int:id>/delete/', DeleteView.as_view(), name='user_delete'),
    path('create/', RegistrationView.as_view(), name='user_create'),
    path('', IndexView.as_view(), name='user_list'),
]
