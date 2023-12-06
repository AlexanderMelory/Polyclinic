from django.urls import path
from polyclinic import views

app_name = 'polyclinic'

urlpatterns = [
    path('list/', views.DepartmentList.as_view(), name='list'),
    path('detail/<int:pk>/', views.DepartmentDetail.as_view(), name='detail'),
]
