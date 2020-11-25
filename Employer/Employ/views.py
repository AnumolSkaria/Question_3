from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

from Employ.forms import EmployeeForm, UpdateEmployeeForm, AddTaskForm, UpdateTaskForm, EmployerForm
from Employ.models import Employee, Task, Employer


class AddEmployee(CreateView):
    model = Employee
    form_class=EmployeeForm
    template_name = 'Employer/add_employee.html'
    success_url = reverse_lazy('listemploye')

class EmployeeList(ListView):
    model=Employee
    template_name = 'Employer/view_employee.html'
    context_object_name = "qs"

class UpdateEmployee(UpdateView):
    model = Employee
    template_name = 'Employer/update_employee.html'
    form_class = UpdateEmployeeForm
    success_url = reverse_lazy('listemploye')

class DeleteEmployee(DeleteView):
    model = Employee
    template_name = 'Employer/delete_employee.html'
    success_url = reverse_lazy('listemploye')

class AddTask(CreateView):
    model = Task
    form_class=AddTaskForm
    template_name = 'Employer/add_task.html'
    success_url = reverse_lazy('listtask')

class TaskList(ListView):
    model=Task
    template_name = 'Employer/view_task.html'
    context_object_name = "qs"

class UpdateTask(UpdateView):
    model = Task
    template_name = 'Employer/update_task.html'
    form_class = UpdateTaskForm
    success_url = reverse_lazy('listtask')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'Employer/delete_task.html'
    success_url = reverse_lazy('listtask')

class AddEmployer(CreateView):
    model = Employer
    template_name = 'admin_role/add_employer.html'
    form_class = EmployerForm
    success_url = reverse_lazy('home')

class EmployerLogin(TemplateView):
    model=Employer
    template_name = 'Login/Employer_login.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        user = Employer.objects.get(contact=contact, password=password)
        print(user.user_name)
        print(user)
        if user is not None:
            print('ok')
            # EmployerLogin(request,user)
            context={}
            context['user']=user.user_name
            return redirect('addtask')
        else:
            message="incorrect Username or password"
            context={}
            context['message']=message
        return render(request,self.template_name,context)



class EmployeeLogin(TemplateView):
    model=Employee
    template_name = 'Login/Employee_login.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)
    def post(self, request, *args, **kwargs):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        user = Employee.objects.get(contact=contact, password=password)
        print(user.user_name)
        usr=user.user_name
        print(usr)
        # print(user)
        if user is not None:
            print('ok')
            # EmployerLogin(request,user)
            context={}
            context['usr']=usr
            return render(request,'Employee/emp_home.html',context)
        else:
            message="incorrect Username or password"
            context={}
            context['message']=message
        return render(request,self.template_name,context)

def empHome(request):
    return render(request,'Employee/emp_home.html')
def index(request):
    return render(request,'index/index1.html')
def home(request):
    return render(request,'index/home.html')

def logoutUser(request):
    # EmployeeLogin(request)
    return redirect('employerlogin')
def logoutEmployee(request):
    return redirect('employeelogin')
# class ViewTask(TemplateView):
#     def post(self, request, *args, **kwargs):
