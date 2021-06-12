from common.base_view import BaseView
from django.shortcuts import render


class MainView(BaseView):

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            return render(request, 'projects.html')
        else:
            return render(request=request, template_name='index.html')
