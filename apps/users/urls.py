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
    path('', IndexView.as_view(), name='user_list'),
    path('create/', RegistrationView.as_view(), name='user_create'),
    # have to move to project root? path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/update/', UpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='user_delete'),
]
