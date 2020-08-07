# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core.models import User, ActivityPeriod


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'real_name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('uid', 'real_name', 'tz')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        (_('Personal Info'), {'fields': ('uid', 'real_name', 'tz')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
    )


class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time')


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
