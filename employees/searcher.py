from .models import Employee
from datetime import datetime


def get_filtered_queryset(filters):
    '''
    Принимает словарь вида:
    filters = {
            'first_name': str,
            'last_name': str,
            'middle_name': str,
            'position': str,
            'employment_date': str,
            'salary': str,
        }
    Возвращает отфильтрованный queryset employees
    '''
    first_name = filters['first_name']
    last_name = filters['last_name']
    middle_name = filters['middle_name']
    position = filters['position']
    employment_date = _convert_date(filters['employment_date'])
    salary = filters['salary']
    return Employee.objects.filter(first_name__icontains=first_name,
                                   last_name__icontains=last_name,
                                   middle_name__icontains=middle_name,
                                   position__icontains=position,
                                   employment_date__icontains=employment_date,
                                   salary__icontains=salary)


def get_ordered_queryset(queryset):
    return queryset.order_by('last_name')


def _convert_date(date_string):
    if date_string:
        return datetime.strptime(date_string, "%d/%m/%Y").date()
    else:
        return ''
