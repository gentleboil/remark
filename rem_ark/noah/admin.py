from django.contrib import admin

# Register your models here.

from .models import employee
@admin.register(employee)
class employeeAdmin(admin.ModelAdmin):
   list_display=['sex','age']

from .models import role
@admin.register(role)
class roleAdmin(admin.ModelAdmin):
   list_display=['role_id']