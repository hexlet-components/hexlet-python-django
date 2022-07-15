from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class index(View):

    def get(self, request, a, b):
        sum = a + b
        return render(request, 'calc/index.html', {'a': a, 'b': b, 'sum': sum})
