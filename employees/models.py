from django.db import models


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
        return self.last_name + " " + self.first_name +\
               " " + self.middle_name
