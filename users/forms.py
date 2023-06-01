from django.contrib.auth.forms import UserCreationForm
from .models import User


class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Your Email',
                                                  'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none '
                                                           'block w-full'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password',
                                                      'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none '
                                                               'block w-full'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password',
                                                      'class': 'p-2 bg-gray-200 rounded-sm text-gray-900 outline-none '
                                                               'block w-full'})
