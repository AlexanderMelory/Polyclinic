from django.contrib import admin

from users.models import User, Patient, Doctor


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка: Пользователь"""

    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """Админка: Пациент"""

    pass


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Админка: Доктор"""

    pass
