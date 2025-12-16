from django.urls import path

from .views import (
    CreateLabelView,
    DeleteLabelView,
    IndexLabelView,
    UpdateLabelView,
)

# ../labels/
urlpatterns = [
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='label_update'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='label_delete'),
    path('create/', CreateLabelView.as_view(), name='label_create'),
    path('', IndexLabelView.as_view(), name='label_list'),
]
