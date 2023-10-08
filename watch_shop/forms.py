from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

from .models import GENDER_TYPE, FEEDBACK, HOME_COUNTRY, CITY_LIVE, MARRIAGE


class ShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = '__all__'


class WatchesReviewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'


class DeleteWatchesReview(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'


ADMIN = 1
VipClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'Администратор'),
    (VipClient, 'VIP Клиент'),
    (CLIENT, 'Клиент')
)

MALE = 1
FEMALE = 2

LIKE = 1
UNLIKE = 2
PERFECT = 3

FEEDBACK = (
    (LIKE, 'Все нравится'),
    (UNLIKE, 'Не очень'),
    (PERFECT, 'Все прекрасно')
)

KG = 1
KZ = 2
RU = 3
TJ = 4
UZ = 5

HOME_COUNTRY = (
    (KG, 'Кыргызстан'),
    (KZ, 'Казахстан'),
    (RU, 'Россия'),
    (TJ, 'Таджикистан'),
    (UZ, 'Узбекистан')
)

CITY_LIVE = (
    ('Бишкек', 'Бишкек'),
    ('Ташкент', 'Ташкент'),
    ('Алматы', 'Алматы'),
    ('Москва', 'Москва'),
    ('Душанбе', 'Душанбе')
)

MARRIAGE = (
    ('Женат/замужем', 'Женат/замужем'),
    ('Холост(ая)', 'Холост(ая)')
)


class RegistrationNewForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    bank_name = forms.CharField(required=True)
    card_number = forms.CharField(required=True)
    feedback = forms.ChoiceField(choices=FEEDBACK, required=True)
    country_live = forms.ChoiceField(choices=HOME_COUNTRY, required=True)
    city_live = forms.ChoiceField(choices=CITY_LIVE, required=True)
    marriage = forms.ChoiceField(choices=MARRIAGE, required=True)
    user_hobby = forms.CharField(required=True)
    telling_about_you = forms.CharField(required=True)
    profession = forms.CharField(required=True)
    language = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'user_type',
            'gender',
            'bank_name',
            'card_number',
            'feedback',
            'country_live',
            'city_live',
            'marriage',
            'user_hobby',
            'telling_about_you',
            'profession',
            'language'
        )

        def save(self, commit=True):
            user = super(RegistrationNewForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
