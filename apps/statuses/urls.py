from django.urls import path
from statuses.views import (
    CreateStatusView,
    DeleteStatusView,
    IndexStatusView,
    UpdateStatusView,
)

# ../statuses/
urlpatterns = [
    path('<int:id>/update/', UpdateStatusView.as_view(), name='status_update'),
    path('<int:id>/delete/', DeleteStatusView.as_view(), name='status_delete'),
    path('create/', CreateStatusView.as_view(), name='status_create'),
    path('', IndexStatusView.as_view(), name='status_list'),
]
