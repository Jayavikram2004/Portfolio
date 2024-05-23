from django.shortcuts import render, redirect,get_object_or_404
from .models import Emp
from .forms import EmpForm
from django.contrib import messages
from django.http import JsonResponse

def search_recommendations(request):
    q = request.GET.get('q', None)
    q2 = request.GET.get('q2', None)

    if q:
        employees = Emp.objects.filter(emp_no__icontains=q).values('emp_no', 'emp_name')[:10]
    elif q2:
        employees = Emp.objects.filter(emp_name__icontains=q2).values('emp_no', 'emp_name')[:10]
    else:
        employees = []

    return JsonResponse(list(employees), safe=False)

def emp_create(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
        else:
            messages.info(request, 'The Employee Number already exists!')
    else:
        form = EmpForm()
    
    return render(request, 'emp_form.html', {'form': form})

def emp_list(request):
    query = request.GET.get('q')
    query2 = request.GET.get('q2')
    if query:
        employees = Emp.objects.filter(emp_no__icontains=query)
    elif query2: 
        employees = Emp.objects.filter(emp_name__icontains=query2)
    else:
        employees = Emp.objects.all().order_by('emp_no')
    return render(request, 'emp_list.html', {'employees': employees})
    


def emp_detail(request, emp_no):
    employee = get_object_or_404(Emp, emp_no=emp_no)
    print("employee",employee.emp_no)
    return render(request, 'emp_detail.html', {'employee': employee})

def emp_update(request, emp_no):
    employee = get_object_or_404(Emp, emp_no=emp_no)
    
    if request.method == 'POST':
        form = EmpForm(request.POST, instance=employee)
        
        if form.is_valid():
            basic = form.cleaned_data.get('basic', 0)
            hra = form.cleaned_data.get('hra', 0)
            salary = basic + hra
            employee.salary = salary
            form.save()
            return redirect('emp_list')
    else:
        form = EmpForm(instance=employee)
    
    return render(request, 'emp_form2.html', {'form': form, 'employee': employee})



def emp_delete(request, emp_no):
    employee = get_object_or_404(Emp, emp_no=emp_no)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_list')
    return render(request, 'emp_confirm_delete.html', {'employee': employee})



