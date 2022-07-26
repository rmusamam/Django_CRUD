from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def show(request):
    employee=Employee.objects.all
    return render(request,"show.html",{'employee':employee })