from django.http import HttpResponse
from django.template import loader

from .models import Employee


def page(request):
    all_employees = Employee.objects.all()
    template = loader.get_template('employees/page.html')
    context = {
        'AllEmployees': all_employees,
    }
    return HttpResponse(template.render(context, request))
