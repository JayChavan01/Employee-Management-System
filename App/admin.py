from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'position', 'join_date']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['position', 'join_date']

admin.site.register(Employee, EmployeeAdmin)