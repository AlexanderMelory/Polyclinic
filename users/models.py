from django.contrib.auth.models import AbstractUser
from django.db import models
from polyclinic.choices import UserRolesChoices, UserGenderChoices
from polyclinic.models import Department


class User(AbstractUser):
    """
    Пользователь
    """

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    third_name = models.CharField('Отчество', max_length=255)
    gender = models.IntegerField('Пол', choices=UserGenderChoices.choices)
    age = models.IntegerField('Возраст')
    address = models.CharField('Адрес', max_length=255, default='г.Архангельск')
    department = models.ForeignKey(Department, verbose_name='Отделение', on_delete=models.SET_DEFAULT, default=None)
    role = models.IntegerField('Роль', choices=UserRolesChoices.choices, default=UserRolesChoices.PATIENT)
    position = models.CharField('Должность', max_length=255, default=None)
    experience = models.IntegerField('Стаж работы', default=None)
    rank = models.CharField('Научное звание', default=None)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.third_name}'
