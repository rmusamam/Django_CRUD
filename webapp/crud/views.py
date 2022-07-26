from django.shortcuts import render ,redirect
#create your views here
from .form import EmployeeForm
from .models import Employee
# Create your views here.
def home(request):
    return render(request,"home.html")

def show(request):
    employee=Employee.objects.all
    return render(request,"show.html",{'employee':employee })

def add(request):
    form=EmployeeForm(request.POST)
    form.sav()
    return redirect('/show')

def load_form(request):
    form= EmployeeForm
    return  render(request,"load_form.html", {'form':form})

def edit(request,id):
    employee= Employee.objects.get(id=id)
    return render(request,'edit.html',{'empolyee':employee})

def update(request, id ):
    employee=Employee.objects.get(id=id)
    form= EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')


