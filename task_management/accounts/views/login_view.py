from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from common.base_view import BaseView


class LoginView(BaseView):

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            context = {"error": "Username or password incorrect"}
            return render(request, 'error.html', context)

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='index.html')
