from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from polyclinic.choices import UserRolesChoices, UserGenderChoices
from polyclinic.models import Department


class User(AbstractUser):
    """
    Пользователь
    """

    username = models.CharField(
        'username',
        max_length=254,
        unique=True,
        help_text='Required. 254 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[validators.validate_email],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    third_name = models.CharField('Отчество', max_length=255, blank=True, null=True)
    gender = models.IntegerField('Пол', choices=UserGenderChoices.choices, blank=True, null=True)
    age = models.IntegerField('Возраст', blank=True, null=True)
    email = models.EmailField('Электронная почта', unique=True)
    address = models.CharField('Адрес', max_length=255, default='г.Архангельск')
    department = models.ForeignKey(Department, verbose_name='Отделение', on_delete=models.SET_NULL, blank=True,
                                   null=True)
    role = models.IntegerField('Роль', choices=UserRolesChoices.choices, blank=True, default=UserRolesChoices.PATIENT)
    position = models.CharField('Должность', max_length=255, blank=True, null=True)
    experience = models.IntegerField('Стаж работы', blank=True, null=True)
    rank = models.CharField('Научное звание', blank=True, null=True)

    EMAIL_FIELD = 'username'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.third_name if self.third_name else ""}'
