from django.views import View


class BaseView(View):

    class Meta:
        abstract = True
