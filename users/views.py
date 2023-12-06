from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from users.forms import DoctorCreateForm, DoctorUpdateForm, PatientUpdateForm, PatientCreateForm
from users.models import Doctor, Patient


class DoctorList(ListView):
    """
    Список докторов
    """

    queryset = Doctor.objects.all()
    template_name = 'users/doctors/list.html'
    context_object_name = 'doctors'


class DoctorDetail(DetailView):
    """
    Детальный просмотр доктора
    """

    model = Doctor
    template_name = 'users/doctors/detail.html'
    context_object_name = 'doctor'
    back_url = reverse_lazy('users:doctors-list')


class DoctorCreate(CreateView):
    """
    Создание доктора
    """

    model = Doctor
    form_class = DoctorCreateForm
    template_name = 'users/doctors/create.html'
    title = 'Создание доктора'
    back_url = reverse_lazy('users:doctors-list')

    def get_success_url(self):
        return self.object.get_detail_url()


class DoctorUpdate(UpdateView):
    """
    Редактирование доктора
    """

    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'users/doctors/update.html'
    title = 'Редактирование доктора'
    back_url = reverse_lazy('users:doctors-list')

    def get_success_url(self):
        return self.object.get_detail_url()


class PatientList(ListView):
    """
    Список пациентов
    """

    queryset = Patient.objects.all()
    template_name = 'users/patients/list.html'
    context_object_name = 'patients'


class PatientDetail(DetailView):
    """
    Детальный просмотр пациента
    """

    model = Patient
    template_name = 'users/patients/detail.html'
    context_object_name = 'patient'
    back_url = reverse_lazy('users:patients-list')


class PatientCreateUpdateMixin:
    """
    Базовый класс создания/редактирования пациента
    """

    model = Patient
    back_url = reverse_lazy('users:patients-list')

    def get_success_url(self):
        return self.object.get_detail_url()


class PatientCreate(PatientCreateUpdateMixin, CreateView):
    """
    Создание пациента
    """

    form_class = PatientCreateForm
    template_name = 'users/patients/create.html'
    title = 'Создание пациента'


class PatientUpdate(PatientCreateUpdateMixin, UpdateView):
    """
    Редактирование пациента
    """

    form_class = PatientUpdateForm
    template_name = 'users/patients/update.html'
    title = 'Редактирование пациента'
