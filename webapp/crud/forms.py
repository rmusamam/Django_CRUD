from django import forms
from .models import Employee

class EmployeeForm (from.ModelForm):
    class Meta:
        model =  Employee
        fields = "__all__"