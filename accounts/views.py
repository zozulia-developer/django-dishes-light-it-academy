from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import redirect

from .forms import LoginRawForm


class LoginFormView(FormView):
    form_class = LoginRawForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password')
        )

        if user and user.is_active:
            login(self.request, user)
            return redirect('/dishes')
        return redirect('/login')

