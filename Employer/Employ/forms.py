from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, forms

from Employ.models import Employee, Task, Employer


class EmployerForm(ModelForm):
    class Meta:
        model=Employer
        fields=["employer_name","user_name","contact","email","password","address"]

    def clean(self):
        # print("inside clean")
        pass


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=["employee_name","user_name","contact","email","password","address","employer",'task']
        # widgets = {
        #
        #     'employee_name':forms.TextInput(attrs={'class':'form-control-sm'}),
        #     'address':forms.Textarea(attrs={'class':'form-control-col-sm'}),
        #     'user_name':forms.TextInput(attrs={'class':'form-control-sm'}),
        #     'contact':forms.TextInput(attrs={'class':'form-control-sm'}),
        #     'password': forms.TextInput(attrs={'class': 'form-control-sm'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control-sm'}),
        #
        # }
    def clean(self):
        # print("inside clean")
        pass
class UpdateEmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=["contact","password"]

    def clean(self):
            # print("inside clean")
        pass

class AddTaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["task_name","starting_date","ending_date","status","employer"]

    def clean(self):
            # print("inside clean")
        pass


class UpdateTaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["task_name","starting_date","ending_date","status","employer"]

    def clean(self):
            # print("inside clean")
        pass