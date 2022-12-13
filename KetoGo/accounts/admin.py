from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from KetoGo.accounts.forms import RegisterUserForm, EditUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'avatar', 'age')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'),
            },
        ),
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'avatar', 'age'),
            },
        ),
    )
    list_display = ['email', 'is_staff', 'date_joined', 'last_login', ]
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    search_help_text = 'Search user by email...'
    ordering = ('email', 'date_joined', 'last_login')
    filter_horizontal = ('groups', 'user_permissions',)

    # exclude = ('username', 'is_active', 'email', 'password1', 'password2', 'date_joined', 'last_login',)
    form = EditUserForm
    add_form = RegisterUserForm
