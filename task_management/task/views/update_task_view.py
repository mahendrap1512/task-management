from common.base_view import BaseView
from task.models import Task
from task.forms import UpdateTaskForm
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
from project.models import Project


class UpdateTaskView(BaseView):

    def get(self, request, project_id, task_id, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                project = Project.objects.get(id=project_id, is_deleted=False)
                task = Task.objects.get(id=task_id, project_id=project_id, is_deleted=False)
                update_form = UpdateTaskForm()
                context = {
                    "update_form": update_form,
                    "user": request.user,
                    "project": project,
                    "task": task
                }
                return render(request, template_name="update_task.html", context=context)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Project.DoesNotExist:
            return self.raise_error(request, error_message="Invalid project id")
        except Task.DoesNotExist:
            return self.raise_error(request, error_message="Invalid Task id")
        except Exception as error:
            return self.raise_error(request=request, error_message=error)


    def post(self, request, project_id, task_id, *args, **kwargs):
        print("inside post method")
        try:
            if request.user.is_authenticated:
                form = UpdateTaskForm(request.POST)
                if form.is_valid():
                    task = Task.objects.get(id=task_id, project_id=project_id, is_deleted=False)
                    task.status = form.cleaned_data["status"]
                    task.save()
                    return redirect('projects')
                else:
                    return self.raise_error(request=request, error_message=form.errors)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Exception as error:
            return self.raise_error(request=request, error_message=error)
