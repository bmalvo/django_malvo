import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, Textarea, ModelForm

from viewer.models import Genre, Movie


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):

    class Meta:
      model = Movie
      fields = '__all__'

    title = CharField(validators=[capitalized_validator])
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    # def clean_description(self):
    #     # Force each sentence of the description to be capitalized.
    #     initial = self.cleaned_data['description']
    #     sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
    #     cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
    #     self.cleaned_data['description'] = cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'commedy' and result['rating'] > 5:
          raise ValidationError(
              "Commedies aren't so good to be rated over 5.")
        return result
