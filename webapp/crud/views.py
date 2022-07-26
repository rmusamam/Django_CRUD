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