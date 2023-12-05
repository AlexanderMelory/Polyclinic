# Generated by Django 5.0 on 2023-12-05 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polyclinic', '0003_alter_department_rooms_qty_and_more'),
        ('users', '0002_alter_user_third_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='polyclinic.department', verbose_name='Отделение'),
        ),
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='Стаж работы'),
        ),
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(blank=True, null=True, verbose_name='Научное звание'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, choices=[(1, 'Заведующий'), (2, 'Врач'), (3, 'Пациент')], default=3, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='third_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
    ]
