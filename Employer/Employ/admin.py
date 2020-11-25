from django.contrib import admin

# Register your models here.
from Employ.models import Employee, Task, Employer

admin.site.register(Employer)
admin.site.register(Task)
admin.site.register(Employee)

