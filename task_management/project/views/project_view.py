from common.base_view import BaseView
from project.models import Project
from django.shortcuts import render


class ProjectView(BaseView):

    def get(self, request, project_id, *args, **kwargs):
        try:
            project = Project.objects.get(id=project_id)
            tasks = project.tasks.all()
            context = {"tasks": tasks, "project": project}
            return render(request, 'project.html', context)
        except Project.DoesNotExist:
            render(request=request, template_name="error.html", context={})


    def post(self, request, *args, **kwargs):
        pass

    def delete(self, request, project_id, *args, **kwargs):
        pass







