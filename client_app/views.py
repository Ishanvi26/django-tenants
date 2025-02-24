from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, "client_index.html", {"employees": employees})

def create_employee(request, name):
    if request.POST:
        name=request.POST.get("name")
        employee=Employee(name=name)
        employee.save()
        return redirect("client_index")
    return HttpResponse(f"<h1>{request.tenant} employee, {name} created.</h1>")
