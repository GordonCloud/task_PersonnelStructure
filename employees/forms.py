from django.forms import ModelForm, CharField

from .models import Employee


class SearchForm(ModelForm):
    position = CharField(
        max_length=200,
    )

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'middle_name',
                  'position', 'employment_date', 'salary')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
