import pickle

from django.http import HttpResponse
from django.template import loader

from .models import Employee, EmployeeTree
from .forms import SearchForm

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
    if not EmployeeTree.full_tree:
        EmployeeTree.full_tree = EmployeeTree(Employee.objects.all()).current_tree
    employee_tree = EmployeeTree.full_tree.copy()
    if employee_director in employee_tree:
        employee_tree.remove(employee_director)
    template = loader.get_template('employees/mainpage.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
        'tr_tag_colors': tr_tag_colors
    }
    return HttpResponse(template.render(context, request))


def searchpage(request):
    employee_director = Employee.objects.get(hierarchy_level=1)
    if not EmployeeTree.full_tree:
        EmployeeTree.full_tree = EmployeeTree(Employee.objects.all()).current_tree
    employee_tree = EmployeeTree.full_tree.copy()
    searchform = SearchForm
    template = loader.get_template('employees/searchpage.html')
    context = {
        'employee_director': employee_director,
        'firm_name': "ОАО Маркиса Де Коте",
        'employee_tree': employee_tree,
        'searchform': searchform,
    }
    return HttpResponse(template.render(context, request))


def post_searchform(request):
    if request.method == "POST":
        filters = {
            'first_name': request.POST["first_name"],
            'last_name': request.POST["last_name"],
            'middle_name': request.POST["middle_name"],
            'position': request.POST["position"],
            'employment_date': request.POST["employment_date"],
            'salary': request.POST["salary"],
        }
        filtered_queryset = get_filtered_queryset(filters)
        filtered_tree = EmployeeTree(filtered_queryset).current_tree
        template = loader.get_template('employees/searchresults.html')
        context = {
            'employee_tree': filtered_tree,
        }
        return HttpResponse(template.render(context, request))


def get_filtered_queryset(filters):
    first_name = filters['first_name']
    last_name = filters['last_name']
    middle_name = filters['middle_name']
    position = filters['position']
    employment_date = filters['employment_date']
    salary = filters['salary']
    return Employee.objects.filter(first_name__icontains=first_name,
                                   last_name__icontains=last_name,
                                   middle_name__icontains=middle_name,
                                   position__icontains=position,
                                   employment_date__icontains=employment_date,
                                   salary__icontains=salary)
