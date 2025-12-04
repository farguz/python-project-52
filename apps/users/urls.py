from django.urls import path
from users.views import (
    DeleteView,
    IndexView,
    # LoginView,
    RegistrationView,
    UpdateView,
)

# ../users/
urlpatterns = [
    # have to move to project root? path('login/', LoginView.as_view(), name='login'),
    path('<int:id>/update/', UpdateView.as_view(), name='user_update'),
    path('<int:id>/delete/', DeleteView.as_view(), name='user_delete'),
    path('create/', RegistrationView.as_view(), name='user_create'),
    path('', IndexView.as_view(), name='user_list'),
]
