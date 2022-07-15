from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from hello_django.calc.models import History


class index(View):

    def get(self, request, a, b):
        sum = a + b
        History(value=sum).save()
        return render(request, 'calc/index.html', {'a': a, 'b': b, 'sum': sum})


class history(View):

    def get(self, request):
        context = {}
        # context['results'] = History.objects.all()[0:10]
        context['results'] = History.objects.order_by('-timestamp')[0:10]

        return render(request, 'calc/history.html', context)
