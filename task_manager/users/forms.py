from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    """username = forms.CharField(
        label=_('Username'),
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only'),
        error_messages={
            'unique': _('This username is already taken'),
        }
    )

    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        help_text=_('8+ characters, not common, not entirely numeric')
    )
    
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
        help_text=_('Confirm password')
    )"""

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

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'password',
            'username',
        ]