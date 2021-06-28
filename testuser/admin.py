from django.contrib import admin
from testuser.models import NewUsers
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUsers
    search_fields = ('email', 'user_name', 'first_name',
                     'image_account')
    list_filter = ('email', 'user_name', 'first_name', 'image_account',
                   'is_active', 'is_staff', 'is_drive', 'is_nomal')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'id', 'first_name', 'image_account',
                    'is_active', 'is_staff', 'is_drive', 'is_nomal')
    fieldsets = (
        (None, {'fields': ('email', 'user_name',
         'first_name', 'image_account')}),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'is_drive', 'is_nomal')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'image_account', 'password1', 'password2', 'is_active', 'is_staff', 'is_drive', 'is_nomal')}
         ),
    )


admin.site.register(NewUsers, UserAdminConfig)
