from .models import Employee


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


def get_ordered_queryset(queryset):
    return queryset.order_by('last_name')
