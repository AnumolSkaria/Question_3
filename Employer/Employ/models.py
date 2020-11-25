from django.db import models

# Create your models here.

class Employer(models.Model):
    employer_name=models.CharField(max_length=200, unique=True)
    contact=models.IntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=400)
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.employer_name


class Task(models.Model):
    task_name=models.CharField(max_length=150,unique=True)
    starting_date=models.DateField()
    ending_date=models.DateField()
    employer=models.ForeignKey(Employer,on_delete=models.CASCADE)
    action =(
        ('1', 'Yet to Begin'),
        ('2', 'Started'),
        ('3', 'Completed')
    )
    status = models.CharField(max_length=100, choices=action)

    def __str__(self):
        return self.task_name


class Employee(models.Model):
    employee_name=models.CharField(max_length=200, unique=True)
    contact=models.IntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=400)
    user_name=models.CharField(max_length=200)
    password=models.CharField(max_length=40)
    employer=models.ForeignKey(Employer,on_delete=models.CASCADE)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
