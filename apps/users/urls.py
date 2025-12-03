from django.urls import path
from users.views import DeleteView, IndexView, RegistrationView, UpdateView, LoginView

# ../users/
urlpatterns = [
    path('', IndexView.as_view(), name='user_list'),
    path('create/', RegistrationView.as_view(), name='user_create'),
    path('create/', LoginView.as_view(), name='login'),
    path('<int:user_id>/update/', UpdateView.as_view(), name='user_update'),
    path('<int:user_id>/delete/', DeleteView.as_view(), name='user_delete'),
]
