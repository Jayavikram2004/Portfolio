from django.contrib import admin
from .models import (
    AuthGroup,
    AuthGroupPermissions,
    AuthPermission,
    AuthUser,
    AuthUserGroups,
    AuthUserUserPermissions,
    DjangoAdminLog,
    DjangoContentType,
    DjangoMigrations,
    DjangoSession,
    Emp,
)

@admin.register(AuthGroup)
class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(AuthGroupPermissions)
class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'permission')
    list_filter = ('group', 'permission')
    ordering = ('id',)

@admin.register(AuthPermission)
class AuthPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content_type', 'codename')
    search_fields = ('name', 'codename')
    list_filter = ('content_type',)
    ordering = ('id',)

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('id',)

@admin.register(AuthUserGroups)
class AuthUserGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'group')
    list_filter = ('user', 'group')
    ordering = ('id',)

@admin.register(AuthUserUserPermissions)
class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'permission')
    list_filter = ('user', 'permission')
    ordering = ('id',)

@admin.register(DjangoAdminLog)
class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 'user', 'content_type', 'action_flag')
    list_filter = ('user', 'action_flag', 'content_type')
    ordering = ('id',)

@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_label', 'model')
    search_fields = ('app_label', 'model')
    ordering = ('id',)

@admin.register(DjangoMigrations)
class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app', 'name', 'applied')
    search_fields = ('app', 'name')
    ordering = ('id',)

@admin.register(DjangoSession)
class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'expire_date')
    ordering = ('session_key',)

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display = (
        'emp_no', 'emp_name', 'sex', 'location', 'basic', 'hra', 'desgn', 
        'dept', 'salary', 'addr1', 'addr2', 'addr3', 'pin', 'ph_no', 
        'rep_officer_no', 'rep_officer_name'
    )
    search_fields = ('emp_name', 'location', 'desgn', 'dept')
    ordering = ('emp_no',)

# You can add custom configurations as needed for each admin class.
