from common.base_view import BaseView
from project.models import Project
from django.shortcuts import redirect, render
from project.forms import ProjectForm


class ProjectView(BaseView):

    def get(self, request, project_id, *args, **kwargs):
        try:
            project = Project.objects.get(id=project_id, is_deleted=False)
            tasks = project.tasks.filter(is_deleted=False)
            context = {"tasks": tasks, "project": project}
            return render(request, 'project.html', context)
        except Project.DoesNotExist:
            return self.raise_error(request=request, error_message="404 object not found")
        except Exception as error:
            return self.raise_error(request=request, error_message=error)
