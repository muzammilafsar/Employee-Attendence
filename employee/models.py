from django.db import models
from datetime import date,time,datetime
# Create your models here.
class Csv_files(models.Model):
    c_fiel=models.FileField()

#creating table for employee
class Employee(models.Model):

    emp_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

#creating table for Attendance
class Attendance(models.Model):
    Absent=models.BooleanField(default=True)
    emp_id=models.ForeignKey(Employee,on_delete=models.CASCADE)
    date=models.DateField(default=date.today())
    time_in= models.TimeField(default=datetime.now().time())
    time_out = models.TimeField(default=datetime.now().time())

