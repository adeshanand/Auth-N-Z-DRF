from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'contact', )

admin.site.unregister(Group)

admin.site.site_header = 'Sample'