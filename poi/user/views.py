from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Sum, Count, Q


from user.forms import EditProfileForm, EditInventoryForm, EditEmployeeForm, EditForcastForm
from user.models import EmployeeProfile, InventoryProfile, ForcastedSalesProfile


# home

def base(request):
    return render(request, 'base/base.html')


@login_required
def dashboard(request):
    args = {'user': request.user}
    return render(request, 'user/dashboard.html', args)


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'user/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/user/profile')
        else:
            return redirect('/user/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'user/change_password.html', args)


# Inventory

@login_required
def inventory_adjustment(request):
    inventory_view = InventoryProfile.objects.all()
    form = EditInventoryForm()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    args = {
        'form': form,
        'inventory_view': inventory_view
    }
    return render(request, 'inventory/inventory_adjustment.html', args)


@login_required
def inventory_overview(request):
    inventory_view = InventoryProfile.objects.all()
    args = {
        'user': request.user,
        'inventory_view': inventory_view
    }
    return render(request, 'inventory/inventory_overview.html', args)


@login_required
def extended_values_view(request):
    pass


# Employee


@login_required
def edit_employee(request, id=None):
    instance = get_object_or_404(EmployeeProfile, id=id)
    form = EditEmployeeForm(data=request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/user/view-employee')
    args = {
        'employee': instance.first,
        'instance': instance,
        'form': form,
    }
    return render(request, 'employee/edit_employee.html', args)


@login_required
def create_employee(request):
    form = EditEmployeeForm(data=request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/user/view-employee')
    args = {
        'form': form,
    }
    return render(request, 'employee/create_employee.html', args)


@login_required
def view_employee(request):
    employee_view = EmployeeProfile.objects.all()
    args = {
        'user': request.user,
        'employee_view': employee_view}
    return render(request, 'employee/view_employee.html', args)


# Sales


@login_required
def projected_sales(request, **kwargs):
    sales_view = ForcastedSalesProfile.objects.all()
    projected_sales_sum = ForcastedSalesProfile.objects.aggregate(total_sum=Sum('total'))
    args = {
        'user': request.user,
        'sales_view': sales_view,
        'projected_sales_sum': projected_sales_sum,
    }
    return render(request, 'sales/projected_sales.html', args)


@login_required
def edit_projected_sales(request, id=None):
    edit_sales_view = ForcastedSalesProfile.objects.all()
    instance = get_object_or_404(ForcastedSalesProfile, id=id)
    form = EditForcastForm(data=request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/user/projected-sales')
    args = {
        'edit_sales_view': edit_sales_view,
        'instance': instance,
        'form': form,
    }
    return render(request, 'sales/edit_projected_sales.html', args)


"""
Dashboard chart class

from django.http import JsonResponse
from django.views.generic import View


class DashboardView(View):
    def dashboard(self, request, *args, **kwargs):
        return render(request, 'user/dashboard.html', {})

    def get_data(self, request, *args, **kwargs):
        data = {
            'sales': 1000,
            'guests': 25,
        }
        return JsonResponse(data)  # http response


class InventoryDatabase(models.Model):

    def inventory(self):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

    def create_table(self, inventory):
        c.execute("CREATE TABLE if not EXISTS inventory(
            sequence INTEGER,
            name TEXT,
            sku REAL,
            area TEXT,
            price REAL,
            total REAL,
            )")

        conn.commit()
        conn.close()

        @property
        def employee(self):
            conn = sqlite3.connect('employee.db')

            c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

            conn.commit()

            c.execute("SELECT * FROM employee WHERE last=last", {'last': '#variable'})

            print(c.fetchall())

        def insert_emp(emp):
            with conn:
                c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

        def search_emps_by_name(lastname):
            c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
            return c.fetchall()

        def update_pay(emp, pay):
            with conn:
                c.execute("UPDATE employees SET pay=: pay
                        WHERE first=: first AND last=: last",
                          {'first': emp.first, 'last': emp.last, 'pay': pay})

        def remove_emp(emp):
            with conn:
                c.execute("DELETE from employees WHERE first = :first AND last = :last",
                          {'first': emp.first, 'last': emp.last})


class EmployeeDatabase(models.Model, EmployeeProfile):

    def employee(self):
        conn = sqlite3.connect('employee.db')
        c = conn.cusor()

        c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp_1.first, 'last': emp_1.last, 'pay': emp_1.pay})

        conn.commit()

        c.execute("SELECT * FROM employee WHERE last=last", {'last': '#variable'})

        print(c.fetchall())

    def insert_emp(emp):
        with conn:
            c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

    def search_emps_by_name(lastname):
        c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
        return c.fetchall()

    def update_pay(emp, pay):
        with conn:
# c.execute(UPDATE employees SET pay = :pay
#        WHERE first = :first AND last = :last
#         {'first': emp.first, 'last': emp.last, 'pay': pay})

# def remove_emp(emp):
#    with conn:
#       c.execute("DELETE from employees WHERE first = :first AND last = :last",
#                {'first': emp.first, 'last': emp.last})


@login_required
def index(request):
    numbers = [8572774282]
    name = "Savan Yim"
    args = {"myname": name, "numbers": numbers}
    return render(request, 'user/home.html', args)
# Dashboard

# total = ForcastedSalesProfile.objects.filter(ForcastedSalesProfile[2:8]).aggregate(total=Sum) ['total']
"""
