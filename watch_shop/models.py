from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    COLOR = (
        ('Красный', 'Красный'),
        ('Белый', 'Белый'),
        ('Черный', 'Черный')
    )

    SIZE = (
        ('Большой', 'Большой'),
        ('Средний', 'Средний'),
        ('Маленький', 'Маленький')
    )
    title = models.CharField('Укажите название часов', max_length=100, null=True)
    description = models.TextField('Укажите описание часов', blank=True, null=True)
    image = models.ImageField('Добавьте фото', upload_to='images/', null=True)
    country_made = models.TextField('Укажите страну производителя', max_length=50, null=True)
    color = models.CharField('Укажите цвет', max_length=100, choices=COLOR)
    size = models.CharField('Укажите размер', max_length=100, choices=SIZE)
    video = models.URLField('Укажите ссылку')
    cost = models.PositiveIntegerField('Укажите цену')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'


class Reviews(models.Model):
    REVIEW_STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    review_object = models.ForeignKey(Shop, on_delete=models.CASCADE,
                                      related_name='comment_object')
    review_text = models.TextField('Напишите отзыв')
    review_stars = models.CharField(max_length=100, choices=REVIEW_STARS)
    review_created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Добавить отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.review_text


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

GENDER_TYPE = (
    (MALE, 'М'),
    (FEMALE, 'Ж')
)

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


class CustomUser(User):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    user_type = models.IntegerField(choices=USER_TYPE,
                                    verbose_name="Выберите тип пользователя", null=True)
    phone_number = models.CharField("ваш номер сотового:", max_length=13, null=True)
    age = models.PositiveIntegerField("Укажите возраст?", default=15, null=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Ваш пол', null=True)
    bank_name = models.CharField("Напишите название банка", max_length=100, null=True)
    card_number = models.CharField("Укажите номер вашей карты:", max_length=20, null=True)
    feedback = models.IntegerField(choices=FEEDBACK, verbose_name="Как ваш нам сайт?", null=True)
    country_live = models.IntegerField(choices=HOME_COUNTRY, verbose_name="Страна проживания?", null=True)
    city_live = models.IntegerField(choices=CITY_LIVE, verbose_name="Ваш город проживания", null=True)
    marriage = models.IntegerField(choices=MARRIAGE, verbose_name="Ваше семейное положение?", null=True)
    user_hobby = models.CharField("укажите ваше хобби", max_length=100, null=True)
    telling_about_you = models.CharField("Расскажите не много о себе", max_length=200, null=True)
    profession = models.CharField("Укажите вашу профессию", max_length=100, null=True)
    language = models.CharField("Укажите ваш язык", max_length=100, null=True)