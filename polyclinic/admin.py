from django.contrib import admin

from polyclinic.models import Diagnosis, MedicalHistory, Department


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    """Админка: Диагноз"""

    pass


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    """Админка: История болезни"""

    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Админка: История болезни"""

    pass
