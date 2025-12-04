from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)
from users.models import CustomUser


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

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name',
            'last_name',
        )