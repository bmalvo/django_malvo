from django.contrib.auth.forms import (
  AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)


class SubmittableAuthenticationForm(LoginView):
    template_name = 'form.html'


class SubmittablePasswordChangeForm(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')
