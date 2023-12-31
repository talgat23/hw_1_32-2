# Generated by Django 4.2.5 on 2023-09-13 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
