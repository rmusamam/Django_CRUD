from django.shortcuts import render ,redirect
# Create your views here.
from .forms import employeeForm
from .models import employee

def home(request):
    return render(request,"home.html")
def load_form(request):
    form = employeeForm
    return render(request , "load_form.html",{'form':form})
def add(request):
    form =employeeForm(request.POST)
    form.save()
    return redirect('/show')
def show(request):
    employee =employee.objects.all
    return render(request,"show.html",{'employee':employee})
def edit(request, id):
    employee =employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})
def update(request, id):
    employee =employee.objects.get(id=id)
    form =employeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')
def delete(request, id):
    employee =employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')