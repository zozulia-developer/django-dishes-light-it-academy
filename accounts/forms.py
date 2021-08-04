from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField, PasswordInput, TextInput, EmailInput
from django.contrib.auth import get_user_model


class SignUpForm(ModelForm):
    username = CharField(
        max_length=30,
        widget=TextInput(attrs={'class': 'form-control'})
    )
    email = CharField(
        max_length=40,
        widget=EmailInput(attrs={'class': 'form-control'})
    )
    password = CharField(
        max_length=40,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = CharField(
        max_length=40,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def clean(self):
        password = self.cleaned_data['password']
        confirm = self.cleaned_data['confirm_password']

        if password != confirm:
            raise ValidationError('Password not equal!')

        return self.cleaned_data


class LoginRawForm(Form):
    username = CharField(
        max_length=30,
        widget=TextInput(attrs={'class': 'form-control'})
    )
    password = CharField(
        max_length=40,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )
