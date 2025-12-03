from django.forms import ModelForm
from users.models import User


class CreateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'nickname', 'password']