# Generated by Django 4.2.5 on 2023-10-01 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watch_shop', '0005_alter_shop_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(verbose_name='Напишите отзыв')),
                ('review_stars', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('review_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_object', to='watch_shop.shop')),
            ],
        ),
    ]