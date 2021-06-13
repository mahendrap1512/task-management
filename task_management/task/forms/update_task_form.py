from django import forms
from task.models import Task


class UpdateTaskForm(forms.Form):
    status = forms.ChoiceField(choices=Task.TaskStatus.choices)
