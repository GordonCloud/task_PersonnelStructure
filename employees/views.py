from django.http import HttpResponse
from django.template import loader

from .models import Employee

tr_tag_colors = [
    "gold",
    "gold",
    "gold",
    "PowderBlue",
    "MediumPurple",
    "RosyBrown",
    "LightGreen",
    "OliveDrab",
    "Thistle"
]


def page(request):
    employee_director = Employee.objects.get(hierarchy_level=1)
    if not Employee.employees_tree:
        employee_tree = Employee.get_tree()
    else:
        employee_tree = Employee.employees_tree
    template = loader.get_template('employees/page.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
        'tr_tag_colors': tr_tag_colors
    }
    return HttpResponse(template.render(context, request))


def searchpage(request):
    employee_director = Employee.objects.get(hierarchy_level=1)
    if not Employee.employees_tree:
        employee_tree = Employee.get_tree()
    else:
        employee_tree = Employee.employees_tree
    template = loader.get_template('employees/searchpage.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
    }
    return HttpResponse(template.render(context, request))
