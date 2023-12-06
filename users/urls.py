from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('doctors/', views.DoctorList.as_view(), name='doctors-list'),
    path('doctors/<int:pk>/detail/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('doctors/create/', views.DoctorCreate.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/update/', views.DoctorUpdate.as_view(), name='doctor-update'),
    path('patients/', views.PatientList.as_view(), name='patients-list'),
    path('patients/<int:pk>/detail/', views.PatientDetail.as_view(), name='patient-detail'),
    path('patients/create/', views.PatientCreate.as_view(), name='patient-create'),
    path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patient-update'),
]
