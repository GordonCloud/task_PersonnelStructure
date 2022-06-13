from django.db.models.query import QuerySet
from django.db import models
from django.db.models import Max


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    position = models.TextField(max_length=100)
    employment_date = models.DateField()
    salary = models.IntegerField()
    hierarchy_level = models.IntegerField(default=5)
    manager = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

    employees_tree = []

    def __str__(self):
        return self.last_name + " " + self.first_name + \
               " " + self.middle_name

    @classmethod
    def get_tree(cls):
        second_level_queryset = cls.objects.filter(hierarchy_level=2)
        for employee in second_level_queryset:
            cls.employees_tree.append(employee)
            manager = employee
            cls.add_subordinates_to_tree(manager=manager)

    @classmethod
    def add_subordinates_to_tree(cls, manager):
        subordinates = cls.objects.filter(manager=manager)[:5]
        for employee in subordinates:
            cls.employees_tree.append(employee)
            cls.add_subordinates_to_tree(employee)
