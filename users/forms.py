from django.forms import ModelForm

from users.models import Doctor, Patient


class DoctorCreateUpdateForm(ModelForm):
    """
    Базовая форма создания/редактирования доктора
    """

    class Meta:
        model = Doctor
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
            'position',
            'rank',
            'experience',
            'department',
        )


class DoctorCreateForm(DoctorCreateUpdateForm):
    """
    Форма создания доктора
    """

    pass


class DoctorUpdateForm(DoctorCreateUpdateForm):
    """
    Форма редактирования доктора
    """

    pass


class PatientCreateUpdateForm(ModelForm):
    """
    Базовая форма создания/редактирования пациента
    """

    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'age',
            'gender',
        )


class PatientCreateForm(PatientCreateUpdateForm):
    """
    Форма создания пациента
    """

    pass


class PatientUpdateForm(PatientCreateUpdateForm):
    """
    Форма редактирования пациента
    """

    pass
