from django.shortcuts import render
from .models import Attendance,Employee,Csv_files
import csv
from django.contrib.auth.decorators import login_required
from .forms import FilerbyDate
# Create your views here.
#uploading csv and parsing it
@login_required(login_url="/admin/")
def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        n = Csv_files()
        n.c_fiel = myfile
        n.save()
        f = open(myfile.name, 'rt')
        reader = csv.DictReader(f)
        for row in reader:
            # print(row)
            at=Attendance()
            e=Employee.objects.get(pk=row['emp_id'])
            at.emp_id=e
            at.time_in=row['time_in']
            at.time_out =row['time_out']
            at.date =row['date']
            at.Absent=(row['absent'])
            at.save()
            print((row['absent']))
            # print(row['date'])
            # print(row['emp_id'])
            # print(row['time_in'])

    return render(request, 'upoadcsv.html')

#filterby month
@login_required(login_url="/admin/")
def filerBYmonth(request):
    if request.method=='GET':

        return render(request,'filterbyDate.html')
    else:
        date=request.POST.get('month')
        emp_id=request.POST.get('emp_id')
        year=date[0:4]
        month=date[5:]
        data=Attendance.objects.filter(emp_id=emp_id,date__year=year,
                                       date__month=int(month)
                                       )
        for d in data:
            print(d)

        print(year)
        print(month)
        return render(request,'filterbyDate.html',{'data':data})
        # filterby day
@login_required(login_url="/admin/")
def filerBYday(request):
    if request.method=='GET':

        return render(request,'filterbyday.html')
    else:
        date=request.POST.get('date')
        print(date)
        # emp_id=request.POST.get('emp_id')
        # year=date[0:4]
        # month=date[5:]
        date=Attendance.objects.filter(date=date)
        for d in date:
            print(d)
        #
        # print(year)
        # print(month)
        return render(request,'filterbyday.html',{'data':date})
        # filterby day and id
@login_required(login_url="/admin/")
def filerBYdayandid(request):
    if request.method=='GET':

        return render(request,'filter by day and id.html')
    else:
        date=request.POST.get('date')
        emp_id=request.POST.get('emp_id')
        print(date)
        # emp_id=request.POST.get('emp_id')
        # year=date[0:4]
        # month=date[5:]
        data=Attendance.objects.filter(emp_id=emp_id,date=date)
        for d in date:
            print(d)
        #
        # print(year)
        # print(month)
        return render(request,'filter by day and id.html',{'data':data})
