from django.db.models import IntegerChoices


class UserRolesChoices(IntegerChoices):
    """
    Роли пользователей
    """

    LEADER = (1, 'Заведующий')
    DOCTOR = (2, 'Врач')
    PATIENT = (3, 'Пациент')


class UserGenderChoices(IntegerChoices):
    """
    Пол
    """

    MALE = (1, 'Мужской')
    FEMALE = (2, 'Женский')


class TreatmentTypeChoices(IntegerChoices):
    """
    Вид лечения
    """

    OUTPATIENT = (1, 'Амбулаторное')
    NON_OUTPATIENT = (2, 'Неамбулаторное')
