from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('polyclinic.urls')),
    path('products/', include('users.urls')),
]
