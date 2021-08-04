from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.shortcuts import redirect

from .forms import LoginRawForm, SignUpForm


class LoginFormView(FormView):
    form_class = LoginRawForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user and user.is_active:
            login(self.request, user)
            return redirect('/dishes')
        return redirect('/login')


class SignUpFormView(CreateView):
    form_class = SignUpForm
    success_url = '/'
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data['password'])

        return super().form_valid(form)
