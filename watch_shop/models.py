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
