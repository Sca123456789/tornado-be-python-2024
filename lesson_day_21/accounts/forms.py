from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class CostumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
            'age',
        )

    class CostumUserChangeForm(UserChangeForm):
        class Meta:
            model = CustomUser
            fields = (
                "username",
                "email",
                "age",
            )