from django.urls import path

from .views import (
    CreateTaskView,
    # DetailTaskView,
    DeleteTaskView,
    IndexTaskView,
    UpdateTaskView,
)

# ../tasks/
urlpatterns = [
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='task_update'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='task_delete'),
    # path('<int:pk>/', DetailTaskView.as_view(), name='task_detail'),
    path('create/', CreateTaskView.as_view(), name='task_create'),
    path('', IndexTaskView.as_view(), name='task_list'),
]
