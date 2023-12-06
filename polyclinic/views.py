from django.views.generic import ListView, DetailView

from polyclinic.models import Department


class DepartmentList(ListView):
    """
    Список отделений
    """

    queryset = Department.objects.all()
    template_name = 'polyclinic/departments/list.html'
    context_object_name = 'departments'


class DepartmentDetail(DetailView):
    """
    Просмотр отделения
    """

    model = Department
    template_name = 'polyclinic/departments/detail.html'
    context_object_name = 'department'
