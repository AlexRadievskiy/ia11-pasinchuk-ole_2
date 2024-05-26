# Generated by Django 3.2.25 on 2024-05-25 23:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(100)])),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('email', models.EmailField(default='no-reply@example.com', max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
