from django.contrib import admin
from django.urls import path

from Employ.views import AddEmployee, EmployeeList, UpdateEmployee, DeleteEmployee, AddTask, TaskList, UpdateTask, \
    DeleteTask, AddEmployer, EmployerLogin, EmployeeLogin, index, logoutUser, home, empHome, logoutEmployee

urlpatterns = [
    path('employer',AddEmployer.as_view(),name='addemployer'),
    path('employee',AddEmployee.as_view(),name='addemployee'),
    path('listemployee',EmployeeList.as_view(),name='listemploye'),
    path('updateemployee/<str:pk>', UpdateEmployee.as_view(), name='updateemployee'),
    path('deleteemployee/<str:pk>', DeleteEmployee.as_view(), name='deleteemployee'),
    path('addtask',AddTask.as_view(),name='addtask'),
    path('listtask',TaskList.as_view(),name='listtask'),
    path('updatetask/<str:pk>', UpdateTask.as_view(), name='updatetask'),
    path('deletetask/<str:pk>', DeleteTask.as_view(), name='deletetask'),

    path('employerlogin',EmployerLogin.as_view(),name='employerlogin'),
    path('employeelogin',EmployeeLogin.as_view(),name='employeelogin'),
    path("index",index,name='index'),
    path('logsout',logoutUser,name='logout'),
    path('logsoutemployee',logoutEmployee,name='logoutemploy'),
    path('home',home,name='home'),
    path('emphome',empHome,name='emphome')
    # path('adminlogin',AdminLogin,name='adminlogin')
    # path('updatestatus')

]
