from common.base_view import BaseView
from task.models import Task
from task.forms import TaskForm
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
from project.models import Project


class CreateTaskView(BaseView):

    def get(self, request, project_id, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                project = Project.objects.get(id=project_id)
                form = TaskForm()
                context = {
                    "form": form,
                    "user": request.user,
                    "project": project
                }
                return render(request, template_name="create_task.html", context=context)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Project.DoesNotExist:
            return self.raise_error(request, error_message="Invalid project id")
        except Exception as error:
            return self.raise_error(request=request, error_message=error)


    def post(self, request, project_id, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                form = TaskForm(request.POST)
                if form.is_valid():
                    form_data = {
                        "name": form.cleaned_data['name'],
                        "project_id": str(project_id),
                        "description": form.cleaned_data['description'],
                        "status" : form.cleaned_data['status'],
                    }
                    Task.objects.create(**form_data)
                    return redirect('projects')
                else:
                    return self.raise_error(request=request, error_message=form.errors)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Exception as error:
            return self.raise_error(request=request, error_message=error)
