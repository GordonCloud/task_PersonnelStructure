from django.http import HttpResponse
from django.template import loader

from .models import Employee


def page(request):
    employee_director = Employee.objects.get(hierarchy_level=1)
    second_level_employees = Employee.objects.filter(hierarchy_level=2)
    employee_tree = Employee.get_tree
    template = loader.get_template('employees/page.html')
    context = {
        'employee_director': employee_director,
        'second_level_employees': second_level_employees,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree
    }
    return HttpResponse(template.render(context, request))
