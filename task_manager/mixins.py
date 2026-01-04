from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class BasePermissionMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    only superuser/admin or object creator
    have enough rights to delete/update object

    labels and statuses - any auth user are free to upd/del
    tasks and users - only its creator are able to modify object
    """

    permission_denied_message = ""
    default_error_redirect_url = reverse_lazy('index_page')

    def get_redirect_url(self):
        return getattr(self, 'error_redirect_url', self.default_error_redirect_url)
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.get_redirect_url())
        return super().handle_no_permission()