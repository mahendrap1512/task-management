from django.views import View
from django.shortcuts import render



class BaseView(View):

    def raise_error(self, request, error_message):
        return render(request=request, template_name="error.html", context={"error": error_message})

    class Meta:
        abstract = True
