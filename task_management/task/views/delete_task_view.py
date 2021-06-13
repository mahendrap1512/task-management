from common.base_view import BaseView
from task.models import Task
from task.forms import UpdateTaskForm
from django.shortcuts import render, redirect
from django.db.models import Q
from datetime import datetime
from project.models import Project


class DeleteTaskView(BaseView):

    def get(self, request, project_id, task_id, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                task = Task.objects.get(id=task_id, project_id=project_id, is_deleted=False)
                task.is_deleted = True
                task.save()
                return redirect('project_task', project_id)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Project.DoesNotExist:
            return self.raise_error(request, error_message="Invalid project id")
        except Task.DoesNotExist:
            return self.raise_error(request, error_message="Invalid Task id")
        except Exception as error:
            return self.raise_error(request=request, error_message=error)