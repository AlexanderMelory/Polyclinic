from django.contrib.auth.models import AbstractUser
from django.db import models
from polyclinic.choices import UserRolesChoices, UserGenderChoices
from polyclinic.models import Department


class User(AbstractUser):
    """
    Пользователь
    """

    pass


class BaseDoctorPatient(models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    gender = models.IntegerField('Пол', choices=UserGenderChoices.choices, blank=True, null=True)
    age = models.IntegerField('Возраст', blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, default='г.Архангельск')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.get_role_display()} {self.first_name} {self.last_name}'


class Doctor(BaseDoctorPatient):
    """
    Доктор
    """

    department = models.ForeignKey(
        Department, verbose_name='Отделение', on_delete=models.SET_NULL, blank=True, null=True
    )
    role = models.IntegerField('Роль', choices=UserRolesChoices.choices, blank=True, default=UserRolesChoices.DOCTOR)
    position = models.CharField('Должность', max_length=255, blank=True, null=True)
    experience = models.IntegerField('Стаж работы', blank=True, null=True)
    rank = models.CharField('Научное звание', blank=True, null=True)


class Patient(BaseDoctorPatient):
    """
    Пациент
    """

    role = models.IntegerField('Роль', choices=UserRolesChoices.choices, blank=True, default=UserRolesChoices.PATIENT)
