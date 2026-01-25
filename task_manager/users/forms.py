from django import forms
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'password1',
            'password2',
            'username',
        ]


class CustomUserChangeForm(UserChangeForm):

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_('Password'),
        required=False,
        help_text=_('Leave blank to keep the old password.'),
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label=_('Password confirmation'),
        required=False,
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if (password or confirm_password) and password != confirm_password:
            raise forms.ValidationError(_('Passwords are not the same'))
        return cleaned_data

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
        ]