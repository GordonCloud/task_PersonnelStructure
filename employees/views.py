from django.http import HttpResponse
from django.template import loader

from .models import Employee
from .forms import SearchForm
from . import searcher

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
    template = loader.get_template('employees/mainpage.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
        'tr_tag_colors': tr_tag_colors
    }
    return HttpResponse(template.render(context, request))


def searchpage(request):
    if request.method == 'GET':
        employee_director = Employee.objects.get(hierarchy_level=1)
        searchform = SearchForm
        employees_queryset = Employee.objects.order_by('last_name')
        template = loader.get_template('employees/searchpage.html')
        context = {
            'employee_director': employee_director,
            'firm_name': "ОАО Маркиса Де Коте",
            'employees_queryset': employees_queryset,
            'searchform': searchform,
        }
        return HttpResponse(template.render(context, request))

    elif request.method == 'POST':
        filters = {
            'first_name': request.POST["first_name"],
            'last_name': request.POST["last_name"],
            'middle_name': request.POST["middle_name"],
            'position': request.POST["position"],
            'employment_date': request.POST["employment_date"],
            'salary': request.POST["salary"],
        }
        filtered_queryset = searcher.get_filtered_queryset(filters)
        filtered_queryset = \
            searcher.get_ordered_queryset(filtered_queryset)
        template = loader.get_template('employees/searchresults.html')
        context = {
            'employee_queryset': filtered_queryset,
        }
        return HttpResponse(template.render(context, request))
