from django.db import models


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

