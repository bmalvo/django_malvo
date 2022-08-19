from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.db.transaction import atomic
from django.forms import Textarea, CharField
from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    biography = CharField(
        label='Tell us your story with movies', widget=Textarea, min_length=40
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        biography = self.cleaned_data['biography']
        profile = Profile(biography=biography, user=result)
        if commit:
            profile.save()
        return result


class SubmittableAuthenticationForm(AuthenticationForm):
    template_name = 'form.html'


class SubmittablePasswordChangeForm(PasswordChangeForm):
    template_name = 'form.html'
