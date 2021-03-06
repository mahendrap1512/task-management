from common.base_view import BaseView
from django.shortcuts import render, redirect
from project.forms import ProjectForm
from project.models import Project
from datetime import date


class CreateProjectView(BaseView):

    def get(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                form = ProjectForm()
                context = {
                    "form": form,
                    "user": request.user
                }
                return render(request, template_name="create_project.html", context=context)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Exception as error:
            return self.raise_error(request=request, error_message=error)

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                form = ProjectForm(request.POST)
                if form.is_valid():
                    form_data = {
                        "name": form.cleaned_data['name'],
                        "client_id": str(request.user.id),
                        "description": form.cleaned_data['description'],
                        "start_date": form.cleaned_data['start_date'],
                        "end_date": form.cleaned_data.get('end_date', None)
                    }
                    end_date = form_data.get("end_date", None)
                    start_date = form_data["start_date"]
                    if end_date and end_date <= date.today:
                        return self.raise_error(request=request, error_message="End date should be in future")
                    elif end_date and end_date < start_date:
                        return self.raise_error(request=request, error_message="End date should be greater than start date")
                    Project.objects.create(**form_data)
                    return redirect('projects')
                else:
                    return self.raise_error(request=request, error_message=form.errors)
            else:
                return self.raise_error(request=request, error_message="Login Required")

        except Exception as error:
            return self.raise_error(request=request, error_message=error)
