from django import forms
from . import models, parser


class ParserForms(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == '':
            cinema_parser = parser.parser()
            for i in cinema_parser:
                models.RussiaCinema.objects.create(**i)