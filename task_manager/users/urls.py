from django.urls import path

from .views import (
    DeleteUserView,
    IndexUserView,
    RegistrationView,
    UpdateUserView,
)

# ../users/
urlpatterns = [
    path('<int:pk>/update/', UpdateUserView.as_view(), name='user_update'),
    path('<int:pk>/delete/', DeleteUserView.as_view(), name='user_delete'),
    path('create/', RegistrationView.as_view(), name='user_create'),
    path('', IndexUserView.as_view(), name='user_list'),
]
