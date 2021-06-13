from common.base_view import BaseView
from django.shortcuts import render, redirect
from project.forms import ProjectForm
from project.models import Project
from datetime import datetime
from django.db.models import Q


class DeleteProjectView(BaseView):

    def get(self, request, project_id, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                project = Project.objects.get(id=project_id, is_deleted=False)
                project.is_deleted=True
                project.save()
                projects = Project.objects.filter((Q(end_date=None) | Q(
                    end_date__gt=datetime.now())), client=request.user, is_deleted=False)
                context = {"projects": projects}
                return render(request, 'project_list.html', context)
            else:
                return self.raise_error(request=request, error_message="Login Required")
        except Exception as error:
            return self.raise_error(request=request, error_message=error)
