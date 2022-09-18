from django.contrib import admin
from . models import * 
# Register your models here.
admin.site.register(Person)
admin.site.register(Employee_Access)
admin.site.register(Applications)
admin.site.register(Access_Form)
@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("person","ec_number")
    list_filter = ("person","ec_number")
    search_fields = ("ec_number__startswith",)
