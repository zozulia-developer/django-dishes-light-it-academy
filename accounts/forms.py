from django.forms import ModelForm, Form, CharField, PasswordInput, TextInput
from django.contrib.auth import get_user_model


class SignUpForm(ModelForm):
    password = CharField(max_length=40, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class LoginRawForm(Form):
    username = CharField(
        max_length=30,
        widget=TextInput(attrs={'class': 'form-control'})
    )
    password = CharField(
        max_length=40,
        widget=PasswordInput(attrs={'class': 'form-control'})
    )
