from django.http import HttpResponse
from django.views import View


class index(View):

    def get(self, request, a, b):
        return HttpResponse(f'{a} + {b} = {a + b}')
