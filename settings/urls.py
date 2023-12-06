from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='polyclinic:list'), name='index'),
    path('polyclinic/', include('polyclinic.urls')),
    path('users/', include('users.urls')),
]
