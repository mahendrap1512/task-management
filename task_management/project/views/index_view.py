from datetime import datetime

from common.base_view import BaseView
from django.db.models import Q
from django.shortcuts import render
from project.models import Project


class MainView(BaseView):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            projects = Project.objects.filter((Q(end_date=None) | Q(
                end_date__gt=datetime.now())), client=request.user, is_deleted=False)
            context = {"projects": projects}
            return render(request, 'project_list.html', context=context)
        else:
            return render(request=request, template_name='index.html')
