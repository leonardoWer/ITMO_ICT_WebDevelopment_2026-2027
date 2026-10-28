from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

INPUT_CLASSES = "w-full bg-neutral-900 border border-neutral-700 text-white px-4 py-3 rounded-sm focus:outline-none focus:border-red-600 transition"

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'display_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASSES})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': INPUT_CLASSES})