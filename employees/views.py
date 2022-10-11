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
    employee_tree = EmployeeTree(Employee.objects.all()).employees_tree
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
    searchform = SearchForm
    if not Employee.employees_tree:
        employee_tree = Employee.get_tree()
    else:
        employee_tree = Employee.employees_tree
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
            'first_name' : request.POST["first_name"],
            'last_name' : request.POST["last_name"],
            'middle_name' : request.POST["middle_name"],
            'position' : request.POST["position"],
            'employment_date' : request.POST["employment_date"],
            'salary' : request.POST["salary"],
        }
        if not Employee.employees_tree:
            employee_tree = Employee.get_tree()
        else:
            employee_tree = Employee.employees_tree

       # filtered_tree = filter(def ,employee_tree)
               # (first_name=first_name,
                #                         last_name=last_name,
                 #                        middle_name=middle_name,
                  #                       position=position,
                   #                      employment_date=employment_date,
                    #                     salary=salary)

       # return HttpResponse(filtered_tree)
