from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from common.base_view import BaseView
from django.contrib.auth.forms import UserCreationForm


class RegisterView(BaseView):

    def post(self, request, *args, **kwargs):
        # print(request.__dict__)
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('projects')
        else:
            context = {'error': signup_form.errors}
            return render(request, 'error.html', context=context)

    def get(self, request, *args, **kwargs):
        signup_form = UserCreationForm()
        context = {
            "form": signup_form
        }
        return render(request=request, template_name='register.html', context=context)
