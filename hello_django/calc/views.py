from django.http import HttpResponse
from django.views import View

class CalcPageView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('calc')
