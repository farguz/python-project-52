from django.urls import path

from .views import (
    # DeleteTaskView,
    IndexTaskView,
    # CreateTaskView,
    # UpdateTaskView,
    # DetailTaskView,
)

# ../tasks/
urlpatterns = [
    # path('<int:id>/update/', UpdateTaskView.as_view(), name='task_update'),
    # path('<int:id>/delete/', DeleteTaskView.as_view(), name='task_delete'),
    # path('<int:id>/', DetailTaskView.as_view(), name='task_detail'),
    # path('create/', CreateTaskView.as_view(), name='task_create'),
    path('', IndexTaskView.as_view(), name='task_list'),
]
