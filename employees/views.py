from django.http import HttpResponse
from django.template import loader

from .models import Employee

tr_tag_colors = [
    "gold",
    "gold",
    "gold",
    "aquamarine",
    "MediumPurple",
    "RosyBrown",
    "LightGreen",
    "OliveDrab",
    "Thistle"
]


def page(request):
    employee_director = Employee.objects.get(hierarchy_level=1)
    employee_tree = Employee.get_tree()
    template = loader.get_template('employees/page.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
        'tr_tag_colors': tr_tag_colors
    }
    return HttpResponse(template.render(context, request))
