from django import forms
from django.forms import fields
from project.models import Project


class DateTimeInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=64, required=True)
    description = forms.CharField(max_length=64, required=True)
    start_date = forms.DateField(widget=DateTimeInput)
    end_date = forms.DateField(widget=DateTimeInput)
