# Generated by Django 4.2.5 on 2023-09-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch_shop', '0002_alter_shop_options_rename_tittle_shop_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Укажите название часов'),
        ),
    ]