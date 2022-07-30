from django import forms

from .models import Employee


class SearchForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name',)
