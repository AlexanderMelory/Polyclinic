# Generated by Django 5.0 on 2023-12-06 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('rooms_qty', models.IntegerField(blank=True, default=0, verbose_name='Количество комнат')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('symptoms', models.CharField(default='Головная боль', max_length=255, verbose_name='Симптомы')),
                ('treatment_time', models.DurationField(blank=True, default=datetime.timedelta(days=10), verbose_name='Время на лечение')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_procedures', models.CharField(max_length=1000, verbose_name='Название лечения')),
                ('treatment_type', models.IntegerField(choices=[(1, 'Амбулаторное'), (2, 'Неамбулаторное')], default=1, verbose_name='Вид лечения')),
            ],
        ),
    ]
