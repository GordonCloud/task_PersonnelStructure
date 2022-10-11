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

    def __str__(self):
        return self.last_name + " " + self.first_name + \
               " " + self.middle_name


class EmployeeTree:
    full_tree = []

    def __init__(self, employees):
        self._employees = employees
        self.employees_tree = []

        self.get_tree()

    def get_tree(self):
        upper_level_employees_list = self._get_upper_lvl_from_queryset()
        for employee in upper_level_employees_list:
            self.employees_tree.append(employee)
            manager = employee
            self._add_subordinates_to_tree(manager=manager)
        return self.employees_tree

    def _get_upper_lvl_from_queryset(self):
        upper_lvl = int(100)
        upper_level_employees_list = []
        for employee in self._employees:
            if employee.hierarchy_level > upper_lvl:
                pass
            elif employee.hierarchy_level == upper_lvl:
                upper_level_employees_list.append(employee)
            else:
                upper_level_employees_list.clear()
                upper_level_employees_list.append(employee)
                upper_lvl = employee.hierarchy_level
        return upper_level_employees_list

    def _add_subordinates_to_tree(self, manager):
        subordinates = list(Employee.objects.filter(manager=manager)[:5])
        subordinates_filtered = list(set(subordinates) & set(self._employees))
        for employee in subordinates_filtered:
            self.employees_tree.append(employee)
            self._add_subordinates_to_tree(employee)

    def clear_tree(self):
        self.employees_tree.clear()
