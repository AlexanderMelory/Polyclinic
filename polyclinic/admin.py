from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    """Админка пользователя"""

    search_fields = ('first_name', 'last_name',)
    list_filter = ('is_active',)
    list_display = ('id', 'first_name', 'last_name', 'is_active')
    list_display_links = ('id', 'first_name', 'last_name',)
