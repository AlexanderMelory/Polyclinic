# Generated by Django 5.0 on 2023-12-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='third_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Отчество'),
        ),
    ]