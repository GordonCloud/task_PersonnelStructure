from django.http import HttpResponse
from django.template import loader

from .models import Employee
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
    return HttpResponse(request)
#    submitbutton = request.POST.get("submit")
#
 #   firstname = ''
 #   lastname = ''
 #   emailvalue = ''
#
 #   form = UserForm(request.POST or None)
 #   if form.is_valid():
 #       firstname = form.cleaned_data.get("first_name")
 #       lastname = form.cleaned_data.get("last_name")
 #       emailvalue = form.cleaned_data.get("email")

# 1)