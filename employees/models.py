from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    position = models.TextField(max_length=100)
    employment_date = models.DateField()
    salary = models.IntegerField()
    manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
