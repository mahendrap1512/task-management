from common.base_view import BaseView
from project.models import Project
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime

class ProjectListView(BaseView):

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                projects = Project.objects.filter((Q(end_date=None) | Q(end_date__gt=datetime.now())))
                context = {"projects": projects}
                return render(request, 'project_list.html', context)
            else:
                return render(request=request, template_name="error.html", context={"error": "Login required"})
        except Exception as error:
            return render(request=request, template_name="error.html", context={"error": error})
