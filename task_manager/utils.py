from django.contrib import messages
from django.shortcuts import redirect


class HandleNoPermissionMixin:
    login_url = 'login'

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                self.error_message_user_is_authenticated
            )
            return redirect(self.url_if_user_is_authenticated)
        else:
            messages.error(
                self.request,
                self.error_message_not_logged
            )
            return redirect(self.login_url)
