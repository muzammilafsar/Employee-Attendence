from django.contrib import admin
from .models import Csv_files,Attendance,Employee
# Register your models here.
#registering on admin panel
admin.site.register(Csv_files)
admin.site.register(Attendance)
admin.site.register(Employee)