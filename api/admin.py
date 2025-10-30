from django.contrib import admin
from .models import Employee, Role, Leave


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'role',
        'phone_number',
        'address',
        'cv_link',
    )
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    ordering = ('first_name',)
    readonly_fields = ('profile_picture_preview',)

    fieldsets = (
        ('Personal Info', {
            'fields': ('profile_picture', 'profile_picture_preview', 'first_name', 'last_name', 'email', 'phone_number', 'address')
        }),
        ('Professional Info', {
            'fields': ('role', 'cv')
        }),
    )

    def profile_picture_preview(self, obj):
        if obj.profile_picture:
            return f'<img src="{obj.profile_picture.url}" width="80" height="80" style="border-radius:50%;" />'
        return "(No image)"
    profile_picture_preview.allow_tags = True
    profile_picture_preview.short_description = 'Profile Picture'

    def cv_link(self, obj):
        if obj.cv:
            return f'<a href="{obj.cv.url}" target="_blank">Download CV</a>'
        return "(No CV uploaded)"
    cv_link.allow_tags = True
    cv_link.short_description = 'CV'


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'start_date', 'end_date', 'approval')
    list_filter = ('approval',)
    search_fields = ('employee__first_name', 'employee__last_name')
    date_hierarchy = 'start_date'
