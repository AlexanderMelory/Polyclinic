from datetime import timedelta

from django.db import models
from django.urls import reverse_lazy

from polyclinic.choices import TreatmentTypeChoices


class Department(models.Model):
    """
    Отделение
    """

    name = models.CharField('Название', max_length=255, unique=True)
    floor = models.IntegerField('Этаж')
    rooms_qty = models.IntegerField('Количество комнат', blank=True, default=0)
    leader = models.OneToOneField(
        'users.Doctor',
        verbose_name='Руководитель отделения',
        related_name='leader_department',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse_lazy('polyclinic:detail', kwargs={'pk': self.pk})


class Diagnosis(models.Model):
    """
    Диагноз
    """

    name = models.CharField('Название', max_length=255)
    symptoms = models.CharField('Симптомы', max_length=255, default='Головная боль')
    treatment_time = models.DurationField('Время на лечение', blank=True, default=timedelta(days=10))

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'

    def __str__(self):
        return self.name


class MedicalHistory(models.Model):
    """
    История болезни
    """

    patient = models.OneToOneField(
        'users.Patient', verbose_name='Пациент', on_delete=models.CASCADE, related_name='patient_history'
    )
    doctor = models.ForeignKey(
        'users.Doctor',
        verbose_name='Врач',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='medical_histories',
    )
    diagnosis = models.OneToOneField(
        Diagnosis, verbose_name='Диагноз', on_delete=models.SET_NULL, related_name='diagnosis', blank=True, null=True
    )
    health_procedures = models.CharField('Название лечения', max_length=1000)
    treatment_type = models.IntegerField(
        'Вид лечения', choices=TreatmentTypeChoices.choices, default=TreatmentTypeChoices.OUTPATIENT
    )

    class Meta:
        verbose_name = 'История болезни'
        verbose_name_plural = 'Истории болезней'

    def __str__(self):
        return f'История болезни {self.patient.get_role_display().lower()}а {self.patient.first_name} {self.patient.last_name}'
