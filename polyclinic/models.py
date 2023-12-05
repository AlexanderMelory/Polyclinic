from django.db import models
from django.conf import settings
from polyclinic.choices import TreatmentTypeChoices


class Department(models.Model):
    """
    Отделение
    """

    name = models.CharField('Название', max_length=255, unique=True)
    floor = models.IntegerField('Этаж')
    rooms_qty = models.IntegerField('Количество комнат', default=0)
    leader = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name='Руководитель отделения', related_name='leader_department', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    """
    Диагноз
    """

    name = models.CharField('Название', max_length=255)
    symptoms = models.CharField('Симптомы', max_length=255, default='Головная боль')
    treatment_time = models.DateField('Время на лечение', default=0)


class MedicalHistory(models.Model):
    """
    История болезни
    """

    patient = models.OneToOneField(
        settings.AUTH_USER_MODEL, verbose_name='Пациент', on_delete=models.CASCADE, related_name='patient_history'
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Врач',
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name='medical_histories',
    )
    diagnosis = models.OneToOneField(
        Diagnosis, verbose_name='Диагноз', on_delete=models.SET_DEFAULT, related_name='diagnosis', default=None
    )
    health_procedures = models.CharField('Название лечения', max_length=1000)
    treatment_typ = models.IntegerField(
        'Вид лечения', choices=TreatmentTypeChoices.choices, default=TreatmentTypeChoices.OUTPATIENT
    )
